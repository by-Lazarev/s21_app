# reporting_client_v3.py

import grpc
import reporting_pb2
import reporting_pb2_grpc
import json
import sys
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from models import Base, Spaceship, Officer

# Настройка соединения с базой данных
DATABASE_URL = "postgresql+psycopg2://ender:password@localhost/spaceship_reports"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Сопоставление чисел к строковым значениям для alignment и ship_class
ALIGNMENT_MAP = {
    0: "Ally",
    1: "Enemy"
}

SHIP_CLASS_MAP = {
    0: "Corvette",
    1: "Frigate",
    2: "Cruiser",
    3: "Destroyer",
    4: "Dreadnought",
    5: "Carrier"
}

def scan(coordinates):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reporting_pb2_grpc.ReportingServiceStub(channel)
        request = reporting_pb2.Coordinates(galactic_coordinates=coordinates)
        response_stream = stub.ReportCoordinates(request)
        
        for spaceship in response_stream:
            # Преобразование alignment и ship_class из чисел в строки
            ship_data = {
                'alignment': ALIGNMENT_MAP[spaceship.alignment],
                'name': spaceship.name,
                'ship_class': SHIP_CLASS_MAP[spaceship.ship_class],
                'length': spaceship.length,
                'crew_size': spaceship.crew_size,
                'armed': spaceship.armed,
                'officers': [
                    {
                        'first_name': officer.first_name,
                        'last_name': officer.last_name,
                        'rank': officer.rank
                    } for officer in spaceship.officers
                ]
            }
            
            print("Valid spaceship data:", json.dumps(ship_data, indent=2))
            
            # Сохранение данных в базу данных
            save_spaceship(ship_data)

def save_spaceship(data):
    # Проверка на существование корабля по имени и alignment
    existing_spaceship = session.query(Spaceship).filter_by(name=data['name'], alignment=data['alignment']).first()
    
    if existing_spaceship:
        print(f"Spaceship '{data['name']}' with alignment '{data['alignment']}' already exists.")
        return
    
    # Создание нового объекта Spaceship
    spaceship = Spaceship(
        name=data['name'],
        alignment=data['alignment'],
        ship_class=data['ship_class'],
        length=data['length'],
        crew_size=data['crew_size'],
        armed=data['armed']
    )
    
    # Добавление офицеров к кораблю
    for officer_data in data['officers']:
        officer = Officer(
            first_name=officer_data['first_name'],
            last_name=officer_data['last_name'],
            rank=officer_data['rank'],
            spaceship=spaceship
        )
        spaceship.officers.append(officer)
    
    session.add(spaceship)
    session.commit()

def list_traitors():
    traitors = session.query(Officer.first_name, Officer.last_name, Officer.rank).filter(
        exists().where(
            (Officer.first_name == Officer.first_name) &
            (Officer.last_name == Officer.last_name) &
            (Officer.rank == Officer.rank) &
            (Spaceship.alignment != 'Ally')
        ).where(
            (Officer.spaceship_id == Spaceship.id)
        )
    ).group_by(Officer.first_name, Officer.last_name, Officer.rank).having(
        exists().where(
            (Officer.first_name == Officer.first_name) &
            (Officer.last_name == Officer.last_name) &
            (Officer.rank == Officer.rank) &
            (Spaceship.alignment == 'Ally')
        ).where(
            (Officer.spaceship_id == Spaceship.id)
        )
    ).all()
    
    traitor_list = [
        {"first_name": t[0], "last_name": t[1], "rank": t[2]} for t in traitors
    ]
    
    for traitor in traitor_list:
        print(json.dumps(traitor, indent=2))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: reporting_client_v3.py <command> [<coordinates>]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'scan':
        if len(sys.argv) != 3:
            print("Usage: reporting_client_v3.py scan <coordinates>")
            sys.exit(1)
        coordinates = sys.argv[2]
        scan(coordinates)
    elif command == 'list_traitors':
        list_traitors()
    else:
        print("Unknown command. Available commands: scan, list_traitors")
        sys.exit(1)


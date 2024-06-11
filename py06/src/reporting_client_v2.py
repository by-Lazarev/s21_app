# reporting_client_v2.py

import grpc
import reporting_pb2
import reporting_pb2_grpc
import json
import sys
from models import Spaceship, ValidationError

# Сопоставление чисел к строковым значениям для alignment и ship_class
ALIGNMENT_MAP = {
    reporting_pb2.Alignment.ALLY: "Ally",
    reporting_pb2.Alignment.ENEMY: "Enemy"
}

SHIP_CLASS_MAP = {
    reporting_pb2.Class.CORVETTE: "Corvette",
    reporting_pb2.Class.FRIGATE: "Frigate",
    reporting_pb2.Class.DESTROYER: "Destroyer",
    reporting_pb2.Class.CRUISER: "Cruiser",
    reporting_pb2.Class.DREADNOUGHT: "Dreadnought",
    reporting_pb2.Class.CARRIER: "Carrier"
}

def run(coordinates):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reporting_pb2_grpc.ReportingServiceStub(channel)
        request = reporting_pb2.Coordinates(galactic_coordinates=coordinates)
        response_stream = stub.ReportCoordinates(request)
        for spaceship in response_stream:
            try:
                # Вывод всех полученных данных перед валидацией
                print("Received spaceship data:", spaceship)

                # Преобразование alignment и ship_class из чисел в строки
                validated_spaceship = Spaceship(
                    alignment=ALIGNMENT_MAP[spaceship.alignment],
                    name=spaceship.name,
                    ship_class=SHIP_CLASS_MAP[spaceship.ship_class],
                    length=spaceship.length,
                    crew_size=spaceship.crew_size,
                    armed=spaceship.armed,
                    officers=[{
                        'first_name': officer.first_name,
                        'last_name': officer.last_name,
                        'rank': officer.rank
                    } for officer in spaceship.officers]
                )
                # Вывод валидных данных
                print("Valid spaceship data:", json.dumps(validated_spaceship.dict(), indent=2))
            except ValidationError as e:
                # Игнорируем некорректные записи
                print(f"Invalid spaceship data: {e}")
            except KeyError as e:
                # Обработка случаев, когда нет соответствия в маппинге
                print(f"Invalid spaceship data (mapping error): {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: reporting_client_v2.py <coordinates>")
        sys.exit(1)
    coordinates = sys.argv[1]
    run(coordinates)


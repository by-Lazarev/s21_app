# reporting_server.py

import grpc
import reporting_pb2
import reporting_pb2_grpc
from concurrent import futures
import random

class ReportingService(reporting_pb2_grpc.ReportingServiceServicer):

    def ReportCoordinates(self, request, context):
        ship_classes = [
            reporting_pb2.Class.CORVETTE,
            reporting_pb2.Class.FRIGATE,
            reporting_pb2.Class.DESTROYER,
            reporting_pb2.Class.CRUISER,
            reporting_pb2.Class.DREADNOUGHT,
            reporting_pb2.Class.CARRIER  # Добавлено значение CARRIER
        ]

        class_params = {
            reporting_pb2.Class.CORVETTE: {"length": (80, 250), "crew_size": (4, 10), "armed": True, "hostile": True},
            reporting_pb2.Class.FRIGATE: {"length": (300, 600), "crew_size": (10, 15), "armed": True, "hostile": False},
            reporting_pb2.Class.DESTROYER: {"length": (800, 2000), "crew_size": (50, 80), "armed": True, "hostile": False},
            reporting_pb2.Class.CRUISER: {"length": (500, 1000), "crew_size": (15, 30), "armed": True, "hostile": True},
            reporting_pb2.Class.DREADNOUGHT: {"length": (5000, 20000), "crew_size": (300, 500), "armed": True, "hostile": True},
            reporting_pb2.Class.CARRIER: {"length": (1000, 4000), "crew_size": (120, 250), "armed": False, "hostile": True}  # Добавлено CARRIER
        }

        for _ in range(random.randint(1, 10)):
            ship_class = random.choice(ship_classes)
            params = class_params[ship_class]

            alignment = random.choice([reporting_pb2.Alignment.ALLY, reporting_pb2.Alignment.ENEMY])
            name = "Unknown" if alignment == reporting_pb2.Alignment.ENEMY else f"Ship_{random.randint(1, 100)}"
            length = random.uniform(*params["length"])
            crew_size = random.randint(*params["crew_size"])
            armed = params["armed"]

            spaceship = reporting_pb2.Spaceship(
                alignment=alignment,
                name=name,
                ship_class=ship_class,  # Отправляем числовое значение ship_class
                length=length,
                crew_size=crew_size,
                armed=armed
            )

            if alignment == reporting_pb2.Alignment.ALLY or armed:
                for _ in range(random.randint(0, 10)):
                    officer = reporting_pb2.Officer(
                        first_name=f"FirstName_{random.randint(1, 100)}",
                        last_name=f"LastName_{random.randint(1, 100)}",
                        rank=f"Rank_{random.randint(1, 5)}"
                    )
                    spaceship.officers.append(officer)

            yield spaceship

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reporting_pb2_grpc.add_ReportingServiceServicer_to_server(ReportingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


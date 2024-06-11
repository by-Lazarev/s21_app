# reporting_client.py

import grpc
import reporting_pb2
import reporting_pb2_grpc
import json
import sys

def run(coordinates):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reporting_pb2_grpc.ReportingServiceStub(channel)
        request = reporting_pb2.Coordinates(galactic_coordinates=coordinates)
        response_stream = stub.ReportCoordinates(request)
        for spaceship in response_stream:
            print(json.dumps({
                "alignment": reporting_pb2.Alignment.Name(spaceship.alignment),
                "name": spaceship.name,
                "ship_class": reporting_pb2.Class.Name(spaceship.ship_class),  # Используем ship_class вместо class
                "length": spaceship.length,
                "crew_size": spaceship.crew_size,
                "armed": spaceship.armed,
                "officers": [
                    {
                        "first_name": officer.first_name,
                        "last_name": officer.last_name,
                        "rank": officer.rank
                    } for officer in spaceship.officers
                ]
            }))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: reporting_client.py <coordinates>")
        sys.exit(1)
    coordinates = sys.argv[1]
    run(coordinates)


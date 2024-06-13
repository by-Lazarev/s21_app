# src/game/locations.py

class Location:
    def __init__(self, id: str, name: str, description: str, connections: dict):
        self.id = id
        self.name = name
        self.description = description
        self.connections = connections  # Словарь направлений к соседним локациям

    def get_description(self):
        return self.description

    def get_connections(self):
        return self.connections



import json
import os
from game.locations import Location

def load_map():
    base_path = os.path.dirname(__file__)
    map_file = os.path.join(base_path, "..", "data", "locations.json")

    with open(map_file, "r") as file:
        data = json.load(file)

    locations = {}
    for loc in data:
        location = Location(
            id=loc["id"],
            name=loc["name"],
            description=loc["description"],
            connections=loc["connections"]
        )
        locations[loc["id"]] = location

    return locations

if __name__ == "__main__":
    locations = load_map()
    for loc_id, loc in locations.items():
        print(f"Location {loc_id}: {loc.name}, connections: {loc.connections}")

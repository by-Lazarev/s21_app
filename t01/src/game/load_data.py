# src/game/load_data.py

import json
import os

def load_initial_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "..", "data")

    player_file = os.path.join(data_path, "player_profile.json")
    npc_file = os.path.join(data_path, "npc_data.json")
    enemy_file = os.path.join(data_path, "enemy_data.json")

    with open(player_file, "r") as file:
        player_data = json.load(file)

    with open(npc_file, "r") as file:
        npc_data = json.load(file)

    with open(enemy_file, "r") as file:
        enemy_data = json.load(file)

    return player_data, npc_data, enemy_data

if __name__ == "__main__":
    player_data, npc_data, enemy_data = load_initial_data()
    print("Initial data loaded successfully.")


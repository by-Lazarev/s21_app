# src/game/load_all.py

from game.load_data import load_initial_data
from game.load_map import load_map

def load_all():
    player_data, npc_data, enemy_data = load_initial_data()
    locations = load_map()
    return player_data, npc_data, enemy_data, locations

if __name__ == "__main__":
    player_data, npc_data, enemy_data, locations = load_all()
    print("Data loaded successfully.")


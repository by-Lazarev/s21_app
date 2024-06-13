# src/tests/test_locations.py

import unittest
from game.locations import Location
from game.protagonist import Protagonist

class TestLocations(unittest.TestCase):

    def setUp(self):
        self.loc1 = Location("loc_1", "Starting Point", "You are at the starting point.", {"north": "loc_2", "east": "loc_3"})
        self.loc2 = Location("loc_2", "Northern Point", "You are at the northern point.", {"south": "loc_1"})
        self.loc3 = Location("loc_3", "Eastern Point", "You are at the eastern point.", {"west": "loc_1"})
        self.locations = {"loc_1": self.loc1, "loc_2": self.loc2, "loc_3": self.loc3}
        self.hero = Protagonist(name="Hero", id="player_1")
        self.hero.set_location(self.loc1)

    def test_initial_location(self):
        self.assertEqual(self.hero.whereami(), "You are at the starting point.")

    def test_move_north(self):
        new_location_id = self.hero.go("north")
        self.assertEqual(new_location_id, "loc_2")
        self.hero.set_location(self.locations[new_location_id])
        self.assertEqual(self.hero.whereami(), "You are at the northern point.")

    def test_invalid_move(self):
        result = self.hero.go("west")
        self.assertEqual(result, "You can't go that way.")

if __name__ == "__main__":
    unittest.main()


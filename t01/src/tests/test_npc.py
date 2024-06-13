# src/tests/test_npc.py

import unittest
from game.npc import NPC

class TestNPC(unittest.TestCase):

    def setUp(self):
        self.npc = NPC(name="Old Man", id="npc_1", dialogue=[
            "Hello, traveler!",
            "It's a nice day, isn't it?",
            "Good luck on your journey."
        ])

    def test_talk(self):
        self.assertEqual(self.npc.talk(), "Hello, traveler!")
        self.assertEqual(self.npc.talk(), "It's a nice day, isn't it?")
        self.assertEqual(self.npc.talk(), "Good luck on your journey.")
        self.assertEqual(self.npc.talk(), "End of conversation.")

    def test_receive(self):
        self.assertEqual(self.npc.receive("gold"), "Old Man received gold.")

if __name__ == "__main__":
    unittest.main()


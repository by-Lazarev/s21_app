# src/tests/test_enemy.py

import unittest
from game.enemy import Enemy

class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.goblin = Enemy(name="Goblin", id="enemy_1", hp=5, strength=2, craft=1)

    def test_initial_hp(self):
        self.assertEqual(self.goblin.hp, 5)

    def test_take_hit(self):
        self.assertEqual(self.goblin.take_hit(3), "Goblin has 2 HP left.")
        self.assertEqual(self.goblin.take_hit(2), "Goblin has been defeated.")

if __name__ == "__main__":
    unittest.main()


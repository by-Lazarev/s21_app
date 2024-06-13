import unittest
from game.protagonist import Protagonist
from game.npc import NPC
from game.enemy import Enemy


class TestProtagonist(unittest.TestCase):

    def setUp(self):
        self.hero = Protagonist(name="Hero", id="player_1")
        self.npc = NPC(name="Old Man", id="npc_1", dialogue=[
            "Hello, traveler!",
            "It's a nice day, isn't it?",
            "Good luck on your journey."
        ])
        self.goblin = Enemy(name="Goblin", id="enemy_1", hp=5, strength=2, craft=1)

    def test_initial_hp(self):
        self.assertEqual(self.hero.hp, 10)

    def test_advance_strength(self):
        self.hero.advance_strength(5)
        self.assertEqual(self.hero.strength, 6)

    def test_take_item(self):
        self.hero.take("sword")
        self.assertEqual(self.hero.inventory["sword"], 1)

    def test_take_hit(self):
        self.hero.take_hit(3)
        self.assertEqual(self.hero.hp, 7)

        with self.assertRaises(Exception) as context:
            self.hero.take_hit(10)

        self.assertTrue("You died" in str(context.exception))

    def test_talk_to_npc(self):
        self.assertEqual(self.hero.talk_to(self.npc), "Hello, traveler!")
        self.assertEqual(self.hero.talk_to(self.npc), "It's a nice day, isn't it?")

    def test_give_item_to_npc(self):
        self.hero.take("gold")
        self.assertEqual(self.hero.give(self.npc, "gold"), "Old Man received gold.")
        self.assertEqual(self.hero.give(self.npc, "gold"), "You don't have gold.")

    def test_attack_enemy(self):
        result = self.hero.attack(self.goblin)
        # Зависит от результата боя: "Goblin has X HP left." или "Goblin has been defeated."
        self.assertIn(result, ["Goblin has 4 HP left.", "Goblin has been defeated.", "You have been hit."])



if __name__ == "__main__":
    unittest.main()


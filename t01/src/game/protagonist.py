from collections import defaultdict
from random import randint
from game.locations import Location


class Protagonist:
    def __init__(self, name: str, id: str):
        self.id = id
        self.name = name
        self.hp = 10
        self.strength = 1
        self.craft = 1
        self.inventory = defaultdict(int)
        self.inventory["pocket dust"] = 1
        self.current_location = None  # Текущая локация

    def set_location(self, location: Location):
        self.current_location = location

    def go(self, direction: str):
        if direction in self.current_location.get_connections():
            new_location_id = self.current_location.get_connections()[direction]
            return new_location_id  # Вернуть идентификатор новой локации
        else:
            return "You can't go that way."

    def whereami(self):
        return self.current_location.get_description() if self.current_location else "You are nowhere."

    def talk_to(self, npc):
        return npc.talk()

    def attack(self, enemy):
        player_roll = randint(1, 6) + self.strength
        enemy_roll = randint(1, 6) + enemy.strength

        if player_roll > enemy_roll:
            return enemy.take_hit()
        else:
            self.take_hit(1)
            return "You have been hit."

    def take_hit(self, value=1):
        self.hp -= value
        if self.hp <= 0:
            raise Exception("You died")

    def heal(self, value=1):
        self.hp += value

    def advance_strength(self, value=1):
        self.strength += value

    def advance_craft(self, value=1):
        self.craft += value

    def take(self, item: str):
        self.inventory[item] += 1

    def give(self, npc, item: str):
        if item in self.inventory and self.inventory[item] > 0:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]
            return npc.receive(item)
        else:
            return f"You don't have {item}."

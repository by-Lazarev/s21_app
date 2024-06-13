# src/game/enemy.py

class Enemy:
    def __init__(self, name: str, id: str, hp: int, strength: int, craft: int):
        self.id = id
        self.name = name
        self.hp = hp
        self.strength = strength
        self.craft = craft

    def take_hit(self, value=1):
        self.hp -= value
        if self.hp <= 0:
            return f"{self.name} has been defeated."
        else:
            return f"{self.name} has {self.hp} HP left."

    def attack(self):
        # Логика атаки врага
        pass


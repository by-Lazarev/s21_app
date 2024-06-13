# src/game/npc.py

class NPC:
    def __init__(self, name: str, id: str, dialogue: list):
        self.id = id
        self.name = name
        self.dialogue = dialogue  # Список строк диалога NPC
        self.current_line = 0

    def talk(self):
        if self.current_line < len(self.dialogue):
            response = self.dialogue[self.current_line]
            self.current_line += 1
            return response
        else:
            return "End of conversation."

    def receive(self, item: str):
        return f"{self.name} received {item}."


from game import main, Cheater, Cooperator, Copycat, Grudger, Detective, Player

class Winner(Player):
    def __init__(self):
        super().__init__()

    def action(self, opponent_history):
        if not opponent_history:
            return 'cooperate'

        if opponent_history[0] == 'cheat':
            return 'cheat'
        
        if len(opponent_history) == 2 and opponent_history[1] == 'cheat':
            return 'cheat'

        if len(opponent_history) == 9:
            return 'cheat'

        return 'cooperate'


# Определяем список игроков
players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(), Winner()]

# Вызываем основную функцию, передавая список игроков
main(players)


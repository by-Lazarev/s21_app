from collections import Counter

class Player:
    def __init__(self):
        self.history = []

    def action(self, opponent_history):
        raise NotImplementedError("Этот метод должен быть реализован в подклассах")

    def record(self, action):
        self.history.append(action)

    def reset(self):
        # Очищаем историю игрока
        self.history = []

    def __str__(self):
        return self.__class__.__name__

class Cheater(Player):
    def action(self, opponent_history):
        return 'cheat'

class Cooperator(Player):
    def action(self, opponent_history):
        return 'cooperate'

class Copycat(Player):
    def action(self, opponent_history):
        if not opponent_history:
            return 'cooperate'
        return opponent_history[-1]

class Grudger(Player):
    def action(self, opponent_history):
        if 'cheat' in opponent_history:
            return 'cheat'
        return 'cooperate'

class Detective(Player):
    def __init__(self):
        super().__init__()
        self.turns = ['cooperate', 'cheat', 'cooperate', 'cooperate']
        self.detected_cheat = False

    def action(self, opponent_history):
        # Первые четыре хода следуем шаблону
        if len(self.history) < 4:
            action = self.turns[len(self.history)]
            # Проверяем, обманул ли противник хотя бы раз в первых четырех ходах
            if opponent_history and opponent_history[-1] == 'cheat':
                self.detected_cheat = True
            return action
        
        # Если обнаружен обман, переключаемся на Copycat
        if self.detected_cheat:
            return opponent_history[-1]
        
        # Если обман не был обнаружен, становимся Cheater
        return 'cheat'

class Game:
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
        self.winners = Counter()

    def play(self, player1, player2):
        player1.reset()
        player2.reset()

        print("#" * 60)
        print(f"# {'Match started:'.center(56)} #")
        print(f"# {f'{player1} vs {player2}'.center(56)} #")
        print("#" * 60)
        
        score1 = 0
        score2 = 0
        
        for _ in range(self.matches):
            action1 = player1.action(player2.history)
            action2 = player2.action(player1.history)
            player1.record(action1)
            player2.record(action2)
            score1, score2 = self.update_scores(score1, score2, action1, action2)

        if score1 > score2:
            winner = str(player1)
            self.winners[winner] += 1
        elif score2 > score1:
            winner = str(player2)
            self.winners[winner] += 1
        else:
            winner = "Draw"

        self.registry[str(player1)] += score1
        self.registry[str(player2)] += score2

        print(f"# {'Winner:'.center(56)} #")
        print(f"# {winner.center(56)} #")
        print(f"# {f'{player1}: {score1} candies'.center(56)} #")
        print(f"# {f'{player2}: {score2} candies'.center(56)} #")
        print("#" * 60)
        print()

    def update_scores(self, score1, score2, action1, action2):
        if action1 == 'cooperate' and action2 == 'cooperate':
            score1 += 2
            score2 += 2
        elif action1 == 'cheat' and action2 == 'cooperate':
            score1 += 3
            score2 -= 1
        elif action1 == 'cooperate' and action2 == 'cheat':
            score1 -= 1
            score2 += 3
        elif action1 == 'cheat' and action2 == 'cheat':
            score1 += 0
            score2 += 0
        return score1, score2

    def top3(self):
        print("\n" + "#" * 60)
        print(f"# {'Top 3 players by score:'.center(56)} #")
        top_three = self.registry.most_common(3)
        for player, score in top_three:
            print(f"# {f'{player.lower()} {score}'.center(56)} #")
        
        print("\n" + "#" * 60)
        print(f"# {'Top 3 players by number of wins:'.center(56)} #")
        top_winners = self.winners.most_common(3)
        for player, wins in top_winners:
            print(f"# {f'{player.lower()} {wins}'.center(56)} #")
        print("#" * 60)

def main(players):
    game = Game()

    for i, player1 in enumerate(players):
        for player2 in players[i + 1:]:
            game.play(player1, player2)

    game.top3()

if __name__ == "__main__":
    players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective()]
    main(players)


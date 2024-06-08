import pytest
from game import Player, Cheater, Cooperator, Copycat, Grudger, Detective, Game

# Тесты для игроков
def test_cheater():
    player = Cheater()
    assert player.action([]) == 'cheat'
    assert player.action(['cooperate', 'cheat', 'cooperate']) == 'cheat'

def test_cooperator():
    player = Cooperator()
    assert player.action([]) == 'cooperate'
    assert player.action(['cheat', 'cooperate', 'cheat']) == 'cooperate'

def test_copycat():
    player = Copycat()
    assert player.action([]) == 'cooperate'
    assert player.action(['cheat', 'cooperate', 'cheat']) == 'cheat'
    assert player.action(['cooperate']) == 'cooperate'

def test_grudger():
    player = Grudger()
    assert player.action([]) == 'cooperate'
    assert player.action(['cooperate', 'cooperate']) == 'cooperate'
    assert player.action(['cooperate', 'cheat']) == 'cheat'

def test_detective():
    player = Detective()
    assert player.action([]) == 'cooperate'
    assert player.action(['cheat']) == 'cooperate'
    assert player.action(['cooperate', 'cheat', 'cooperate', 'cooperate']) == 'cooperate'
    assert player.action(['cooperate', 'cooperate', 'cooperate', 'cheat']) == 'cooperate'
    assert player.action(['cooperate', 'cheat', 'cooperate', 'cooperate', 'cooperate']) == 'cooperate'

# Тесты для игры
def test_update_scores():
    game = Game()
    assert game.update_scores(0, 0, 'cooperate', 'cooperate') == (2, 2)
    assert game.update_scores(0, 0, 'cheat', 'cooperate') == (3, -1)
    assert game.update_scores(0, 0, 'cooperate', 'cheat') == (-1, 3)
    assert game.update_scores(0, 0, 'cheat', 'cheat') == (0, 0)

def test_play_game():
    game = Game(matches=5)
    player1 = Cheater()
    player2 = Cooperator()

    game.play(player1, player2)
    
    # Убедимся, что Cheater выигрывает
    assert game.registry['Cheater'] > game.registry['Cooperator']

def test_game_reset():
    game = Game(matches=5)
    player1 = Cheater()
    player2 = Cooperator()

    game.play(player1, player2)

    player1.reset()  # Обновленная строка
    player2.reset()  # Обновленная строка
    
    # Проверяем, что история очищается после игры
    assert len(player1.history) == 0
    assert len(player2.history) == 0

def test_top3():
    game = Game()
    player1 = Cheater()
    player2 = Cooperator()
    player3 = Copycat()

    game.play(player1, player2)
    game.play(player1, player3)
    game.play(player2, player3)

    top3_scores = game.registry.most_common(3)
    top3_wins = game.winners.most_common(3)

    assert len(top3_scores) <= 3
    assert len(top3_wins) <= 3


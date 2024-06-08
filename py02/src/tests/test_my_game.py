import pytest
from game import Cheater, Cooperator, Copycat, Grudger, Detective, Game
from my_game import Winner

def test_winner():
    player = Winner()
    assert player.action([]) == 'cooperate'
    assert player.action(['cheat']) == 'cheat'
    assert player.action(['cooperate', 'cheat']) == 'cheat'
    assert player.action(['cooperate'] * 9) == 'cheat'

def test_game_with_winner():
    game = Game(matches=5)
    player1 = Winner()
    player2 = Cheater()

    game.play(player1, player2)
    

def test_main_function(capsys):
    from my_game import players, main

    main(players)
    
    captured = capsys.readouterr()
    assert "Top 3 players by score" in captured.out
    assert "Top 3 players by number of wins" in captured.out


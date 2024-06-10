import pytest
from personality import turrets_generator

def test_traits_sum():
    turret = turrets_generator()
    total = turret.neuroticism + turret.openness + turret.conscientiousness + turret.extraversion + turret.agreeableness
    assert total == 100, f"Sum of traits should be 100, but got {total}"

def test_traits_are_integers():
    turret = turrets_generator()
    assert isinstance(turret.neuroticism, int), "Neuroticism should be an integer"
    assert isinstance(turret.openness, int), "Openness should be an integer"
    assert isinstance(turret.conscientiousness, int), "Conscientiousness should be an integer"
    assert isinstance(turret.extraversion, int), "Extraversion should be an integer"
    assert isinstance(turret.agreeableness, int), "Agreeableness should be an integer"

def test_methods_exist_and_work(capsys):
    turret = turrets_generator()
    
    # Проверяем метод shoot
    turret.shoot()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Shooting", f"Expected 'Shooting', but got {captured.out.strip()}"

    # Проверяем метод search
    turret.search()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Searching", f"Expected 'Searching', but got {captured.out.strip()}"

    # Проверяем метод talk
    turret.talk()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Talking", f"Expected 'Talking', but got {captured.out.strip()}"


def test_personality_distribution():
    # Проверяем распределение личностных черт, чтобы они были в пределах 0-100
    turret = turrets_generator()
    assert 0 <= turret.neuroticism <= 100, "Neuroticism should be between 0 and 100"
    assert 0 <= turret.openness <= 100, "Openness should be between 0 and 100"
    assert 0 <= turret.conscientiousness <= 100, "Conscientiousness should be between 0 and 100"
    assert 0 <= turret.extraversion <= 100, "Extraversion should be between 0 and 100"
    assert 0 <= turret.agreeableness <= 100, "Agreeableness should be between 0 and 100"


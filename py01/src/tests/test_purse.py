import pytest
from purse import add_ingot, get_ingot, empty, split_booty

def test_add_ingot_squeak(capsys):
    purse = {"gold_ingots": 1}
    result = add_ingot(purse)
    captured = capsys.readouterr()
    assert captured.out == "SQUEAK\n"
    assert result == {"gold_ingots": 2}

def test_get_ingot_squeak(capsys):
    purse = {"gold_ingots": 2}
    result = get_ingot(purse)
    captured = capsys.readouterr()
    assert captured.out == "SQUEAK\n"
    assert result == {"gold_ingots": 1}

def test_empty_squeak(capsys):
    purse = {"gold_ingots": 1}
    result = empty(purse)
    captured = capsys.readouterr()
    assert captured.out == "SQUEAK\n"
    assert result == {}

def test_add_ingot():
    # Тесты для функции add_ingot
    assert add_ingot({}) == {"gold_ingots": 1}
    assert add_ingot({"gold_ingots": 1}) == {"gold_ingots": 2}
    assert add_ingot({"gold_ingots": 1, "stones": 3}) == {"gold_ingots": 2, "stones": 3}
    assert add_ingot({"stones": 3}) == {"gold_ingots": 1, "stones": 3}

def test_get_ingot():
    # Тесты для функции get_ingot
    assert get_ingot({}) == {}
    assert get_ingot({"gold_ingots": 1}) == {}
    assert get_ingot({"gold_ingots": 2}) == {"gold_ingots": 1}
    assert get_ingot({"gold_ingots": 2, "stones": 3}) == {"gold_ingots": 1, "stones": 3}
    assert get_ingot({"stones": 3}) == {"stones": 3}

def test_empty():
    # Тесты для функции empty
    assert empty({}) == {}
    assert empty({"gold_ingots": 1}) == {}
    assert empty({"gold_ingots": 2, "stones": 3}) == {}
    assert empty({"stones": 3}) == {}

def test_combined_operations():
    # Тесты для комбинаций операций
    purse = {}
    purse = add_ingot(purse)
    assert purse == {"gold_ingots": 1}
    purse = add_ingot(purse)
    assert purse == {"gold_ingots": 2}
    purse = get_ingot(purse)
    assert purse == {"gold_ingots": 1}
    purse = get_ingot(purse)
    assert purse == {}
    purse = empty(purse)
    assert purse == {}

    # Композиция функций
    assert add_ingot(get_ingot(add_ingot(empty(purse)))) == {"gold_ingots": 1}
    assert get_ingot(add_ingot(add_ingot(empty(purse)))) == {"gold_ingots": 1}
    assert empty(add_ingot(add_ingot(empty(purse)))) == {}

def sort_purses(purses):
    # Вспомогательная функция для сортировки кошельков по количеству слитков
    return sorted(purses, key=lambda p: p.get("gold_ingots", 0))

def test_split_booty():
    # Тесты для функции split_booty
    result = split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10})
    expected = ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})
    assert sort_purses(result) == sort_purses(expected)

    result = split_booty({"gold_ingots": 5}, {"gold_ingots": 1})
    expected = ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 2})
    assert sort_purses(result) == sort_purses(expected)

    result = split_booty({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
    expected = ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
    assert sort_purses(result) == sort_purses(expected)

    result = split_booty({"gold_ingots": 1})
    expected = ({"gold_ingots": 1}, {"gold_ingots": 0}, {"gold_ingots": 0})
    assert sort_purses(result) == sort_purses(expected)

    result = split_booty()
    expected = ({"gold_ingots": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
    assert sort_purses(result) == sort_purses(expected)

if __name__ == "__main__":
    pytest.main()


import pytest
from key import Key


def test_instance_is_list():
    key = Key()
    assert isinstance(key, list), "Экземпляр Key должен считаться списком"

def test_comparison_with_int():
    key = Key()
    try:
        result = (key == 1)
        result = (key != 1)
        result = (key < 1)
        result = (key > 1)
        result = (key <= 1)
        result = (key >= 1)
    except TypeError:
        pytest.fail("Экземпляр Key должен поддерживать сравнение с int без TypeError")

def test_length_comparison():
    key = Key([1, 2, 3])
    dummy_list = [1, 2, 3]
    assert len(key) < len(dummy_list), "Длина экземпляра Key должна быть меньше длины списка"


import pytest
from decypher import decypher

def test_decypher():
    # Тестовые случаи
    test_cases = [
        ("Have you delivered eggplant pizza at restored keep?", "HYDEPARK"),
        ("The quick brown fox jumps over the lazy dog", "TQBFJOTLD"),
        ("A big black bear sat on a big black rug", "ABBBSOABBR"), 
        ("Can you keep a secret?", "CYKAS"),
        ("Why did you bring me here?", "WDYBMH"),
        ("Be careful around", "BCA"),
        ("", ""),  # Пустая строка
        ("Single", "S"),  # Одиночное слово
        ("MULTI Words with DIFFERENT casing", "MWWDC")  # Смешанный регистр
    ]
    
    for message, expected in test_cases:
        assert decypher(message) == expected

if __name__ == "__main__":
    pytest.main()


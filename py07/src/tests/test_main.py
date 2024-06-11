# test_main.py

import pytest
import json
from unittest.mock import patch
from io import StringIO
import main
import questions_loader

@pytest.fixture
def sample_questions():
    return [
        {
            "question": "What is your favorite color?",
            "answers": ["Red", "Blue", "Green", "Yellow"]
        }
    ]

@pytest.fixture
def mock_questions_file(tmp_path, sample_questions):
    questions_file = tmp_path / "questions.json"
    with open(questions_file, 'w') as file:
        json.dump(sample_questions, file)
    return str(questions_file)

@patch('builtins.input', side_effect=['1', '12', '70', '1', '2'])
def test_scan_command(mock_input, mock_questions_file):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('sys.argv', ['main.py', 'test', mock_questions_file]):
            main.main()
        output = mock_stdout.getvalue()
        # Проверяем, что вопрос был задан и что определение "Human" появилось в выводе
        assert "What is your favorite color?" in output
        assert "The subject is determined to be a Human." in output

def test_unknown_command():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('sys.argv', ['main.py', 'unknown']):
            main.main()
        output = mock_stdout.getvalue()
        assert "Unknown command" in output


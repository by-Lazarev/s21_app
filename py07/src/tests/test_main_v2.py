# tests/test_main_v2.py

import pytest
from unittest.mock import patch
from io import StringIO
import main_v2
import json

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

def test_empty_questions_file(tmp_path):
    questions_file = tmp_path / "empty_questions.json"
    questions_file.write_text("[]")

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('sys.argv', ['main_v2.py', 'test', str(questions_file)]):
            with pytest.raises(SystemExit) as excinfo:
                main_v2.main()
            assert excinfo.value.code == 1
            output = mock_stdout.getvalue()
            assert "The questions file is empty." in output

@patch('builtins.input', side_effect=['0', '1', '12', '70', '1', '2'])
def test_invalid_answer_number(mock_input, mock_questions_file):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('sys.argv', ['main_v2.py', 'test', mock_questions_file]):
            main_v2.main()
        output = mock_stdout.getvalue()
        assert "Invalid answer number." in output
        assert "Please enter a valid number corresponding to one of the answers." in output



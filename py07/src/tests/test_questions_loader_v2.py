# tests/test_questions_loader_v2.py

import pytest
import json
from questions_loader_v2 import load_questions

def test_load_questions(tmp_path):
    questions_data = [
        {
            "question": "What is your favorite color?",
            "answers": ["Red", "Blue", "Green", "Yellow"]
        }
    ]
    questions_file = tmp_path / "questions.json"
    with open(questions_file, 'w') as file:
        json.dump(questions_data, file)

    loaded_questions = load_questions(questions_file)
    assert loaded_questions == questions_data

def test_load_empty_questions_file(tmp_path):
    questions_file = tmp_path / "empty_questions.json"
    questions_file.write_text("[]")

    loaded_questions = load_questions(questions_file)
    assert loaded_questions == []


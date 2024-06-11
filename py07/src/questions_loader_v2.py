# questions_loader_v2.py

import json

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)


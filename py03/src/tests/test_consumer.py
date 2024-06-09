import pytest
import json
from consumer import process_message

def test_process_message():
    message = {
        "metadata": {"from": "1111111111", "to": "2222222222"},
        "amount": 10000
    }
    bad_accounts = ["2222222222"]
    raw_message = {"type": "message", "data": json.dumps(message)}

    processed = process_message(raw_message, bad_accounts)
    assert processed["metadata"]["from"] == "2222222222"
    assert processed["metadata"]["to"] == "1111111111"
    assert processed["amount"] == 10000

def test_process_message_negative_amount():
    message = {
        "metadata": {"from": "1111111111", "to": "2222222222"},
        "amount": -3000
    }
    bad_accounts = ["2222222222"]
    raw_message = {"type": "message", "data": json.dumps(message)}

    processed = process_message(raw_message, bad_accounts)
    assert processed["metadata"]["from"] == "1111111111"
    assert processed["metadata"]["to"] == "2222222222"
    assert processed["amount"] == -3000


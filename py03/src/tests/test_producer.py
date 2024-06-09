import json
import redis
import pytest
from producer import generate_message

def test_generate_message():
    message = generate_message()
    assert "metadata" in message
    assert "from" in message["metadata"]
    assert "to" in message["metadata"]
    assert "amount" in message
    assert len(message["metadata"]["from"]) == 10
    assert len(message["metadata"]["to"]) == 10
    assert isinstance(message["amount"], int)

def test_redis_publish(monkeypatch):
    mock_redis = redis.Redis()
    monkeypatch.setattr(mock_redis, 'publish', lambda channel, message: 1)
    
    assert mock_redis.publish('test_channel', json.dumps({"test": "message"})) == 1


import threading
import requests
import pytest
from wsgiref.simple_server import make_server
from credentials import application

# Запускаем сервер в фоновом потоке
@pytest.fixture(scope="module", autouse=True)
def start_server():
    server = make_server('127.0.0.1', 8888, application)
    thread = threading.Thread(target=server.serve_forever)
    thread.setDaemon(True)
    thread.start()
    yield
    server.shutdown()

def test_known_species():
    url = "http://127.0.0.1:8888/?species=Time%20Lord"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"credentials": "Rassilon"}

def test_unknown_species():
    url = "http://127.0.0.1:8888/?species=UnknownSpecies"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {"credentials": "Unknown"}

def test_no_species():
    url = "http://127.0.0.1:8888/"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {"credentials": "Unknown"}

def test_human_species():
    url = "http://127.0.0.1:8888/?species=Human"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"credentials": "Doctor"}

def test_dalek_species():
    url = "http://127.0.0.1:8888/?species=Dalek"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"credentials": "Exterminate"}

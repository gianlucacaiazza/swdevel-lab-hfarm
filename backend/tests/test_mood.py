import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app.main import app

client = TestClient(app)

def test_find_songs_for_party():
    response = client.get("/mood/party")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 

def test_find_songs_for_chill():
    response = client.get("/mood/chill")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_find_songs_for_workout():
    response = client.get("/mood/workout")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_songs_for_passion():
    response = client.get("/mood/passion")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_discover_random_song():
    response = client.get("/mood/discover")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
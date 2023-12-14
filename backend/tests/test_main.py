import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app


"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_provider_name_exists():
    # Test when the provider name exists in the CSV
    response = client.get("/module/lookfor/Sorgenia")
    assert response.status_code == 200
    assert response.json() == [
        {
            'localita': 'Via algardi alessandro 4',
            'tipologia': 'N',
            'numero_col': '5'
        }
    ]


def test_provider_name_does_not_exist():
    # Test when the provider name does not exist in the CSV
    response = client.get("/module/lookfor/pippo")
    assert response.json() == []


def test_case_insensitivity():
    # Test case insensitivity for provider names
    response_1 = client.get("/module/lookfor/SoRgEnIa")
    response_2 = client.get("/module/lookfor/sorgenia")
    response_3 = client.get("/module/lookfor/SORGENIA")
    assert response_1.json() == response_2.json() == response_3.json()

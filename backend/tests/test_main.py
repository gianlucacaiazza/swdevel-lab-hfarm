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

def test_street_name_exists():
    # Replace this with your actual API endpoint and client setup
    response12 = client.get("/module/search/CORSO INDIPENDENZA")
    excepted_response12 = "The provider for the charging station present in CORSO INDIPENDENZA is A2A Energy Solutions"
    assert response12.status_code == 200
    assert response12.json() == excepted_response12


def test_street_name_does_not_exist():
    # Test when the provider name does not exist in the CSV
    response = client.get("/module/search/VIA CASALSERUGO")
    expected_error = "Unfortunately the street name you inserted is not present in our database"
    assert response.json() == expected_error


def test_case_insensitivity_street_name():
    #Test case insensitivity for provider names
    response_1 = client.get("/module/search/ViALaRgA")
    response_2 = client.get("/module/search/VIALARGA")
    response_3 = client.get("/module/search/vialarga")
    assert response_1.json() == response_2.json() == response_3.json()


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


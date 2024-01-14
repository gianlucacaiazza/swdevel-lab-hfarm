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


def test_success_read_item():
    response = client.get("/query/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == {"person_name": 'Albert Einstein', 
                               "birthday": '03/14/1879'}


""" def test_fail_read_item():
    response = client.get("/query/Pippo")
    assert response.status_code == 200
    assert response.json() == {"error": "Person not found"} """


# The following will generate an error in pycheck
""" def test_success_read_item_module():
    response = client.get("/module/search/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == {"Albert Einstein's birthday is 03/14/1879."} """


# The following is correct, can you spot the diffence?
def test_success_read_item_module():
    response = client.get("/module/search/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == ["Albert Einstein's birthday is 03/14/1879."]






import pytest
from fastapi.testclient import TestClient
from app.mymodules.feature_2_best_school_in_town import best_school_in_town  # Assuming your main module is in a directory named "app"

# Create a client for testing
client = TestClient(app)

# Tests for the best_school_in_town function

def test_best_school_in_town_valid():
    # Test with valid data
    response = client.get('/best-school/Milan/primary')  # Replace 'Milan' with a city and 'primary' with a valid school level
    assert response.status_code == 200
    data = response.json()
    assert 'School Name' in data
    assert 'Services' in data
    assert 'Service Count' in data

def test_best_school_in_town_invalid_city():
    # Test with a city not present in the data
    response = client.get('/best-school/InvalidCity/primary')
    assert response.status_code == 200
    data = response.json()
    assert data == "No data available for the specified city and school level."

def test_best_school_in_town_invalid_level():
    # Test with a school level not present in the data
    response = client.get('/best-school/Milan/invalid_level')
    assert response.status_code == 200
    data = response.json()
    assert data == "No data available for the specified city and school level."

# feat_1

# Tests for the elenco_scuole_con_infrastrutture function

def test_elenco_scuole_con_infrastrutture_valid():
    # Test with valid data
    response = client.post('/elenco-scuole-con-infrastrutture', json={
        "nome_provincia": "Veneto",
        "infrastrutture": ["Mensa", "Palestra Piscina"]
    })
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_elenco_scuole_con_infrastrutture_invalid_provincia():
    # Test with an invalid province
    response = client.post('/elenco-scuole-con-infrastrutture', json={
        "nome_provincia": "InvalidProvince",
        "infrastrutture": ["Mensa", "Palestra Piscina"]
    })
    assert response.status_code == 200
    data = response.json()
    assert data == "Errore: provincia non esistente."

def test_elenco_scuole_con_infrastrutture_empty_infrastrutture():
    # Test with empty infrastructure list
    response = client.post('/elenco-scuole-con-infrastrutture', json={
        "nome_provincia": "Veneto",
        "infrastrutture": []
    })
    assert response.status_code == 200
    data = response.json()
    assert data == "Errore: nessuna infrastruttura specificata."

def test_elenco_scuole_con_infrastrutture_invalid_infrastruttura():
    # Test with an invalid infrastructure column
    response = client.post('/elenco-scuole-con-infrastrutture', json={
        "nome_provincia": "Veneto",
        "infrastrutture": ["InvalidInfrastruttura"]
    })
    assert response.status_code == 200
    data = response.json()
    assert data == "Errore: colonna 'InvalidInfrastruttura' non presente nel dataset."

def test_elenco_scuole_con_infrastrutture_no_data():
    # Test with no schools found
    response = client.post('/elenco-scuole-con-infrastrutture', json={
        "nome_provincia": "Veneto",
        "infrastrutture": ["Palestra Piscina"]
    })
    assert response.status_code == 200
    data = response.json()
    assert data == "Nessuna scuola trovata con le infrastrutture specificate nella provincia data."

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
    

def test_numbers_of_stations_exists():
    # Test when the street name exists in the CSV
    response = client.get("/get_charging_stations/VIA LARGA")
    assert response.status_code == 200
    expected_response = {"street_name": "VIA LARGA", "number_stations": "3"}
    assert response.json() == expected_response
    

def test_numbers_of_stations_does_not_exist():
    # Test when the street name does not exist in the CSV
    response = client.get("/get_charging_stations/NONEXISTENTSTREET")
    assert response.status_code == 200
    expected_error = {"error": f"The street 'NONEXISTENTSTREET' is not present in the dataset."}
    assert response.json() == expected_error
    

def test_socket_types_exists():
    response= client.get("/socket_types_by_zone/VIA LARGA 7")
    assert response.status_code == 200
    expected_response = {"zone": "VIA LARGA 7", "socket type": ["AC Normal"]}
    assert response.json() == expected_response
    

def test_socket_types_does_not_exist():
    response= client.get("/socket_types_by_zone/NONEXISTENTZONE")
    assert response.status_code == 500
    expected_error = {'detail':''}
    assert response.json() == expected_error


def test_case_insensitivity():
    # Test case insensitivity for provider names
    response_1 = client.get("/module/lookfor/SoRgEnIa")
    response_2 = client.get("/module/lookfor/sorgenia")
    response_3 = client.get("/module/lookfor/SORGENIA")
    assert response_1.json() == response_2.json() == response_3.json()


def test_case_insensitivity_charg_points():
    # Test case insensitivity for street names
    response_1 = client.get("/get_charging_points/VIA LARGA")
    response_2 = client.get("/get_charging_points/via larga")
    response_3 = client.get("/get_charging_points/Via Larga")
    assert response_1.json() == response_2.json() == response_3.json()
    

def test_case_insensitivity_socket_types():
    # Test case insensitivity for charging_stations
    response_1 = client.get("/socket_types_by_zone/ViA lArGa 7")
    response_2 = client.get("/socket_types_by_zone/via larga 7")
    response_3 = client.get("/socket_types_by_zone/VIA LARGA 7")
    assert response_1.json() == response_2.json() == response_3.json()















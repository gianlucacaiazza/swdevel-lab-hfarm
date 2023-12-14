import os
import sys
from fastapi.testclient import TestClient
import pandas as pd

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app
from app.mymodules.Destination_random import randomize_destination
from app.mymodules.df_integrations import flights


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

def test_success_destinations():
    departure = 'LONDON - LGW'
    response = client.get('/get_airport')
    assert response.status_code == 200
    print(response.json())

test_success_destinations()

def test_randomize_destination_valid_input():
    # Test with a valid departure airport
    departure = 'LONDONR'
    response = client.get('/query/{departure}')
    assert response.status_code == 200
    print(response.json())

def test_randomize_destination_invalid_input():
    # Test with an invalid departure airport
    departure = 'QWETHCSSDH'
    response = client.get('/query/{departure}')
    assert response.status_code == 200
    if response == ['No departure found']:
        return True

def test_randomize_destination_empty_df():
    # Test with an empty dataframe
    empty_df = pd.DataFrame()
    departure = 'ROME'
    response = randomize_destination(departure, empty_df)
    print (response)

test_randomize_destination_valid_input()

import os
import sys
from fastapi.testclient import TestClient
import pandas as pd
import json

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app
from app.mymodules.Destination_random import randomize_destination
from app.mymodules.Feature_1_avg_price import calculate_average_price
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
    assert json.loads(response.json()) == {"person_name": 'Albert Einstein', 
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


def test_avg_price_valid_input():
    '''We are checking wheter the algorithm is correctly calculating the average price with a valid input'''
    response = client.get('/LONDON - LGW/MANCHESTER')
    assert response.status_code == 200
    assert response.json() == 99.59571428571427

def test_avg_price_invalid_input():
    '''We are checking wheter the algorithm is correctly behaving with an invalid input, in this case there is not a direct connection 
    between AMSTERDAM and FUERTEVENTURA so it shouldn't calculate any output'''
    response = client.get('/AMSTERDAM/FUERTEVENTURA')
    assert response.status_code == 200
    assert response.json() == None

# The following is correct, can you spot the diffence?
def test_success_read_item_module():
    response = client.get("/module/search/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == ["Albert Einstein's birthday is 03/14/1879."]

def test_cheapest_to_fly():
    response = client.get('LONDON - LGW')
    assert response.status_code == 200

def test_randomize_destination_empty_df():
    # Test with an empty dataframe
    empty_df = pd.DataFrame()
    departure = 'ROME'
    response = randomize_destination(departure, empty_df)
    print (response)

def test_average_class_price():
    # Test with valid input
    response = client.get('/FLYBE')
    assert response.status_code == 200
    assert response.json() == 'Average Price ECONOMY: 114.62 £Average Price FIRST: 46.95 £'

def test_average_one_class():
    # Test 
    response = client.get('/AEROMEXICO')
    assert response.status_code == 200
    assert response.json() == 'Average Price ECONOMY: 128.10 £ The airline only has ECONOMY class flights'

def test_get_arrivals():
    response = client.get('/get_arrivals')
    assert response.status_code == 200
    print(response.json())

def test_get_img():
    response = client.get('/img-LONDON - LGW')
    assert response.status_code == 200
    print(response.json())

def test_combined_endpoint_valid_departure():
    # Test with a valid departure airport
    response = client.get('/random/LONDON - LGW')
    assert response.status_code == 200
    data = response.json()  # or the expected data type
    print(data)

def test_combined_endpoint_invalid_departure():
    # Test with an invalid departure airport
    departure = 'INVALID_AIRPORT'
    response = client.get(f"/random/{departure}")
    assert response.status_code == 200
    data = response.json()
    # Expecting an error message or empty response based on API design
    assert data == ['No departure found'] or 'error' in data
    print(data)



import os
import sys
from fastapi.testclient import TestClient
import pandas as pd
import json

from app.main import app
from app.mymodules.feat_2_random import randomize_destination
from app.mymodules.feat_3_class_price import calculate_average_price_airline
from app.mymodules.df_integrations import flights
from app.mymodules.cleaning import clean_cost

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import

"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_avg_price_valid_input():
    '''We are checking wheter the algorithm is correctly
    calculating the average price with a valid input'''
    response = client.get('/avg/LONDON - LGW/MANCHESTER')
    assert response.status_code == 200
    assert response.json() == '99.60'


def test_avg_price_invalid_input():
    '''We are checking wheter the algorithm is correctly behaving
    with an invalid input, in this case there is not a direct connection
    between AMSTERDAM and FUERTEVENTURA so it shouldn't calculate any output'''
    response = client.get('/avg/AMSTERDAM/FUERTEVENTURA')
    assert response.status_code == 200
    assert response.json() == None


def test_cheapest_to_fly():
    response = client.get('/arrival-LONDON - LGW')
    assert response.status_code == 200
    assert response.json() == {'Air Carrier': 'EASYJET', 'Price in £': 75.64}


def test_randomize_destination_empty_df():
    # Test with an empty dataframe
    empty_df = pd.DataFrame()
    departure = 'ROME'
    response = randomize_destination(departure, empty_df)


def test_average_class_price():
    # Test with valid input
    response = client.get('/airlines-FLYBE')
    assert response.status_code == 200
    assert response.json() == 'Average Price ECONOMY: 114.62 £Average Price FIRST: 46.95 £'


def test_average_one_class():
    # Test 
    response = client.get('/airlines-AEROMEXICO')
    assert response.status_code == 200
    assert response.json() == 'Average Price ECONOMY: 128.10 £ The airline only has ECONOMY class flights'


def test_get_airline():
    response = client.get('/get_airline')

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response
    json_response = response.json()

    expected_airlines = '["FLYBE","EASYJET","BRITISH AIRWAYS","ALITALIA","AER LINGUS","AIR SOUTHWEST","SWISS AIRLINES","BRITISH MIDLAND","MIDDLE EAST AIRLINES","RYANAIR","AIR FRANCE","CYPRUS AIRWAYS","EASTERN AIRWAYS","BLUEISLANDS","KLM","VIRGIN ATLANTIC","AURIGNY AIR SERVICES","DO NOT USE - EASYJET - PLEASE ","SN BRUSSELS AIRLINES","LUFTHANSA","BMI BABY","LUXAIR S.A.","SCANDINAVIAN AIRLINES","AIR CANADA","ICELAND AIRWAYS","MALEV - HUNGARIAN","MONARCH AIRLINES","NORWEGIAN AIR SHUTTLE A.","WIZZAIR","FINNAIR","IBERIA","AIR BERLIN","CHINA EASTERN AIRLINES","CATHAY PACIFIC","TAP - AIR PORTUGAL","ROYAL AIR MAROC","MANX","GERMAN WINGS","KINGFISHER AIRLINES LTD","JET AIRWAYS","AIR CHINA","AEROFLOT","EMIRATES","LOT POLISH AIRLINES","AEROMEXICO","UNITED AIRLINES","DELTA AIR LINES INC.","TRANSAERO AIRLINES","SOUTH AFRICAN AIRWAYS","KOREAN AIR","AER ARANN EXPRESS","SINGAPORE AIRLINES","JET 2","CIMBER STERLING","QANTAS","BRITANNIA AIRWAYS","HAHN AIR LINES GMBH","TURKISH AIRLINES INC.","CONTINENTAL AIRLINES","AIR MALTA","MISC SUPPLIERS","AIR PACIFIC LIMITED","ESTONIAN AIR","CROATIA AIRLINES","TAM - LINHAS AEREAS","AIR EUROPA AIR ESPANA SA","JAPAN AIR LINES"]'

# Compare the two lists
    assert json_response == expected_airlines 


def test_get_departure():
    response = client.get('/get_departure')

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response
    json_response = response.json()

    expected_departure = '["GLASGOW","LONDON - LGW","SOUTHAMPTON","LERWICK","INVERNESS","KRAKOW","BELFAST CITY","MARRAKECH","NEWCASTLE","LONDON - LHR","EDINBURGH","SINGAPORE","ABERDEEN","BARRA","MILAN - LINATE","AMSTERDAM","MANCHESTER","COLOGNE","PISA","STANSTED","PLYMOUTH","LONDON -CITY","LEEDS","LIVERPOOL","DUBLIN","MALAGA","NICE","STORNOWAY","MARSEILLE","PALMA MALLORCA","KIRKWALL","ZURICH","BOURNEMOUTH","BEIRUT","BRISTOL","TEES SIDE","LARNACA","EXETER","NORWICH","BELFAST INTL","TENERIFE SUR","VIENNA","PARIS","ISTANBUL","BENBECULA","FARO","ORIO AL SERIO","TREVISO","DAKAR","BEIJING","LUTON","BARCELONA","NANJING","BIRMINGHAM","ROME","VALENCIA","BRUSSELS","LA CORUNA","LAS PALMAS","GENEVA","MALPENSA","MADRID","HALIFAX CANADA","MIAMI","LISBON","MONTREAL","GOTHENBURG","GENOA","GLENEGEDALE","CAPE TOWN","SEOUL-GIMPO","HUMBERSIDE","SEOUL","BREST","PRAGUE","LAGOS","PUSAN","GALWAY","JERSEY","PARIS - ORLY","DUSSELDORF","CORK","BIARRITZ","STAVANGER","STOCKHOLM","CAMPBELTOWN","CHENGDU","ADDIS ABABA","TOKYO - NARITA","BLACKPOOL","NEWQUAY","ZWEISIMMEN","BUDAPEST","DETROIT - DTW","BILBAO","DUBROVNIK","BERLIN","HAMBURG","EAST MIDLANDS",null,"AARHUS","ATHENS","COPENHAGEN","OSLO","WASHINGTON","TEL AVIV YAFO","SYDNEY","AMMAN","POZNAN","BALTIMORE","MELBOURNE","LYON","BUCHAREST","LOS ANGELES","CARDIFF","HELSINKI","ALICANTE","PRESTWICK","ANTWERP","HONG KONG","NAIROBI","BRISBANE","FRANKFURT","ANTIGUA","MONTSERRAT","GIBRALTAR","VENICE","LUXEMBOURG","VIGO","DUBAI","DENVER","NANTES","TURKU","HOUSTON","TOULOUSE","ISLE OF MAN","OTTAWA","STRASBOURG","GUERNSEY","MALTA","EINDHOVEN","DONCASTER SHEFFIELD","CAIRO","BILLUND","CONNEL","COLONSAY IS","SUVA FIJI","CALVI","KEFLAVIK INTERNATIONAL","VERONA","OPORTO","TIREE","COLL ISLAND","NAPLES","KISHINEV","DELHI","CAGLIARI","DUNDEE","NEWARK","SALT LAKE CITY","SHANGHAI","TORONTO","WARSAW","GDANSK","MOSCOW","ROTTERDAM","TROMSO","CATANIA","CALGARY","HAVANA","BREMEN","NUREMBURG","TIANJIN","TURIN","TALLINN","KANSAI INTERNATIONAL","WICK","CASABLANCA","PALANGA","PANAMA CITY","TENERIFE","VILNIUS","AALBORG","BASLE","LAS VEGAS","CALCUTTA","ALDERNEY","MUMBAI","ST PETERSBURG","GUARULHOS INTL.","MADRAS","JOBURG","ASTURIAS","ROOIKOP","PULA","LA ROCHELLE FR","ANGLESEY","MONTEVIDEO","CANAL BALO","WASHINGTON - NATIONAL","MEXICO CITY","GUADALAJARA","DURBAN","BERMUDA"]'

# Compare the two lists
    assert json_response == expected_departure 


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


def test_clean_cost():
    response = client.get('/Cleaning/£57')
    assert response.status_code == 200
    assert response.json() == 57


def test_clean_fake():
    response = client.get('/Cleaning/57')
    assert response.status_code == 200
    assert response.json() == 57

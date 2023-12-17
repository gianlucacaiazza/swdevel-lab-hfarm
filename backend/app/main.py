

from fastapi import FastAPI,HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import pandas as pd
import sys

app = FastAPI()
sys.path.append('app')

# Load flight data and integrate cleaning functions
from mymodules.cleaning import df_clean
from mymodules.df_integrations import flights
from mymodules.feat_1_avg_price import calculate_average_price
from mymodules.feat_3_class_price import calculate_average_price_airline
from mymodules.feat_2_random import randomize_destination
from mymodules.feat_4_cheapest import cheapest_to_fly
from mymodules.cleaning import clean_cost

app = FastAPI()


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.
    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get("/random/{departure}")
def combined_endpoint(departure: str):
    result = randomize_destination(departure, flights)
    return {
        "give_output": result['give_output'],
        "arrivalcity": result['arrivalcity']
    }


@app.get('/get_departure')
def get_departure_from_csv():
    results = flights['Departure'].drop_duplicates().to_json(orient='records')
    return results
    

@app.get('/get_airline')
def airlines():
    tt = df_clean['Air Carrier'].drop_duplicates().to_json(orient='records')
    return tt


@app.get('/airlines-{AIRLINES}')
def average_web(AIRLINES):
    result = calculate_average_price_airline(flights, AIRLINES)
    return result


@app.get('/avg/{Departure}/{Arrival}')
def avg_price(Departure:str, Arrival:str):
    result = calculate_average_price(flights, Departure, Arrival)
    if result != None:
        result = round(result,2)
        result = "{:.2f}".format(result)
        return result
    else:
        return None
  

@app.get('/arrival-{Arrival}')
def cheapest(Arrival):
    result = cheapest_to_fly(flights, Arrival)
    return result


@app.get('/Cleaning/{Value}')
def clean(Value):
    result = clean_cost(Value)
    return result

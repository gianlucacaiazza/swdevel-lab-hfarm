

from fastapi import FastAPI,HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import pandas as pd
import sys

app = FastAPI()
sys.path.append('app')

# Load flight data and integrate cleaning functions
from mymodules.Cleaning import flights_data_cleaned
from mymodules.df_integrations import flights
from mymodules.Feature_1_avg_price import calculate_average_price, filter_destinations
from mymodules.Avg_Class_Price import calculate_average_price_airline
from mymodules.Destination_random import randomize_destination



app = FastAPI()


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.
    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}

@app.get("/query/{departure}")
def randomize_destination_endpoint(departure: str):
    result = randomize_destination(departure, flights)
    return result

@app.get('/get_departure')
def get_departure_from_csv():
    results = flights['Departure'].drop_duplicates().to_json(orient='records')
    return results
    
@app.get('/get_airline')
def airlines():
    tt = flights_data_cleaned['Air Carrier'].drop_duplicates().to_json(orient='records')
    return tt


@app.get('/{AIRLINES}')
def average_web(AIRLINES):
    result = calculate_average_price_airline(flights, AIRLINES)
    return result


@app.get('/{Departure}/{Arrival}')
def avg_price(Departure:str, Arrival:str):
    result = calculate_average_price(flights, Departure, Arrival)
    result = round(result,2)
    result = "{:.2f}".format(result)
    return result

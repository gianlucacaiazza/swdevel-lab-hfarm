from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import sys
app = FastAPI()
sys.path.append('app')

# Load flight data and integrate cleaning functions
from mymodules.Cleaning import flights_data_cleaned
from mymodules.df_integrations import flights
from mymodules.Feature_1_avg_price import calculate_average_price, filter_destinations
#from mymodule.feature import calculate_average_price, prompt_for_airports
























































@app.get('/get_airport')
def airports():
    airports = flights['Departure'].drop_duplicates().to_json(orient = 'records')
    return airports

@app.get('/{Departure}/{Arrival}')
def avg_price(Departure:str, Arrival:str):
    result = calculate_average_price(flights, Departure, Arrival)
    return result

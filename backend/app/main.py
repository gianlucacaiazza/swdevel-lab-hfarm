"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd


app = FastAPI()

df = pd.read_csv('/app/app/ricarica_colonnine.csv', sep=';')


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}

@app.get('/module/search/{street_name}')
def get_charging_stations_provider_given_street_name(street_name):
    charging_station=df[df['nome_via']== street_name]
    if not charging_station.empty:
        return f" The provider for the charging station present in {street_name} is {charging_station['titolare'].values[0]}"
    else:
        return "Unfortunately the street name you inserted is not present in our database"


@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})

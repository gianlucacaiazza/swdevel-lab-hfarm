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

df = pd.read_csv('/app/app/ricarica_colonnine.csv',sep=';')


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get('/get_charging_stations')
def numbers_of_stations_per_via(street_name):
    selected_street = df[df['nome_via'] == street_name]
    
    if not selected_street.empty:
        number_of_stations = selected_street['numero_col'].sum()  # Sum the column values for the selected street
        info_vie = number_of_stations
        return f"Number of charging stations in '{street_name}': {info_vie}"
    else:
        return f"The sreet '{street_name}' is not present in the dataset."

@app.get('/get_charging_stations/{street_name}')
def numbers_of_stations_per_via(street_name: str):
    """
    Endpoint to get the number of charging columns based on the street name.

    Args:
        nome_via (str): The name of the street.

    Returns:
        dict: Information about the number of charging columns for the provided street name.
    """
    street_name = street_name.upper()  # Convert to title case for consistency
    selected_street = df[df['nome_via'] == street_name]
    
    if not selected_street.empty:
        number_of_stations = selected_street['numero_col'].sum()  # Sum the column values for the selected street
        return {"street_name": street_name, "number_stations": str(number_of_stations)}
    else:
        return {"error": f"The street '{street_name}' is not present in the dataset."}

def numbers_of_stations_per_via(street_name_input: str = None):
    if street_name_input is not None:
        result = numbers_of_stations_per_via(street_name_input)
        return result
    else:
        return '/'


@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})

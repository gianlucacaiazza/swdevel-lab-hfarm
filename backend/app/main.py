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
import csv


app = FastAPI()

df = pd.read_csv('/app/app/ricarica_colonnine.csv')


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get('/module/search/{provider_name}')
def get_charging_points_by_provider(provider_name):
    """
    Retrieve charging points based on the provided provider's name.

    Args:
    - provider_name (str): The name of the charging point provider.

    Returns:
    - List[dict]: List of dictionaries containing charging point information.
    """
    charging_points = []
    with open('/app/app/ricarica_colonnine.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        for row in reader:
            if row['titolare'].upper() == provider_name.upper():
                charging_points.append({
                    'localita': row['localita'].capitalize(),
                    'tipologia': row['tipologia'],
                    'numero_col': row['numero_col']
                })
    return charging_points


@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})
"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import csv


app = FastAPI()


df = pd.read_csv('/app/app/ricarica_colonnine.csv', sep=';')

@app.get('/addresses/{area_name}')
def get_via_by_area(area_name):
    filtered_data = df[df['nome_nil'] == area_name]
    return filtered_data['nome_via'].tolist()


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


@app.get('/module/lookfor/{provider_name}')
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


@app.get('/get_charging_point')
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

def get_socket_types_by_zone(zone: str):
    try:
        # Filter the DataFrame for the specified zone
        zone=zone.upper()
        zone_data = df[df['localita'] == zone]

        # Check if the zone exists
        if zone_data.empty:
            raise HTTPException(status_code=404, detail=f"Zone '{zone}' not found.")

        # Get the unique socket types in the zone
        socket_types = zone_data['infra'].unique().tolist()

        return {"zone": zone, "socket type": socket_types}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/socket_types_by_zone/{zone}")
async def socket_types_by_zone(zone: str):
    return get_socket_types_by_zone(zone)



@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})
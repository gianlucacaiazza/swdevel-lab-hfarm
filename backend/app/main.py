"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd

from .mymodules.search_with_province import schools_by_province
from .mymodules.best_school import best_school_in_town
from .mymodules.search_with_infrastructure import search_with_infrastructure, load_and_clean_data

from .mymodules import listing

app = FastAPI()

# Lettura del csv, si usa sep=';' poiche' questo file usa come separatore
# il punto e virgola e non la virgola.
veneto = pd.read_csv('/app/app/veneto.csv', sep=';')
veneto = veneto.fillna('')
veneto = load_and_clean_data

@app.get('/all/{type}')
def list_all(type: str):
    """
    Endpoint to query all available provinces.

    Returns:
        dict: Available provinces.
    """

    if type == 'provinces':
        return {'elements': listing.list_provinces(veneto)}
    elif type == 'cities':
        return {'elements': listing.list_cities(veneto)}
    elif type == 'school_types':
        return {'elements': listing.list_school_types(veneto)}

    return {'error': 'element not found'}


@app.get('/module/search/province/{province}')
def with_province(province: str):
    """
    Endpoint to query schools by province

    Args:
        province (str): province name.

    Returns:
        dict: all the schools in the inserted province.
    """

    return JSONResponse(schools_by_province(province, veneto))


@app.get('/module/search/rank/{city}/{level}')
def with_highest_rank(city: str, level: str):
    """
    Endpoint to query schools by city and level

    Args:
        province (str): city name.
        level (str): level name.

    Returns:
        dict: all the schools filtered by province and level.
    """

    result = best_school_in_town(city, level, veneto)

    if result is not None:
        return {'result': result.transpose().to_dict()}

    return {'error': 'Unable to find school'}


@app.get('/module/search/infrastructure/{province}/{infrastructure}')
def with_infrastructure(province: str, infrastructure: str):
    """
    Endpoint to query schools by province and infrastructure

    Args:
        province (str): province name.
        infrastructure (str): level name.

    Returns:
        dict: all the schools filtered by province and infrastructure.
    """

    result = search_with_infrastructure(province, infrastructure, veneto)

    if result is not None:
        return {'result': result.transpose().to_dict()}

    return {'error': 'Unable to find school'}

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
from .mymodules.utils import top_wines_by_rating 


app = FastAPI()

df_red = pd.read_csv('/app/app/datasets/Red.csv')
df_rose = pd.read_csv('/app/app/datasets/Rose.csv')
df_sparkling = pd.read_csv('/app/app/datasets/Sparkling.csv')
df_white = pd.read_csv('/app/app/datasets/White.csv')

df_red["type"] = "red"
df_rose["type"] = "rose"
df_sparkling["type"] = "sparkling"
df_white["type"] = "white"

df_wines = pd.concat([df_red, df_rose, df_sparkling, df_white])

@app.get('/top-wines')
def get_most_rated_wines(limit: int = 10):
    """
     Endpoint to get the best reviewed wines.

    Parameters:
        limit: (optional) an integer representing the max number of wines that has to be returned

    Returns:
        dict: top wines sorted by rating (descending)
    """
    top_wines_dict = top_wines_by_rating(df_wines, limit).to_dict(orient='records')
    return JSONResponse(content=top_wines_dict)


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})

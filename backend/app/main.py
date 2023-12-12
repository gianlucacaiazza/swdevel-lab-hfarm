"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, HTTPException 
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import io

app = FastAPI() 

# Upload files containing wines data
wines = pd.concat([pd.read_csv(file) for file in ['/Users/user/Documents/GitHub/swdevel-lab-hfarm/backend/app/Red.csv', '/Users/user/Documents/GitHub/swdevel-lab-hfarm/backend/app/Rose.csv', '/Users/user/Documents/GitHub/swdevel-lab-hfarm/backend/app/Sparkling.csv', '/Users/user/Documents/GitHub/swdevel-lab-hfarm/backend/app/White.csv']], ignore_index=True)

# Define an endpoint that returns data in JSON format
@app.get("/get-wines-json/{vintage_min}/{vintage_max}")
def get_wines_json(vintage_min: int, vintage_max: int):
    try:
        # Convert the 'Year' column to integers
        wines["Year"] = pd.to_numeric(wines["Year"], errors="coerce")

        # Filter the wine data within the specified range of vintages
        filtered_wines = wines[(wines["Year"] >= vintage_min) & (wines["Year"] <= vintage_max)]

        # Convert the filtered data to JSON format and return the response
        wines_json = filtered_wines.to_json(orient="records")
        return wines_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-wines-json/{rating_min}/{rating_max}")
def get_wines_json(rating_min: float, rating_max: float):
    try:
        # Filter the wine data within the specified range of ratings
        filtered_wines = wines[(wines["Rating"] >= rating_min) & (wines["Rating"] <= rating_max)]

        # Convert the filtered data to JSON format and return the response
        wines_json = filtered_wines.to_json(orient="records")
        return JSONResponse(content=wines_json)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


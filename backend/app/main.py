"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd





from .mymodules.mood import find_songs_for_party, find_songs_for_chill, find_songs_for_workout, find_songs_for_passion, discover_random_song
app = FastAPI()



mood_functions = {
    "party": find_songs_for_party,
    "chill": find_songs_for_chill,
    "workout": find_songs_for_workout,
    "passion": find_songs_for_passion,
    "discover": discover_random_song  
}


@app.get('/mood/{mood_name}')
def get_songs_by_mood(mood_name: str):
    if mood_name in mood_functions:
        return mood_functions[mood_name]()
    else:
        raise HTTPException(status_code=404, detail="Mood not found")
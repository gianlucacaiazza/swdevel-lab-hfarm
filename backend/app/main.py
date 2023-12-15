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


from .mymodules.mood import (find_songs_for_party, find_songs_for_chill,
                             find_songs_for_workout, find_songs_for_passion,
                             discover_random_song)

from .mymodules.info import (count_songs, artist_songs,
                             get_song_count_by_genre, genre_popularity)

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
    """"Retreive a list of songs matching a specified mood"""
    if mood_name in mood_functions:
        return mood_functions[mood_name]()
    else:
        raise HTTPException(status_code=404, detail="Mood not found")


info_functions = {
    "c_songs": count_songs,
    "a_songs": artist_songs,
    "genre": get_song_count_by_genre,
    "p_genre": genre_popularity
}


@app.get('/info/{info_g}')
def get_info(info_g: str):
    """"Retreive information take form the csv"""
    if info_g in info_functions:
        result = info_functions[info_g]()
        return result
    else:
        raise HTTPException(status_code=404, detail="Information not found")

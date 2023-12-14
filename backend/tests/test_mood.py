import os
import sys
import pandas as pd
import random
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from app.mymodules.mood import find_songs_for_party, find_songs_for_chill, find_songs_for_workout, find_songs_for_passion

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

client = TestClient(app)

def test_find_songs_for_party():
    """"Test the output of find_songs_for_party function to ensure It is a list"""
    response = client.get("/mood/party")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 

def test_find_songs_for_chill():
    """"Test the output of find_songs_for_chill function to ensure It is a list"""
    response = client.get("/mood/chill")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_find_songs_for_workout():
    """"Test the output of find_songs_for_workout function to ensure It is a list"""
    response = client.get("/mood/workout")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_songs_for_passion():
    """"Test the output of find_songs_for_passion function to ensure It is a list"""
    response = client.get("/mood/passion")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_discover_random_song():
    """"Test the output of discover_random_song function to ensure It is a list"""
    response = client.get("/mood/discover")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_songs_for_party_values():
    """Test the find_songs_for_party function to ensure it returns songs within the specified feature ranges."""
    songs_for_party = find_songs_for_party()
    random_song = random.choice(songs_for_party)
    song_in_dataset = spotify_songs[(spotify_songs['track_name'] == random_song['track_name']) &
                                    (spotify_songs['track_artist'] == random_song['track_artist'])].iloc[0]
    assert 0.6 <= song_in_dataset['danceability'] <= 1.0
    assert 0.6 <= song_in_dataset['energy'] <= 1.0
    assert -60 <= song_in_dataset['loudness'] <= 0
    assert 0.0 <= song_in_dataset['speechiness'] <= 0.5
    assert 0.0 <= song_in_dataset['instrumentalness'] <= 0.5
    assert 0.5 <= song_in_dataset['valence'] <= 1.0
    assert 120 <= song_in_dataset['tempo'] <= 180


def test_find_songs_for_chill_values():
    """Test the find_songs_for_chill function to ensure it returns songs within the specified feature ranges."""
    songs_for_chill = find_songs_for_chill()
    random_song = random.choice(songs_for_chill)
    song_in_dataset = spotify_songs.loc[(spotify_songs['track_name'] == random_song['track_name']) & 
                                        (spotify_songs['track_artist'] == random_song['track_artist'])].iloc[0]

    assert song_in_dataset['danceability'] < 0.6
    assert song_in_dataset['energy'] < 0.5
    assert song_in_dataset['speechiness'] < 0.5
    assert 0.3 <= song_in_dataset['valence'] <= 0.7
    assert 70 <= song_in_dataset['tempo'] <= 110

def test_find_songs_for_workout_values():
    """Test the find_songs_for_workout function to ensure it returns songs within the specified feature ranges."""
    songs_for_workout = find_songs_for_workout()
    random_song = random.choice(songs_for_workout)
    song_in_dataset = spotify_songs.loc[(spotify_songs['track_name'] == random_song['track_name']) & 
                                        (spotify_songs['track_artist'] == random_song['track_artist'])].iloc[0]

    assert song_in_dataset['energy'] > 0.6
    assert song_in_dataset['tempo'] > 120
    assert song_in_dataset['danceability'] > 0.5
    assert song_in_dataset['instrumentalness'] < 0.5
    assert 0.4 <= song_in_dataset['valence'] <= 0.8

def test_find_songs_for_passion_values():
    """Test the find_songs_for_passion function to ensure it returns songs within the specified feature ranges."""
    songs_for_passion = find_songs_for_passion()
    random_song = random.choice(songs_for_passion)
    song_in_dataset = spotify_songs.loc[(spotify_songs['track_name'] == random_song['track_name']) & 
                                        (spotify_songs['track_artist'] == random_song['track_artist'])].iloc[0]

    assert 0.3 <= song_in_dataset['danceability'] <= 0.7
    assert 0.4 <= song_in_dataset['energy'] <= 0.8
    assert -60 <= song_in_dataset['loudness'] <= 0
    assert 0.0 <= song_in_dataset['speechiness'] <= 0.5
    assert 0.0 <= song_in_dataset['instrumentalness'] <= 0.5
    assert 0.5 <= song_in_dataset['valence'] <= 1.0
    assert 80 <= song_in_dataset['tempo'] <= 120
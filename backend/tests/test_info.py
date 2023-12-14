import os
import sys
import pandas as pd
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

from app.mymodules.info import genre_popularity, get_song_count_by_genre, count_songs, artist_songs

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')



def test_genre_popularity():
    """Test the genre_popularity function to ensure it returns a dictionary with genres
    as keys and floats as values, with popularity scores between 0 and 100."""
    result = genre_popularity()
    assert isinstance(result, dict)
    for genre, popularity in result.items():
        assert isinstance(popularity, float)
        assert 0 <= popularity <= 100


def test_get_song_count_by_genre():
  """Test the get_song_count_by_genre function to ensure it returns a dictionary with
    subgenres as keys and integers as values, with the sum of values matching the
    total number of songs in the dataset."""  
    result = get_song_count_by_genre()
    assert isinstance(result, dict)
    assert sum(result.values()) == len(spotify_songs)


def test_count_songs():
    """Test the count_songs function to ensure it returns an integer count of all
    songs in the dataset."""
    result = count_songs('path_to_your_csv')
    assert isinstance(result, int)
    assert result == len(spotify_songs)


def test_artist_songs():
    """Test the artist_songs function to ensure it returns a dictionary with artists
    as keys and integers as values, sorted by artist name."""
    result = artist_songs()
    assert isinstance(result, dict)
    assert list(result.keys()) == sorted(result.keys())
    for artist, count in result.items():
        assert isinstance(count, int)
        assert count == (spotify_songs['track_artist'] == artist).sum()
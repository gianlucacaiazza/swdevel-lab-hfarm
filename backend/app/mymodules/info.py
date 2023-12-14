import pandas as pd
from itertools import islice

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def genre_popularity():
    """Return a dictionary with subgenres as keys and their average popularity as values"""
    genre_popularity = spotify_songs.groupby('playlist_subgenre')['track_popularity'].mean().sort_values(ascending=False)
    genre_popularity_dict = genre_popularity.to_dict()
    return genre_popularity_dict
    


def get_song_count_by_genre():
    """Return a dictionary with subgenres as keys and the count of songs as values"""
    subgenre_counts = spotify_songs['playlist_subgenre'].value_counts().to_dict()
    return subgenre_counts


def artist_songs():
    """Return a dictionary with artists as keys and their song counts as values"""
    artist_counts = spotify_songs['track_artist'].value_counts().to_dict()
    sorted_artist_counts = dict(sorted(artist_counts.items()))
    return(sorted_artist_counts)

def count_songs(csv_path):
    """Return a dictionary with the total count of songs in the dataset"""      
    total_songs_count = len(spotify_songs)       
    return total_songs_count
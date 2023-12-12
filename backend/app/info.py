import pandas as pd

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def genre_popularity():
    genre_popularity = spotify_songs.groupby('playlist_subgenre')['track_popularity'].mean().sort_values(ascending=False)
    genre_popularity_dict = genre_popularity.to_dict()
    return genre_popularity
import pandas as pd
from itertools import islice

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def genre_popularity():
    genre_popularity = spotify_songs.groupby('playlist_subgenre')['track_popularity'].mean().sort_values(ascending=False)
    genre_popularity_dict = genre_popularity.to_dict()
    return genre_popularity
    


def get_song_count_by_genre():
        subgenre_counts = spotify_songs['playlist_subgenre'].value_counts().to_dict()
        return subgenre_counts


def artist_songs():
    artist_counts = spotify_songs['track_artist'].value_counts().to_dict()
    sorted_artist_counts = dict(sorted(artist_counts.items()))
    return(dict(islice(sorted_artist_counts.items(), 0, 50)))

def count_songs(csv_path):      
        total_songs_count = len(spotify_songs)       
        return total_songs_count
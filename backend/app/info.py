import pandas as pd

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def genre_popularity():
    genre_popularity = spotify_songs.groupby('playlist_subgenre')['track_popularity'].mean().sort_values(ascending=False)
    genre_popularity_dict = genre_popularity.to_dict()
    return genre_popularity
    


def get_song_count_by_genre():
        subgenre_counts = songs_spotify['playlist_subgenre'].value_counts().to_dict()
        return subgenre_counts

def count_songs(csv_path):      
        total_songs_count = len(spotify_songs)       
        return total_songs_count
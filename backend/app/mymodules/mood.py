import pandas as pd

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def find_songs_for_party():
    return spotify_songs[(spotify_songs['danceability'].between(0.6, 1.0)) &
              (spotify_songs['energy'].between(0.6, 1.0)) &
              (spotify_songs['loudness'].between(-60, 0)) &
              (spotify_songs['speechiness'].between(0.0, 0.5)) &
              (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
              (spotify_songs['valence'].between(0.5, 1.0)) &
              (spotify_songs['tempo'].between(120, 180))].sample(5)[['track_name', 'track_artist']]

def find_songs_for_chill():
    return spotify_songs[(spotify_songs['danceability'] < 0.6) &
              (spotify_songs['energy'] < 0.5) &
              (spotify_songs['speechiness'] < 0.5) &
              (spotify_songs['valence'].between(0.3, 0.7)) &
              (spotify_songs['tempo'].between(70, 110))].sample(5)[['track_name', 'track_artist']]

def find_songs_for_workout():
    return spotify_songs[(spotify_songs['energy'] > 0.6) &
              (spotify_songs['tempo'] > 120) &
              (spotify_songs['danceability'] > 0.5) &
              (spotify_songs['instrumentalness'] < 0.5) &
              (spotify_songs['valence'].between(0.4, 0.8))].sample(5)[['track_name', 'track_artist']]

def find_songs_for_passion():
    return spotify_songs[(spotify_songs['danceability'].between(0.3, 0.7)) &
              (spotify_songs['energy'].between(0.4, 0.8)) &
              (spotify_songs['loudness'].between(-60, 0)) &
              (spotify_songs['speechiness'].between(0.0, 0.5)) &
              (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
              (spotify_songs['valence'].between(0.5, 1.0)) &
              (spotify_songs['tempo'].between(80, 120))].sample(5)[['track_name', 'track_artist']]

def discover_random_song():
    return spotify_songs.sample(1)[['track_name', 'track_artist']]
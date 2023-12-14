import pandas as pd

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')

def find_songs_for_party():
    songs_for_party = spotify_songs[(spotify_songs['danceability'].between(0.6, 1.0)) &
                                    (spotify_songs['energy'].between(0.6, 1.0)) &
                                    (spotify_songs['loudness'].between(-60, 0)) &
                                    (spotify_songs['speechiness'].between(0.0, 0.5)) &
                                    (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
                                    (spotify_songs['valence'].between(0.5, 1.0)) &
                                    (spotify_songs['tempo'].between(120, 180))]
    return songs_for_party.sample(50)[['track_name', 'track_artist']].to_dict(orient='records')

def find_songs_for_chill():
    songs_for_chill = spotify_songs[(spotify_songs['danceability'] < 0.6) &
                                    (spotify_songs['energy'] < 0.5) &
                                    (spotify_songs['speechiness'] < 0.5) &
                                    (spotify_songs['valence'].between(0.3, 0.7)) &
                                    (spotify_songs['tempo'].between(70, 110))]
    return songs_for_chill.sample(50)[['track_name', 'track_artist']].to_dict(orient='records')

def find_songs_for_workout():
    songs_for_workout = spotify_songs[(spotify_songs['energy'] > 0.6) &
                                      (spotify_songs['tempo'] > 120) &
                                      (spotify_songs['danceability'] > 0.5) &
                                      (spotify_songs['instrumentalness'] < 0.5) &
                                      (spotify_songs['valence'].between(0.4, 0.8))]
    return songs_for_workout.sample(50)[['track_name', 'track_artist']].to_dict(orient='records')

def find_songs_for_passion():
    songs_for_passion = spotify_songs[(spotify_songs['danceability'].between(0.3, 0.7)) &
                                      (spotify_songs['energy'].between(0.4, 0.8)) &
                                      (spotify_songs['loudness'].between(-60, 0)) &
                                      (spotify_songs['speechiness'].between(0.0, 0.5)) &
                                      (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
                                      (spotify_songs['valence'].between(0.5, 1.0)) &
                                      (spotify_songs['tempo'].between(80, 120))]
    return songs_for_passion.sample(50)[['track_name', 'track_artist']].to_dict(orient='records')

def discover_random_song():
    random_song = spotify_songs.sample(1)[['track_name', 'track_artist']].to_dict(orient='records')
    return random_song
print(type(find_songs_for_passion()))
import json
import PySimpleGUI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

f = open("SpotifyDataDict.txt", 'r')
dictionary = json.loads(f.read())
for i in range(1,201):
    try:
        print(str(i) + ": ", end='')
        print(dictionary[str(i)]['name'], end='')
        print(" by ", end='')
        print(dictionary[str(i)]['artist'], end='')
        print(" is in the key " + str(dictionary[str(i)]['key']))
    except KeyError:
        print(str(i) + " Error")
print(sp.recommendation_genre_seeds())
rec = {"indie", "alt-rock", "show-tunes", "rock", "r-n-b"}
print(sp.recommendations(seed_genres=rec))


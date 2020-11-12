import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
username = 'epalmer822'
CLIENT_ID = 'fc5e21deea874e2a9246c8e8935e9fe1'
CLIENT_SECRET = 'a79221482a5f40d286fc7b5e5c42e318'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope="user-library-read", client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://spotify.com"))

sp.me()
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

username = '7k5znrbx07x5i01cbwsullbq8'
CLIENT_ID = '3d98c472e0e544ea8fdb7244dbac1341'
CLIENT_SECRET = '5ccc1acf40b448909961e28ace0539b2'



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope="user-library-read",
                                               client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri="https://spotify.com"))

x = sp.track("https://open.spotify.com/track/3GstSobbjTEjubD6xXXPVR?si=MDFHchTsRB-plrdgBpPtlA")
print(x['album']['artists'])
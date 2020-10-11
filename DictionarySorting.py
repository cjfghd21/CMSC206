import sys
import csv
import pandas
import numpy as np
import matplotlib.pyplot
import spotipy

file = input("Enter the CSV file to pull data from: ")

fullDict = dict()
inputCSV = open()

username = 'epalmer822'
CLIENT_ID = 'a79221482a5f40d286fc7b5e5c42e318'
CLIENT_SECRET = 'a79221482a5f40d286fc7b5e5c42e318'


if __name__ == 'epalmer822':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()


token = spotipy.util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)


song = dict()
url = "https://open.spotify.com/track/7hxHWCCAIIxFLCzvDgnQHX"
song = sp.audio_analysis(url)
tempTrackDict = dict()
tempTrackDict = song['track']
# only use if tempo_confidence > 0.5, 'time_signature_confidence' > 0.5, 'key_confidence' > 0.5,
# and mode_confidence > 0.3
print("Analysis for ", end='')
print(sp.track(url)['name'], end='')
print(": ", end='')

print("\nDuration: " + str(tempTrackDict['duration']) + "\nLoudness: " + str(tempTrackDict['loudness']))
# we need 'duration', 'loudness', 'tempo', 'key', and 'mode'



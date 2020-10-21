import json
import PySimpleGUI
import spotipy

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


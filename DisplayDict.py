import json

f = open("SpotifyDataDict.txt", 'r')
dictionary = json.loads(f.read())
for i in range(1,201):
    try:
        print(str(i) + ": ", end='')
        print(dictionary[str(i)]['name'], end='')
        print(" by ", end='')
        print(dictionary[str(i)]['artist'])
    except KeyError:
        print(str(i) + " Error")
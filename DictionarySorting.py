import spotipy
import pandas as pd
import multiprocessing as mp
from multiprocessing import Pool
import json
import os
import re
import subprocess
import time
from tqdm import tqdm


NUM_OF_SONGS = 200
FIRST_SONG_ROW = 3

numbersList = list(range(3,200))
NUM_OF_SONGS += 1  # compensate for headers (first song from spotify CSVs is listed in row 3)

NUM_OF_ATTRIBUTES = 5
URL_ROW = 4  # adjusted for columns being indexed at 1 in csv
file = "US_Top200_10-10-2020.csv" # replace this with an input later
def checkCPUcount():
    cores = mp.cpu_count()
    print("found " + str(cores) + " threads, ", end='' )
    processes = int(cores/2)
    print("using " + str(processes) + " processes.\n")
    return cores

class songDataClass:
    dataPointCount = 0 # evaluate how many of the songs are actually being used as data points
    songAttributeDict = dict()
    pbar = tqdm(total=200)


c = songDataClass()

fullDict = dict() # dictionary using position in 200 list to index everything else, you can pull data from
songData = dict()

# find cpu threads to optimize multiprocessing



inputCSV = pd.read_csv(file, header=None)

username = 'epalmer822'
CLIENT_ID = 'a79221482a5f40d286fc7b5e5c42e318'
CLIENT_SECRET = 'a79221482a5f40d286fc7b5e5c42e318'

token = spotipy.util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)

# only use if tempo_confidence > 0.5, 'time_signature_confidence' > 0.5, 'key_confidence' > 0.5,
# and mode_confidence > 0.3
# we need 'duration', 'loudness', 'tempo', 'key', and 'mode'
# each song data list will contain, in order, ['name'], ['artist], ['duration'], ['loudness'], ['tempo'], ['key'], and ['mode']
# indexed with the number of the position in top 200

# -------------------------------------------------------------------------------------------------------------------------

# notes: keys/modes are returned as numbers, but obviously a song isn't in the key of 5. Uses "standard pitch class notation"
# so on a scale of 1-11,

# 0 = C
# 1 = C#
# 2 = D
# 3 = Eb
# 4 = E
# 5 = F
# 6 = F#
# 7 = G
# 8 = G#
# 9 = A
# 10 = Bb
# 11 = B

# modes are also labeled as integers, but no support for more than the two most common modes, so the confidence value on that has to be lower
# because songs aren't always written in major or minor

# 0 = minor
# 1 = major

# ----------------------------------------------------------------------------------------------------------------------

#made a function so multiprocessing can work

def SongDataSocket(i):
    # if i % 2 == 0:
        # print(str(int(i/2)) + "%")
    failConfidenceTest = False  # if the confidence values are too low, we have to throw out the data, this flag will
    # let the loop pass over that data point
    # resetting here so at the beginning of every iteration it starts as false
    # ---haven't done that yet---

    url = inputCSV.iloc[i-1][URL_ROW]  # sets the song URL for this iteration of the loop, constant just in case spotify reformats its

    songAnalysis = sp.audio_analysis(url)  # fetch the song attributes
    confidenceValues = [songAnalysis['track']['tempo_confidence'],
                        songAnalysis['track']['time_signature_confidence'],
                        songAnalysis['track']['key_confidence'], songAnalysis['track']['mode_confidence']]
    songAnalysis = songAnalysis['track']
    trackData = dict()
    urlData = sp.track(url)
    trackData = {
        'name': urlData['name'],
        'artist': urlData['album']['artists'][0]['name'],
        # for some reason spotify indexes all artist data in a list that only has one element, which is a dictionary. no clue why
        'duration': songAnalysis['duration'],
        'loudness': songAnalysis['loudness'],
        'tempo': songAnalysis['tempo'],
        'key': songAnalysis['key'],
        'mode': songAnalysis['mode']
    }
    dataReturn = [str(i-2), dict(trackData)]
    return dataReturn


# change to a string for easier input validation, can convert to an integer again later
result_list = []

def log_results(result):
    c.songAttributeDict.update({str(result[0]): result[1]})
    c.pbar.update(1)


def main():
    allowed_processes = checkCPUcount()
    pool = mp.Pool(processes=allowed_processes)
    for i in range(3, 203):
        pool.apply_async(SongDataSocket, args = (i, ), callback = log_results)
    pool.close()
    pool.join()
    pool.close()


def print_results():
    print(c.songAttributeDict)

if __name__ == '__main__':

    main()
    print("-------------------------------------------------------------------------\n\n"
          "-------------------------------------------------------------------------")
with open('SpotifyDataDict.txt', 'w') as f:
    f.write(json.dumps(c.songAttributeDict))













# Spotify Data Project


Requirements.txt contains the short list of dependencies required to run the project. 
Install each of them with either pip or conda, and you should be good to go.

For spotipy to work, you will need to grant it access through your spotify account. 
Change the username to your own in the "username" variable found on line 14 of DictionarySorting.py, and line 4 of tk.py.
Make sure to run tk.py FIRST, and make sure that a ".cache-[username]" file is generated. If you run DictionarySorting.py 
 without a cache file present in the working directory, it WILL open a few hundred chrome tabs asking for authentication, 
 and ~may~ set computers on fire. Again, run tk.py FIRST, and make absolutely sure that a cache file has been generated 
 in the same directory as dictionarySorting.py.


You can replace "US_Top200_10-10-2020.csv" with a different top-200 spotify chart 
(you may need to change the constants if spotify decided to change their formatting, but that's unlikely)


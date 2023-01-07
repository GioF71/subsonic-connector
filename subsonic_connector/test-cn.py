from pprint import pprint
from decouple import config
import libsonic


USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
SERVER_URL = config('SERVER_URL')
SERVER_PORT = config('SERVER_PORT')

#print('Connecting to SERVER {} at port {}'.format(SERVER_URL, SERVER_PORT))
print(f'Connecting to SERVER {SERVER_URL} at port {SERVER_PORT}')

# We pass in the base url, the username, password, and port number
# Be sure to use https:// if this is an ssl connection!
conn = libsonic.Connection(SERVER_URL, USERNAME, PASSWORD, port=SERVER_PORT)

# Let's get 2 completely random songs
songs = conn.getRandomSongs(size=2)
print(type(songs))
# We'll just pretty print the results we got to the terminal
pprint(songs)

randomSongs = songs['randomSongs']
print(type(randomSongs))

for song in songs['randomSongs']['song']:
    #pass
    print(type(song))
    print("Song id is {}".format(song["id"]))
    #pprint(song)


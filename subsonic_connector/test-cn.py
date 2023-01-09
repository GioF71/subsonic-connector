from pprint import pprint
from decouple import config
import libsonic
import connector

SERVER_URL = config('SERVER_URL')
print(SERVER_URL)
SERVER_PORT = config('SERVER_PORT')
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

#print('Connecting to SERVER {} at port {}'.format(SERVER_URL, SERVER_PORT))
#print(f'Connecting to SERVER {SERVER_URL} at port {SERVER_PORT}')

# We pass in the base url, the username, password, and port number
# Be sure to use https:// if this is an ssl connection!
#conn = libsonic.Connection(SERVER_URL, USERNAME, PASSWORD, port=SERVER_PORT)

#print(conn._getBaseQdict())

# Let's get 2 completely random songs
#songs = conn.getRandomSongs(size=2)
#print(type(songs))
# We'll just pretty print the results we got to the terminal
#pprint(songs)

#randomSongs = songs['randomSongs']
#print(type(randomSongs))

#for song in songs['randomSongs']['song']:
    #print(type(song))
    #print("Song id is {}".format(song["id"]))


ssc = connector.Connector(
    baseUrl = SERVER_URL, 
    port = SERVER_PORT, 
    username = USERNAME, 
    password = PASSWORD,
    appName="navibridge")

songs = ssc.getRandomSongs(size = 3)
#print(type(songs))
# We'll just pretty print the results we got to the terminal
#pprint(songs)

for song in songs['randomSongs']['song']:
    #print(type(song))
    print("Song id: {}".format(song["id"]))
    streamable_url = ssc.buildSongUrl(song["id"])
    cover_url = ssc.buildCoverArtUrl(song["id"])
    print(" -> Stream = [" + streamable_url + "]")
    print(" -> Cover  = [" + cover_url + "]")

newest_albums = ssc.getNewestAlbumList(size = 2)
pprint(newest_albums)

random_album = ssc.getRandomAlbumList(size = 1)
pprint(random_album)
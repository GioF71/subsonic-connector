from pprint import pprint
from decouple import config
import libsonic
import connector

SERVER_URL = config('SERVER_URL')
print(SERVER_URL)
SERVER_PORT = config('SERVER_PORT')
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

ssc = connector.Connector(
    baseUrl = SERVER_URL, 
    port = SERVER_PORT, 
    username = USERNAME, 
    password = PASSWORD,
    appName="navibridge")

# Newest albums (two albums expected)
newest_albums = ssc.getNewestAlbumList(size = 2)
pprint(newest_albums)

# Random album (just one)
random_album = ssc.getRandomAlbumList(size = 1)
pprint(random_album)

# Random songs (three expected)
songs = ssc.getRandomSongs(size = 3)
# full dump with pprint
#pprint(songs)
for song in songs['randomSongs']['song']:
    print("Song id: {}".format(song["id"]))
    streamable_url = ssc.buildSongUrl(song["id"])
    cover_url = ssc.buildCoverArtUrl(song["id"])
    print(" -> Stream = [" + streamable_url + "]")
    print(" -> Cover  = [" + cover_url + "]")

artists = ssc.getArtists()
print(type(artists))
all_artists = artists["artists"]
all_artist_list = all_artists["index"]

max = 3
cnt = 0
for current in all_artist_list:
    current_initial = current["name"]
    current_artist_list = current["artist"]
    #pprint(current_artist_list)
    for current_artist in current_artist_list:
        #pprint(current_artist)
        current_artist_name = current_artist["name"]
        current_artist_id = current_artist["id"]
        current_artist_album_count = current_artist["albumCount"]
        current_artist_url = current_artist["artistImageUrl"] if "artistImageUrl" in current_artist else None
        print("Artist {}|{}|{}".format(current_initial, current_artist_name, current_artist_album_count))
        print("  URL: {}".format(current_artist_url))
    cnt += 1
    if cnt == max: break
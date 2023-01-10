from pprint import pprint
from decouple import config
import libsonic

from connector import Connector

from artist import Artist
from album import Album
from song import Song
from album_list import AlbumList
from artist_list import ArtistList

SERVER_URL = config('SERVER_URL')
print(SERVER_URL)
SERVER_PORT = config('SERVER_PORT')
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

ssc = Connector(
    baseUrl = SERVER_URL, 
    port = SERVER_PORT, 
    username = USERNAME, 
    password = PASSWORD,
    appName="navibridge")

# Newest albums (two albums expected)
newest_albums : AlbumList = ssc.getNewestAlbumList(size = 2);
newest_albums_list : list = newest_albums.getList()
#pprint(newest_albums_data)
for c in newest_albums_list:
    album : Album = Album(c)
    print("Album {} = [{}]".format(album.getId(), album.getTitle()))
    pprint(album.getData())
    #print(album.getTitle())

# Random album (just one)
random_albums : AlbumList = ssc.getRandomAlbumList(size = 1000);
random_albums_data = random_albums.getList()
pprint(random_albums_data)
for c in random_albums_data:
    album : Album = Album(c)
    print("Album {} = [{}] Genre [{}]".format(
        album.getId(), 
        album.getTitle(),
        album.getGenre()))
    #pprint(album.getData())

# Random songs (three expected)
songs = ssc.getRandomSongs(size = 3)
# full dump with pprint
#pprint(songs)
for current in songs["randomSongs"]["song"]:
    current_song : Song = Song(current)
    song = current_song.getData()
    print("Song id: {} Title [{}] Disc [{}] Track [{}]".format(current_song.getId(), current_song.getTitle(), current_song.getDiscNumber(), current_song.getTrack()))
    id = current_song.getId()
    streamable_url = ssc.buildSongUrl(id)
    cover_url = ssc.buildCoverArtUrl(id)
    print(" -> Stream = [" + streamable_url + "]")
    print(" -> Cover  = [" + cover_url + "]")

all_artist_list = ssc.getArtists().getList()
#print(type(artists))
#all_artists = artists["artists"]
#all_artist_list = all_artists["index"]

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
        print("  LastFM Image (unsafe?): [{}]".format(current_artist_url))
        current_artist_data = ssc.getArtist(current_artist_id)
        #current_artist_albums = ssc.search2(current_artist_name, albumCount = 0, songCount = 0)
        #album_list = current_artist_albums["searchResult2"]["album"]
        album_list = current_artist_data["artist"]["album"]
        #pprint(current_artist_albums)
        for current_album in album_list:
            current_album_name = current_album["name"]
            if "coverArt" in current_album:
                current_album_cover_art = current_album["coverArt"]
                current_album_cover_art_url = ssc.buildCoverArtUrl(current_album_cover_art)
                print("    Album Art from [{}]: [{}]".format(current_album_name, current_album_cover_art_url))
        #pprint(album_list)
    cnt += 1
    if cnt == max: break
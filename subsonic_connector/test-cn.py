from pprint import pprint
from decouple import config
import hashlib
import libsonic

from connector import Connector

from artist import Artist
from album import Album
from song import Song
from album_list import AlbumList
from artist_list import ArtistList
from artist_list_item import ArtistListItem

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
    print("Album {} = [{}] Genre [{}]".format(
        album.getId(), 
        album.getTitle(),
        album.getGenre()))

# Random album (just one)
random_albums : AlbumList = ssc.getRandomAlbumList(size = 1000);
random_albums_data = random_albums.getList()
#pprint(random_albums_data)
for c in random_albums_data:
    album : Album = Album(c)
    print("Album {} = [{}] Genre [{}]".format(
        album.getId(), 
        album.getTitle(),
        album.getGenre()))

# Random songs (three expected)
songs = ssc.getRandomSongs(size = 3)
# full dump with pprint
#pprint(songs)
for current in songs["randomSongs"]["song"]:
    current_song : Song = Song(current)
    song = current_song.getData()
    print("Song [{}] A:[{}] G:[{}] D:[{}] T:[{}]".format(
        current_song.getTitle(), 
        current_song.getAlbum(),
        current_song.getGenre(),
        current_song.getDiscNumber(), 
        current_song.getTrack()))
    id = current_song.getId()
    streamable_url = ssc.buildSongUrl(id)
    cover_url = ssc.buildCoverArtUrl(id)
    #print(" -> Stream = [" + streamable_url + "]")
    #print(" -> Cover  = [" + cover_url + "]")

max = 3
cnt = 0

all_artist_list = ssc.getArtists().getList()
for current in all_artist_list:
    current_initial = current["name"]
    current_artist_list = current["artist"]
    #pprint(current_artist_list)
    for current_artist in current_artist_list:
        c : ArtistListItem = ArtistListItem(current_artist)
        #print("  LastFM Image (unsafe?): [{}]".format(c.getArtistImageUrl()))
        current_artist_data = ssc.getArtist(c.getId())
        artist : Artist = Artist(current_artist_data)
        #current_artist_albums = ssc.search2(current_artist_name, albumCount = 0, songCount = 0)
        #album_list = current_artist_albums["searchResult2"]["album"]
        first_album_name : str = None
        first_album_cover_art : str = None
        #album_list = current_artist_data["artist"]["album"]
        album_list = artist.getAlbumList()
        if len(album_list) > 0:
            first_album = album_list[0]
            selected_album : Album = Album(first_album)
            first_album_name = selected_album.getTitle()
            first_album_cover_art = selected_album.getCoverArt()
            if first_album_cover_art:
                first_album_cover_art = hashlib.md5(first_album_cover_art.encode('utf-8')).hexdigest()
                #print("    Album Art from [{}]: Hash [{}]".format(first_album_cover_art, first_album_cover_art))
        #pprint(current_artist_albums)
        print("Artist Initial[{}] N:[{}] AC:[{}] FirstAlbum:[{}] HashedCoverUrl:[{}]".format(
            current_initial, 
            c.getName(), 
            c.getAlbumCount(),
            first_album_name,
            first_album_cover_art))
        #pprint(album_list)
    cnt += 1
    if cnt == max: break
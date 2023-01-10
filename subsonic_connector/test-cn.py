from pprint import pprint
from decouple import config
import hashlib
import libsonic

from connector import Connector

from artist import Artist
from album import Album
from song import Song
from album_list import AlbumList
from artists import Artists
from artists_initial import ArtistsInitial
from artist_list_item import ArtistListItem
from search_result import SearchResult

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

def ewf(ssc):
    searchResultEwf : SearchResult = ssc.search(
        "Earth wind fire",
        artistCount = 0, 
        albumCount = 1000,
        songCount = 1000)
    #pprint(searchResultEwf.getData())
    ewfAlbums : list[Album] = searchResultEwf.getAlbums()
    ewfAlbum : Album
    ac : int = 0
    for ewfAlbum in ewfAlbums:
        print("EWF ndx:[{}] T:[{}] G:[{}]".format(
            ac,
            ewfAlbum.getTitle(),
            ewfAlbum.getGenre()))
        ac += 1
    ewfSongs : list[Song] = searchResultEwf.getSongs()
    ewfSong : Song
    sc : int = 0
    for ewfSong in ewfSongs:
        print("EWF ndx:[{}] Title:[{}] Art:[{}] A:[{}] D:[{}] T:[{}]".format(
            sc,
            ewfSong.getTitle(),
            ewfSong.getArtist(),
            ewfSong.getAlbum(),
            ewfSong.getDiscNumber(),
            ewfSong.getTrack()))
        sc += 1
    


# Newest albums (two albums expected)
newest_album_list : list[Album] = ssc.getNewestAlbumList(size = 2).getAlbums()
for album in newest_album_list:
    print("Album {} = [{}] Genre [{}]".format(
        album.getId(), 
        album.getTitle(),
        album.getGenre()))

# Random album (just one)
random_album_list : list[Album] = ssc.getRandomAlbumList(size = 1000).getAlbums()
for album in random_album_list:
    print("Album {} = [{}] Genre [{}]".format(
        album.getId(), 
        album.getTitle(),
        album.getGenre()))

random_songs : list = ssc.getRandomSongs(size = 3).getSongs()
for current in random_songs:
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

#####
# EWF
ewf(ssc)

#####
max_per_initial : int = 3
artists : Artists = ssc.getArtists()
all_artists_initials : list[ArtistsInitial] = artists.getArtistListInitials()
for current_initial in all_artists_initials:
    cnt : int = 0
    c : ArtistListItem
    for c in current_initial.getArtistListItems():
        cnt += 1
        if cnt > max_per_initial:
            break
        print("Count [{}] Initial [{}] Artist: {}".format(
            cnt,
            current_initial.getName(),
            c.getName()))
        artist : Artist = ssc.getArtist(c.getId())
        first_album_name : str = None
        first_album_cover_art : str = None
        album_list = artist.getAlbumList()
        if len(album_list) > 0:
            first_album = album_list[0]
            selected_album : Album = Album(first_album)
            first_album_name = selected_album.getTitle()
            first_album_cover_art = selected_album.getCoverArt()
            if first_album_cover_art:
                first_album_cover_art = hashlib.md5(first_album_cover_art.encode('utf-8')).hexdigest()
        print("Artist Initial[{}] N:[{}] AC:[{}] First:[{}] HashedCover:[{}]".format(
            current_initial.getName(), 
            c.getName(), 
            c.getAlbumCount(),
            first_album_name,
            first_album_cover_art))

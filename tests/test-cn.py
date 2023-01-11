from pprint import pprint
import os
import hashlib
import libsonic

from subsonic_connector.connector import Connector

from subsonic_connector.artist import Artist
from subsonic_connector.album import Album
from subsonic_connector.song import Song
from subsonic_connector.album_list import AlbumList
from subsonic_connector.artists import Artists
from subsonic_connector.artists_initial import ArtistsInitial
from subsonic_connector.artist_list_item import ArtistListItem
from subsonic_connector.search_result import SearchResult
from subsonic_connector.artist_cover import ArtistCover

SERVER_URL : str = str(os.getenv("SUBSONIC_SERVER_URL"))
SERVER_PORT : int = int(str(os.getenv("SUBSONIC_SERVER_PORT")))
USERNAME : str = str(os.getenv("SUBSONIC_USERNAME"))
PASSWORD : str = str(os.getenv("SUBSONIC_PASSWORD"))

ssc = Connector(
    baseUrl = SERVER_URL, 
    port = SERVER_PORT, 
    username = USERNAME, 
    password = PASSWORD,
    appName="navibridge")

def search_earth_wind_and_fire(ssc):
    searchResultEwf : SearchResult = ssc.search(
        "Earth wind fire",
        artistCount = 10, 
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

def newest_albums(ssc):
    # Newest albums (two albums expected)
    newest_album_list : list[Album] = ssc.getNewestAlbumList(size = 2).getAlbums()
    for album in newest_album_list:
        print("Album {} = [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getGenre()))

def random_albums(ssc):
    # Random album (just one)
    random_album_list : list[Album] = ssc.getRandomAlbumList(size = 1000).getAlbums()
    for album in random_album_list:
        print("Album {} = [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getGenre()))

def random_songs(ssr):
    random_songs : list[Song] = ssc.getRandomSongs(size = 3).getSongs()
    for current_song in random_songs:
        song = current_song.getData()
        print("Song [{}] A:[{}] G:[{}] D:[{}] T:[{}]".format(
            current_song.getTitle(), 
            current_song.getAlbum(),
            current_song.getGenre(),
            current_song.getDiscNumber(), 
            current_song.getTrack()))
        id = current_song.getId()
        #streamable_url = ssc.buildSongUrl(id)
        #cover_url = ssc.buildCoverArtUrl(id)
        #print(" -> Stream = [" + streamable_url + "]")
        #print(" -> Cover  = [" + cover_url + "]")

def show_artists(ssc):
    max_per_initial : int = 15
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
            artist_cover : ArtistCover = ssc.getArtistCover(artist)
            artist_first_album_id : str
            artist_cover_url : str
            hashed_cover_art : str
            if artist_cover:
                # set first album id
                artist_first_album_id = artist_cover.getAlbumId()
                # create url
                artist_cover_url = ssc.buildCoverArtUrl(artist_cover.getCoverArt())
                hashed_cover_art = hashlib.md5(artist_cover_url.encode('utf-8')).hexdigest()
                print("Artist Initial[{}] N:[{}] AC:[{}] AlbumId:[{}] HashedCover:[{}]".format(
                    current_initial.getName(), 
                    c.getName(), 
                    c.getAlbumCount(),
                    artist_first_album_id,
                    hashed_cover_art))

def showGenres(ssc):
    pprint(ssc.getGenres())

def main():
    showGenres(ssc)
    random_albums(ssc)
    newest_albums(ssc)
    random_songs(ssc)
    search_earth_wind_and_fire(ssc)
    show_artists(ssc)

if __name__ == "__main__":
    main()

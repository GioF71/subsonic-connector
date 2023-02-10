from pprint import pprint
import os
import hashlib

from subsonic_connector.connector import Connector
from subsonic_connector.configuration import Configuration
from subsonic_connector.default_config import DefaultConfiguration

from subsonic_connector.artist import Artist
from subsonic_connector.album import Album
from subsonic_connector.song import Song
from subsonic_connector.album_list import AlbumList
from subsonic_connector.artists import Artists
from subsonic_connector.artists_initial import ArtistsInitial
from subsonic_connector.artist_list_item import ArtistListItem
from subsonic_connector.search_result import SearchResult
from subsonic_connector.artist_cover import ArtistCover
from subsonic_connector.genres import Genres
from subsonic_connector.genre import Genre
from subsonic_connector.random_songs import RandomSongs
from subsonic_connector.response import Response
from subsonic_connector.list_type import ListType

print("Subclass check:", issubclass(DefaultConfiguration, Configuration))

ssc = Connector(DefaultConfiguration())

def search_earth_wind_and_fire(ssc):
    searchResultEwf : SearchResult = ssc.search(
        "Earth wind fire",
        artistCount = 10, 
        albumCount = 1000,
        songCount = 1000)
    #pprint(searchResultEwf.getData())
    ewfArtists : list[Artist] = searchResultEwf.getArtists()
    for ewfArtist in ewfArtists:
        print("EWF Artist: {} [{}]".format(
            ewfArtist.getName(),
            ewfArtist.getId()))
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
    newest_album_list : list[Album] = ssc.getNewestAlbumList(size = 2).getObj().getAlbums()
    for album in newest_album_list:
        print("Album {} = [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getGenre()))

def random_albums(ssc) -> list[str]:
    album_list : list[str] = []
    # Random album (a few of them)
    random_album_list : list[Album] = ssc.getRandomAlbumList(size = 1000).getObj().getAlbums()
    for album in random_album_list:
        print("Album {} = [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getGenre()))
        album_list.append(album.getId())
    return album_list

def random_songs(ssr):
    random_songs_response : Response[RandomSongs] = ssc.getRandomSongs(size = 25)
    random_songs : list[Song] = random_songs_response.getObj().getSongs()
    current_song : Song
    for current_song in random_songs:
        print("Song [{}] A:[{}] G:[{}] D:[{}] T:[{}]".format(
            current_song.getTitle(), 
            current_song.getAlbum(),
            current_song.getGenre(),
            current_song.getDiscNumber(), 
            current_song.getTrack()))
        id = current_song.getId()
        song_res : Response[Song] = ssc.getSong(id)
        print("Song Id:[{}] Title: [{}]".format(song_res.getObj().getId(), song_res.getObj().getTitle()))
        streamable_url = ssc.buildSongUrl(id)
        cover_url = ssc.buildCoverArtUrl(id)
        print(" -> Stream = [" + streamable_url + "]")
        print(" -> Cover  = [" + cover_url + "]")

def show_artists(ssc):
    max_per_initial : int = 15
    artists : Artists = ssc.getArtists().getObj()
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
            artist_cover : ArtistCover = ssc.getCoverByArtistId(c.getId())
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

def display_genres(ssc, cache : dict[str, str]):
    genres_response : Response[Genres] = ssc.getGenres()
    print("Genres Request: Status [{}] Version [{}]".format(
        genres_response.getStatus(), 
        genres_response.getVersion()))
    genre : Genre
    for genre in genres_response.getObj().getGenres() if genres_response.getObj() else []:
        if not genre.getName(): break
        print("G:[{}] AC:[{}] SC:[{}]".format(
            genre.getName(),
            genre.getAlbumCount(),
            genre.getSongCount()))
        if genre.getSongCount() > 0 or genre.getAlbumCount() > 0:
            showCoverArtForGenre(
                ssc, 
                str(genre.getName()), 
                cache)

def showCoverArtForGenre(ssc, genre : str, cache : dict[str, str]):
    select_cover_art : str
    if genre in cache:
        select_cover_art = cache[genre]
    else:
        select_cover_art : str = ssc.getCoverArtForGenre(genre)
        cache[genre] = select_cover_art
    if not select_cover_art:
        print("No cover art for genre {}".format(genre))
        return
    print("Cover art for genre: [{}] = {}".format(genre, select_cover_art))
    select_cover_art_url = ssc.buildCoverArtUrl(select_cover_art)
    if select_cover_art_url:
        print("Cover art URL for genre: [{}] = {}".format(
            genre, 
            select_cover_art_url))

def display_random_rock_album_list(ssc):
    response : Response[AlbumList] = ssc.getAlbumList(
        ltype = ListType.BY_GENRE, 
        genre = "Rock")
    album : Album
    for album in response.getObj().getAlbums():
        print("Genre: [{}] Album: [{}] Artist [{}]".format(album.getGenre(), album.getTitle(), album.getArtist()))

def display_random_albums(ssc):
    random_album_list : list[str] = random_albums(ssc)
    if random_album_list:
        #show first
        first_random : Response[Album] = ssc.getAlbum(random_album_list[0])
        if (first_random):
            print("getAlbum response status[{}] version[{}]".format(first_random.getStatus(), first_random.getVersion()))
        if (first_random and first_random.getObj()):
            print("{} [{}] {} [{}] Dur: [{}] Sc: [{}] Art: [{}]".format(
                first_random.getObj().getArtist(),
                first_random.getObj().getArtistId(), 
                first_random.getObj().getTitle(),
                first_random.getObj().getId(),
                first_random.getObj().getDuration(),
                first_random.getObj().getSongCount(),
                first_random.getObj().getCoverArt()))
            #pprint(first_random.getData())
            song_list : list[Song] = first_random.getObj().getSongs()
            for current_song in song_list:
                print("[{}] {} {}".format(
                    current_song.getDiscNumber(),
                    current_song.getTrack(),
                    current_song.getTitle()))

def main():
    random_songs(ssc)
    genre_cache : dict[str, str] = {}
    display_genres(ssc, genre_cache)
    # this time it will be faster
    display_genres(ssc, genre_cache)
    display_random_rock_album_list(ssc)
    search_earth_wind_and_fire(ssc)
    display_random_albums(ssc)
    newest_albums(ssc)
    show_artists(ssc)

if __name__ == "__main__":
    main()

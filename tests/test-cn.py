from pprint import pprint
import os
import hashlib

from subsonic_connector.connector import Connector
from subsonic_connector.configuration import Configuration
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
from subsonic_connector.playlists import Playlists
from subsonic_connector.playlist import Playlist
from subsonic_connector.playlist_entry import PlaylistEntry
from subsonic_connector.random_songs import RandomSongs
from subsonic_connector.response import Response
from subsonic_connector.list_type import ListType

from test_config import TestConfig
from invalid_config import RandomPasswordConfiguration

def connector():
    return Connector(TestConfig().connector_configuration())

def search_something():
    ssc = connector()
    search_result : SearchResult = ssc.search(
        TestConfig().searchArgument(),
        artistCount = 10, 
        albumCount = 1000,
        songCount = 1000)
    someArtists : list[Artist] = search_result.getArtists()
    for some_artist in someArtists:
        print("Some Artist: {} [{}]".format(
            some_artist.getName(),
            some_artist.getId()))
    some_albums : list[Album] = search_result.getAlbums()
    some_album : Album
    ac : int = 0
    for some_album in some_albums:
        print("Some Album ndx:[{}] T:[{}] G:[{}]".format(
            ac,
            some_album.getTitle(),
            some_album.getGenre()))
        ac += 1
    some_songs : list[Song] = search_result.getSongs()
    some_song : Song
    sc : int = 0
    for some_song in some_songs:
        print("Some Song ndx:[{}] Title:[{}] Art:[{}] A:[{}] D:[{}] T:[{}]".format(
            sc,
            some_song.getTitle(),
            some_song.getArtist(),
            some_song.getAlbum(),
            some_song.getDiscNumber(),
            some_song.getTrack()))
        sc += 1

def newest_albums():
    ssc = connector()
    # Newest albums (two albums expected)
    newest_album_list : list[Album] = ssc.getNewestAlbumList(size = 2).getObj().getAlbums()
    for album in newest_album_list:
        print("Album [{}] [{}] Year [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getYear(),
            album.getGenre()))

def random_albums() -> list[str]:
    ssc = connector()
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

def download_random_song():
    ssc = connector()
    random_songs_response : Response[RandomSongs] = ssc.getRandomSongs(size = 1)
    if not random_songs_response.isOk():
        print("Request status:", random_songs_response.getStatus())
        return
    random_songs : list[Song] = random_songs_response.getObj().getSongs()
    current_song : Song
    for current_song in random_songs:
        print("Downloading Song [{}] A:[{}] G:[{}] D:[{}] T:[{}]".format(
            current_song.getTitle(), 
            current_song.getAlbum(),
            current_song.getGenre(),
            current_song.getDiscNumber(), 
            current_song.getTrack()))
        filename : str = "song_{}.{}".format(current_song.getId(), current_song.getSuffix())
        with open(filename, mode='wb') as localfile:
            to_download = ssc.download(current_song.getId())
            while chunk := to_download.read(5 * 1000 * 1000):
                localfile.write(chunk)

def random_songs():
    ssc = connector()
    random_songs_response : Response[RandomSongs] = ssc.getRandomSongs(size = 25)
    if not random_songs_response.isOk():
        print("Request status:", random_songs_response.getStatus())
        return
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

def show_artists():
    ssc = connector()
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

def display_genres(cache : dict[str, str]):
    ssc = connector()
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
                str(genre.getName()), 
                cache)

def showCoverArtForGenre(genre : str, cache : dict[str, str]):
    ssc = connector()
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

def display_random_album_list_for_genre():
    ssc = connector()
    response : Response[AlbumList] = ssc.getAlbumList(
        ltype = ListType.BY_GENRE, 
        genre = TestConfig().get_genre())
    album : Album
    for album in response.getObj().getAlbums():
        print("Genre: [{}] Album: [{}] Artist [{}]".format(album.getGenre(), album.getTitle(), album.getArtist()))

def display_random_albums():
    ssc = connector()
    random_album_list : list[str] = random_albums()
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
                ssc

def invalid_credentials():
    cn : Connector = Connector(RandomPasswordConfiguration())
    try:
        cn.ping()
        raise Exception("This was expected to fail")
    except Exception as e:
        print(f"Error [{str(e)}] occurred as expected")

def print_playlist(playlist : Playlist):
    print(f"Playlist id {playlist.getId()} name {playlist.getId()}")
    print(f"  created      {playlist.getCreated()}")
    print(f"  changed      {playlist.getChanged()}")
    print(f"  coverArt     {playlist.getCoverArt()}")
    print(f"  owner        {playlist.getOwner()}")
    print(f"  public       {playlist.getPublic()}")
    print(f"  duration     {playlist.getDuration()}")
    print(f"  songCount    {playlist.getSongCount()}")
    art_uri = connector().buildCoverArtUrl(playlist.getCoverArt())
    print(f"  coverArt uri {art_uri}")
    playlist_entries : list[PlaylistEntry] = playlist.getEntries()
    entry : PlaylistEntry
    for entry in playlist_entries:
        print(f"    id           {entry.getId()}")
        print(f"    parent       {entry.getParent()}")
        print(f"    title        {entry.getTitle()}")
        print(f"    coverArt     {entry.getCoverArt()}")
        stream_url : str = connector().buildSongUrl(entry.getId())
        cover_url : str = connector().buildCoverArtUrl(entry.getCoverArt())
        print(f"    streamUrl    {stream_url}")
        print(f"    coverArtUrl  {cover_url}")

def show_playlists():
    print("using getPlaylists")
    playlists_response : Response[Playlists] = connector().getPlaylists()
    if not playlists_response.isOk(): raise Exception("Cannot retrieve playlists")
    playlists : Playlists = playlists_response.getObj()
    playlist : Playlist
    for playlist in playlists.getPlaylists():
        print_playlist(playlist)
    # also check getPlaylist method
    print("using getPlaylist")
    for playlist in playlists.getPlaylists():
        id : str = playlist.getId()
        playlist_response : Response[Playlist] = connector().getPlaylist(id)
        if not playlist_response.isOk(): raise Exception(f"Cannot retrieve playlist [{id}]")
        print_playlist(playlist_response.getObj())

def main():
    invalid_credentials()
    show_playlists()
    download_random_song()
    random_songs()
    genre_cache : dict[str, str] = {}
    display_genres(genre_cache)
    # this time it will be faster
    display_genres(genre_cache)
    display_random_album_list_for_genre()
    search_something()
    display_random_albums()
    newest_albums()
    show_artists()

if __name__ == "__main__":
    main()

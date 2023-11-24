from pprint import pprint
import os
import hashlib
import secrets

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
from subsonic_connector.top_songs import TopSongs
from subsonic_connector.artist_info import ArtistInfo
from subsonic_connector.similar_artist import SimilarArtist
from subsonic_connector.internet_radio_stations import InternetRadioStations
from subsonic_connector.internet_radio_station import InternetRadioStation
from subsonic_connector.similar_songs import SimilarSongs
from subsonic_connector.response import Response
from subsonic_connector.list_type import ListType
from subsonic_connector.starred import Starred

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
        print("Some Song ndx:[{}] Title:[{}] Art:[{}] A:[{}] D:[{}] T:[{}] G:[{}]".format(
            sc,
            some_song.getTitle(),
            some_song.getArtist(),
            some_song.getAlbum(),
            some_song.getDiscNumber(),
            some_song.getTrack(),
            some_song.getGenre()))
        sc += 1

def newest_albums():
    ssc = connector()
    # Newest albums (two albums expected)
    newest_album_list : list[Album] = ssc.getNewestAlbumList(size = 2).getObj().getAlbums()
    album : Album
    for album in newest_album_list:
        print("Album [{}] [{}] Year [{}] Genre [{}]".format(
            album.getId(), 
            album.getTitle(),
            album.getYear(),
            album.getGenre()))

def highest_rated_albums():
    ssc = connector()
    # highest rated (two albums expected)
    try:
        album_list : list[Album] = ssc.getAlbumList(ltype = ListType.HIGHEST, size = 2).getObj().getAlbums()
        album : Album
        for album in album_list:
            print("Album [{}] [{}] Year [{}] Genre [{}]".format(
                album.getId(), 
                album.getTitle(),
                album.getYear(),
                album.getGenre()))
    except Exception as ex:
        print(f"highest_rated_albums failed [{type(ex)}] [{ex}]")

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
    if not all_artists_initials or len(all_artists_initials) == 0: return
    for current_initial in all_artists_initials:
        # get 1 random artist per initial
        all : list[ArtistListItem] = current_initial.getArtistListItems()
        if not all or len(all) == 0: break
        selected : list[ArtistListItem] = list()
        for i in range(1):
            selected.append(secrets.choice(all))
        cnt : int = 0
        c : ArtistListItem
        for c in selected:
            cnt += 1
            if cnt > max_per_initial:
                break
            print("Count [{}] Initial [{}] Artist: {}".format(
                cnt,
                current_initial.getName(),
                c.getName()))
            artist_cover : ArtistCover = ssc.getCoverByArtistId(c.getId())
            artist_album_id : str
            artist_art_url : str
            hashed_cover_art : str
            if artist_cover:
                artist_art_url = artist_cover.getArtistArtUrl()
                artist_album_id = artist_cover.getAlbumId()
                hashed_cover_art = hashlib.md5(artist_art_url.encode('utf-8')).hexdigest() if artist_art_url else None
                print("Artist Initial[{}] N:[{}] AC:[{}] HashedCover:[{}]".format(
                    current_initial.getName(), 
                    c.getName(), 
                    c.getAlbumCount(),
                    hashed_cover_art))
                print(f"Artist [{c.getId()}] Art Url # [{hashed_cover_art}] Album_id [{artist_album_id}]")

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

def get_artist_covers():
    artists_response : Response[Artists] = connector().getArtists()
    ai_list : list[ArtistsInitial] = artists_response.getObj().getArtistListInitials()
    ai : ArtistsInitial
    for ai in ai_list:
        ali_list : list[ArtistListItem] = ai.getArtistListItems()
        if not ali_list or len(ali_list) == 0: break
        # get 1 random artist
        select : list[ArtistListItem] = list()
        for _ in range(1):
            select.append(secrets.choice(ali_list))
        ali : ArtistListItem
        for ali in select:
            artist_id : str = ali.getId()
            artist_name : str = ali.getName()
            album_count : str = ali.getAlbumCount()
            cover_art : str = ali.getCoverArt()
            artist_image_url : str = ali.getArtistImageUrl()
            cover_art_url : str = connector().buildCoverArtUrl(cover_art) if cover_art else None
            print(f"found id {artist_id} name {artist_name} album_count {album_count} cover_art {cover_art} cover_art_url {cover_art_url} artist_image_url {artist_image_url}")

def random_scrobble():
    response : Response[RandomSongs] = connector().getRandomSongs(size = 1)
    song_list : list[Song] = response.getObj().getSongs()
    if len(song_list) == 0: return
    song : Song = song_list[0]
    scrobble_result : dict = connector().scrobble(song.getId())
    print(f"Song Artist:[{song.getArtist()}] Title:[{song.getTitle()}] Id:[{song.getId()}] scrobbled")

def list_radios():
    try:
        response : Response[InternetRadioStations] = connector().getInternetRadioStations()
        if not response.isOk(): raise Exception("Cannot get radio stations")
        current : InternetRadioStation
        for current in response.getObj().getStations():
            print(f"Radio id:[{current.getId()}] name:[{current.getName()}] streamUrl:[{current.getStreamUrl()}] homePageUrl:[{current.getHomePageUrl()}]")
    except Exception as ex:
        print(f"Cannot get radio stations: [{type(ex)}] [{ex}]")

def top_songs():
    top_song_artist : str = TestConfig().get_top_song_artist()
    try:
        res : Response[TopSongs] = connector().getTopSongs(top_song_artist)
        if not res.isOk(): raise Exception(f"Cannot get top songs for artist {top_song_artist}")
        song : Song
        for song in res.getObj().getSongs():
            print(f"Top song: {song.getTitle()}")
    except Exception as ex:
        print(f"Cannot get top songs by artist: [{top_song_artist}] [{type(ex)}] [{ex}]")

def similar_songs():
    random_songs_response : Response[RandomSongs] = connector().getRandomSongs(size = 1)
    if not random_songs_response.isOk():
        raise Exception("Failed to get random songs")
    if len(random_songs_response.getObj().getSongs()) == 0:
        raise Exception("Cannot get one song")
    song : Song = random_songs_response.getObj().getSongs()[0]
    print(f"Song is [{song.getTitle()}] by [{song.getArtist()}]")
    try:
        similar_songs_by_artist : SimilarSongs = connector().getSimilarSongs(iid = song.getId())
        similar_song : Song
        for similar_song in similar_songs_by_artist.getObj().getSongs():
            print(f"A similar song is [{similar_song.getTitle()}] by [{similar_song.getArtist()}]")
    except Exception as ex:
        print(f"Cannot get similar songs by song_id: [{song.getId()}]")

def artist_radio():
    random_songs_response : Response[RandomSongs] = connector().getRandomSongs(size = 1)
    if not random_songs_response.isOk():
        raise Exception("Failed to get random songs")
    if len(random_songs_response.getObj().getSongs()) == 0:
        raise Exception("Cannot get one song")
    song : Song = random_songs_response.getObj().getSongs()[0]
    print(f"Song is [{song.getTitle()}] by [{song.getArtist()}]")
    try:
        artist_radio : SimilarSongs = connector().getSimilarSongs(iid = song.getArtistId())
        artist_radio_song : Song
        for artist_radio_song in artist_radio.getObj().getSongs():
            print(f"Artist radio song is [{artist_radio_song.getTitle()}] by [{artist_radio_song.getArtist()}]")
    except Exception as ex:
        print(f"Cannot get artist radio for by song_id: [{song.getId()}] artist_id: [{song.getArtistId()}]")

def artist_info():
    top_song_artist : str = TestConfig().get_top_song_artist()
    artist_res : SearchResult = connector().search(top_song_artist, artistCount = 1, albumCount = 0, songCount = 0)
    artist_count : int = len(artist_res.getArtists())
    if artist_count > 0:
        artist_id = artist_res.getArtists()[0].getId()
        res : Response[ArtistInfo] = connector().getArtistInfo(artist_id)
        if not res.isOk(): raise Exception(f"Cannot get top songs for artist {top_song_artist}")
        bio : str = res.getObj().getBiography()
        print(f"Got a bio of [{len(bio) if bio else 0}] characters")
        s_a : SimilarArtist
        sim_art_list : list[SimilarArtist] = res.getObj().getSimilarArtists()
        for s_a in sim_art_list:
            print(f"Similar Artist id: [{s_a.getId()}] name: [{s_a.getName()}]")

def starred():
    res : Response[Starred] = connector().getStarred()
    # artists
    artist_list : list[Artist] = res.getObj().getArtists()
    current_artist : Artist
    for current_artist in artist_list:
        print(f"Found starred artist [{current_artist.getName()}] starred [{current_artist.getStarred()}]")
    # albums
    album_list : list[Album] = res.getObj().getAlbums()
    current_album : Album
    for current_album in album_list:
        print(f"Found starred album [{current_album.getTitle()}] starred [{current_album.getStarred()}]")
    # songs
    song_list : list[Song] = res.getObj().getSongs()
    current_song : Song
    for current_song in song_list:
        print(f"Found starred song [{current_song.getTitle()}] starred [{current_song.getStarred()}]")

def main():
    invalid_credentials()
    search_something()
    newest_albums()
    highest_rated_albums()
    starred()
    top_songs()
    similar_songs()
    artist_radio()
    artist_info()
    list_radios()
    random_scrobble()
    get_artist_covers()
    show_playlists()
    download_random_song()
    random_songs()
    genre_cache : dict[str, str] = {}
    display_genres(genre_cache)
    # this time it will be faster
    display_genres(genre_cache)
    display_random_album_list_for_genre()
    display_random_albums()
    show_artists()

if __name__ == "__main__":
    main()

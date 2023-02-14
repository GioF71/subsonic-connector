import libsonic

from .item import Item
from .artist import Artist
from .artists import Artists
from .album_list import AlbumList
from .album import Album
from .song import Song
from .random_songs import RandomSongs
from .search_result import SearchResult
from .artist_cover import ArtistCover
from .genres import Genres
from .response import Response
from .list_type import ListType

from .configuration import Configuration

class Connector:
    
    def __init__(self, configuration : Configuration):
        self.__configuration = configuration

    def getIndexes(self, 
            musicFolderId = None, 
            ifModifiedSince = 0):
        return self.__connect().getIndexes(
            musicFolderId = musicFolderId, 
            ifModifiedSince = ifModifiedSince)

    def getArtists(self) -> Response[Artists]:
        data = self.__connect().getArtists()
        return Response(data, Artists(data) if data else None)

    def getGenres(self) -> Response[Genres]:
        data = self.__connect().getGenres()
        return Response(data, Genres(data) if data else None)

    def getCoverArtForGenre(self,
            genre : str,
            maxSongs = 20) -> str | None:
        songs : dict = self.__connect().getSongsByGenre(
            genre, 
            maxSongs)
        if not songs: 
            raise Exception("No songs for genre [{}]"
                .format(genre))
        songList = Item(songs).getList(["songsByGenre", "song"])
        if not songList: return None
        coverArt : str = ""
        for current in songList:
            current_art = current["coverArt"]
            if current_art != "": return current_art

    def getRandomSongs(self, 
            size = 10, 
            genre = None, 
            fromYear = None, toYear = None, 
            musicFolderId = None) -> Response[RandomSongs]:
        data : dict = self.__connect().getRandomSongs(
            size = size, 
            genre = genre, 
            fromYear = fromYear, toYear = toYear, 
            musicFolderId = musicFolderId)
        return Response(data, RandomSongs(data) if data else None)

    def getAlbumList(self, 
            ltype : ListType = None, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> Response[AlbumList]:
        data : dict = self.__connect().getAlbumList(
            ltype = ltype.getArgValue() if ltype else None, 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId)
        return Response(data, AlbumList(data) if data else None)

    def getAlbum(self,
            albumId : str) -> Response[Album]:
        data = self.__connect().getAlbum(albumId)
        return Response(data, Album(data) if data else None)

    def getSong(self,
            song_id : str) -> Response[Song]:
        data = self.__connect().getSong(song_id)
        return Response(data, Song(data) if data else None)

    def getNewestAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> Response[AlbumList]:
        return self.getAlbumList(
            ltype = ListType.NEWEST, 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId)

    def getRandomAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> Response[AlbumList]:
        return self.getAlbumList(
            ltype = ListType.RANDOM, 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId)

    def getArtist(self, artist_id : str) -> Response[Artist]:
        data = self.__connect().getArtist(artist_id)
        return Response(data, Artist(data) if data else None)

    def getCoverByArtistId(self, artist_id : str) -> ArtistCover | None:
        artist_response : Response[Artist] = self.getArtist(artist_id)
        if not artist_response and not artist_response.getObj(): return None
        return self.getCoverByArtist(artist_response.getObj())

    def getCoverByArtist(self, artist : Artist) -> ArtistCover | None:
        album_list : list[Album] = artist.getAlbumList()
        current : Album
        for selected_album in album_list:
            select_album_id = selected_album.getId()
            select_album_cover_art = selected_album.getCoverArt()
            if select_album_id and select_album_cover_art:
                return ArtistCover(select_album_id, select_album_cover_art)

    def search(self, 
            query : str, 
            artistCount : int = 20, artistOffset : int = 0, 
            albumCount : int = 20, albumOffset : int = 0, 
            songCount : int = 20, songOffset : int = 0, 
            musicFolderId = None) -> SearchResult:
        return SearchResult(self.__connect().search2(
            query = query,
            artistCount = artistCount, artistOffset = artistOffset, 
            albumCount = albumCount, albumOffset = albumOffset, 
            songCount = songCount, songOffset = songOffset, 
            musicFolderId = musicFolderId))

    def buildSongUrlBySong(self, song : Song) -> str:
        return self.__buildUrl(
            verb = "stream",
            url_dict = {
                "id" : song.getId(), 
                "format" : song.getSuffix()})

    def buildSongUrl(self, song_id : str) -> str:
        song_res : Response[Song] = self.getSong(song_id)
        if song_res:
            return self.buildSongUrlBySong(song = song_res.getObj())

    def buildCoverArtUrl(self, item_id : str) -> str:
        return self.__buildUrl(
            verb = "getCoverArt", 
            url_dict = {"id" : item_id})

    def __addAuthParameters(self, url_dict : dict[str, str] = {}) -> dict[str, str]:
        connection = self.__connect()
        qdict = connection._getBaseQdict()
        url_dict["u"] = self.__configuration.getUserName()
        url_dict["s"] = qdict["s"] #salt
        url_dict["t"] = qdict["t"] #token
        url_dict["c"] = self.__configuration.getAppName()
        url_dict["v"] = self.__configuration.getApiVersion()
        return url_dict
    
    def __buildUrl(self, verb, url_dict : dict[str, str] = {}) -> str:
        url = "{}/rest/{}".format(self.__createBaseUrlWithPort(), verb)
        url_dict = self.__addAuthParameters(url_dict)
        first : bool = True
        for key in url_dict: 
            url += "{}{}={}".format("?" if first else "&", key, url_dict[key])
            first = False
        return url
            
    def __createBaseUrlWithPort(self):
        baseUrl = self.__configuration.getBaseUrl()
        port = self.__configuration.getPort()
        url = baseUrl
        if ((baseUrl and baseUrl.startswith("https://") and port != 443) or 
            (baseUrl and baseUrl.startswith("http://") and port != 80)):
            url = "{}:{}".format(baseUrl, port)
        return url

    def download(self, song_id : str):
        return self.__connect().download(song_id)

    def __connect(self):
        return libsonic.Connection(
            baseUrl = self.__configuration.getBaseUrl(), 
            username = self.__configuration.getUserName(), 
            password = self.__configuration.getPassword(), 
            port = int(str(self.__configuration.getPort())),
            appName = str(self.__configuration.getAppName()),
            apiVersion = str(self.__configuration.getApiVersion()))
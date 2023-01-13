import libsonic

from .item import Item
from .artist import Artist
from .artists import Artists
from .album_list import AlbumList
from .album import Album
from .random_songs import RandomSongs
from .search_result import SearchResult
from .artist_cover import ArtistCover
from .genres import Genres

class Connector:
    
    __KEY_BASE_URL = "baseUrl"
    __KEY_PORT = "port"
    __KEY_USERNAME = "username"
    __KEY_PASSWORD = "password"
    __KEY_API_VERSION = "apiVersion"
    __KEY_APP_NAME = "appName"

    def __init__(
            self,
            baseUrl : str,
            port : int,
            username : str,
            password : str,
            apiVersion : str = libsonic.API_VERSION,
            appName : str = "navibridge"):
        self.__config__ = {}
        self.__config__[Connector.__KEY_BASE_URL] = baseUrl
        self.__config__[Connector.__KEY_PORT] = port
        self.__config__[Connector.__KEY_USERNAME] = username
        self.__config__[Connector.__KEY_PASSWORD] = password
        self.__config__[Connector.__KEY_API_VERSION] = apiVersion
        self.__config__[Connector.__KEY_APP_NAME] = appName
        
    def getIndexes(self, 
            musicFolderId = None, 
            ifModifiedSince = 0):
        return self.__connect().getIndexes(
            musicFolderId = musicFolderId, 
            ifModifiedSince = ifModifiedSince)

    def getArtists(self) -> Artists:
        return Artists(self.__connect().getArtists())

    def getGenres(self) -> Genres:
        return Genres(self.__connect().getGenres())

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
        #songList : list = songs["songsByGenre"]["song"]
        if not songList: return None
        coverArt : str = ""
        for current in songList:
            current_art = current["coverArt"]
            if current_art != "": return current_art

    def getRandomSongs(self, 
            size = 10, 
            genre = None, 
            fromYear = None, toYear = None, 
            musicFolderId = None) -> RandomSongs:
        return RandomSongs(self.__connect().getRandomSongs(
            size = size, 
            genre = genre, 
            fromYear = fromYear, toYear = toYear, 
            musicFolderId = musicFolderId))

    def getAlbumList(self, 
            ltype, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> AlbumList:
        return AlbumList(self.__connect().getAlbumList(
            ltype = ltype, 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId))

    def getNewestAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> AlbumList:
        return self.getAlbumList(
            ltype = "newest", 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId)

    def getRandomAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None) -> AlbumList:
        return self.getAlbumList(
            ltype = "random", 
            size = size, offset = offset, 
            fromYear = fromYear, toYear = toYear,
            genre = genre, musicFolderId = musicFolderId)

    def getArtist(self, artist_id : str) -> Artist:
        return Artist(self.__connect().getArtist(artist_id))

    def getArtistCover(self, artist : Artist) -> ArtistCover | None:
        first_album : str
        first_album_cover_art : str
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

    def buildSongUrl(self, song_id : str) -> str:
        connection = self.__connect()
        qdict = connection._getBaseQdict()
        return "{}/rest/stream?u={}&s={}&t={}&c={}&v={}&id={}".format(
            self.__createBaseUrlWithPort(),
            self.__get_config(Connector.__KEY_USERNAME),
            qdict["s"], # salt
            qdict["t"], # token
            self.__get_config(Connector.__KEY_APP_NAME),
            self.__get_config(Connector.__KEY_API_VERSION),
            song_id);

    def buildCoverArtUrl(self, item_id : str) -> str:
        return self.__buildUrl(verb = "getCoverArt", item_id = item_id)

    def __buildUrl(self, verb, item_id : str) -> str:
        connection = self.__connect()
        qdict = connection._getBaseQdict()
        return "{}/rest/{}?u={}&s={}&t={}&c={}&v={}&id={}".format(
            self.__createBaseUrlWithPort(),
            verb,
            self.__get_config(Connector.__KEY_USERNAME),
            qdict["s"], # salt
            qdict["t"], # token
            self.__get_config(Connector.__KEY_APP_NAME),
            self.__get_config(Connector.__KEY_API_VERSION),
            item_id);
            
    def __get_config(self, name : str) -> str | None:
        return (self.__config__[name] 
            if name in self.__config__ 
            else None)
    
    def __createBaseUrlWithPort(self):
        baseUrl = self.__get_config(Connector.__KEY_BASE_URL)
        port = self.__get_config(Connector.__KEY_PORT)
        url = baseUrl
        if ((baseUrl and baseUrl.startswith("https://") and port != 443) or 
            (baseUrl and baseUrl.startswith("http://") and port != 80)):
            url = "{}:{}".format(baseUrl, port)
        return url
            
    def __connect(self):
        return libsonic.Connection(
            baseUrl = self.__get_config(Connector.__KEY_BASE_URL), 
            username = self.__get_config(Connector.__KEY_USERNAME), 
            password = self.__get_config(Connector.__KEY_PASSWORD), 
            port = int(str(self.__get_config(Connector.__KEY_PORT))),
            appName = str(self.__get_config(Connector.__KEY_APP_NAME)),
            apiVersion = str(self.__get_config(Connector.__KEY_API_VERSION)))
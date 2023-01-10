import libsonic
from artist import Artist
from artists import Artists
from album_list import AlbumList
from album import Album
from random_songs import RandomSongs
from search_result import SearchResult
from artist_cover import ArtistCover

class Connector:
    
    __KEY_BASE_URL = "baseUrl"
    __KEY_PORT = "port"
    __KEY_USERNAME = "username"
    __KEY_PASSWORD = "password"
    __KEY_API_VERSION = "apiVersion"
    __KEY_APP_NAME = "appName"

    def __init__(self, baseUrl : str, port : int, username : str, password : str, apiVersion : str = libsonic.API_VERSION, appName : str = "navibridge"):
        self.__config__ = {}
        self.__config__[Connector.__KEY_BASE_URL] = baseUrl
        self.__config__[Connector.__KEY_PORT] = int(port)
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

    def getArtistCover(self, artist : Artist) -> ArtistCover:
        first_album : str = None
        first_album_cover_art : str = None
        album_list = artist.getAlbumList()
        if len(album_list) > 0:
            first_album = album_list[0]
            selected_album : Album = Album(first_album)
            first_album_id = selected_album.getId()
            first_album_cover_art = selected_album.getCoverArt()
            return ArtistCover(first_album_id, first_album_cover_art)

    def search(self, 
            query, 
            artistCount = 20, artistOffset = 0, 
            albumCount = 20, albumOffset = 0, 
            songCount = 20, songOffset = 0, 
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
            
    def __get_config(self, name : str) -> str:
        return self.__config__[name] if name in self.__config__ else None
    
    def __createBaseUrlWithPort(self):
        baseUrl = self.__get_config(Connector.__KEY_BASE_URL)
        port = self.__get_config(Connector.__KEY_PORT)
        url = baseUrl
        if (baseUrl.startswith("https://") and port != 443) or (baseUrl.startswith("http://") and port != 80):
            url = "{}:{}".format(baseUrl, port)
        return url
            
    def __connect(self):
        return libsonic.Connection(
            baseUrl = self.__get_config(Connector.__KEY_BASE_URL), 
            username = self.__get_config("username"), 
            password = self.__get_config(Connector.__KEY_PASSWORD), 
            port=self.__get_config(Connector.__KEY_PORT),
            appName = self.__get_config(Connector.__KEY_APP_NAME),
            apiVersion = self.__get_config(Connector.__KEY_API_VERSION))
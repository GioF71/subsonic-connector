import libsonic

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
        
    def getRandomSongs(self, size = 10, genre = None, fromYear = None, toYear = None, musicFolderId = None):
        return self.__connect().getRandomSongs(size, genre, fromYear, toYear, musicFolderId)

    def getAlbumList(self, 
            ltype, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None):
        return self.__connect().getAlbumList(
            ltype, 
            size, offset, 
            fromYear, toYear,
            genre, musicFolderId)

    def getNewestAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None):
        return self.__connect().getAlbumList(
            "newest", 
            size, offset, 
            fromYear, toYear,
            genre, musicFolderId)

    def getRandomAlbumList(self, 
            size = 10, offset = 0, 
            fromYear = None, toYear = None, 
            genre = None, musicFolderId = None):
        return self.__connect().getAlbumList(
            "random", 
            size, offset, 
            fromYear, toYear,
            genre, musicFolderId)

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
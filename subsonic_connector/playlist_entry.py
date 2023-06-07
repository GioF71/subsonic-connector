from .item import Item

class PlaylistEntry:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str:
        return self.__item.getByName("id")

    def getParent(self) -> str:
        return self.__item.getByName("parent")
    
    def getTitle(self) -> str:
        return self.__item.getByName("title")

    def getAlbum(self) -> str:
        return self.__item.getByName("album")

    def getArtist(self) -> str:
        return self.__item.getByName("artist")

    def getIsDir(self) -> str:
        return self.__item.getByName("isDir")

    def getCoverArt(self) -> str:
        return self.__item.getByName("coverArt")

    def getCreated(self) -> str:
        return self.__item.getByName("created")

    def getDuration(self) -> str:
        return self.__item.getByName("duration")

    def getBitRate(self) -> str:
        return self.__item.getByName("bitRate")
    
    def getTrack(self) -> str:
        return self.__item.getByName("track")

    def getYear(self) -> str:
        return self.__item.getByName("year")

    def getSize(self) -> str:
        return self.__item.getByName("size")

    def getSuffix(self) -> str:
        return self.__item.getByName("suffix")
    
    def getContentType(self) -> str:
        return self.__item.getByName("contentType")

    def getIsVideo(self) -> str:
        return self.__item.getByName("isVideo")

    def getPath(self) -> str:
        return self.__item.getByName("path")

    def getAlbumId(self) -> str:
        return self.__item.getByName("albumId")

    def getArtistId(self) -> str:
        return self.__item.getByName("artistId")

    def getType(self) -> str:
        return self.__item.getByName("type")

from .item import Item

class PlaylistEntry:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getByName("id")

    def getParent(self) -> str | None:
        return self.__item.getByName("parent")
    
    def getTitle(self) -> str | None:
        return self.__item.getByName("title")

    def getAlbum(self) -> str | None:
        return self.__item.getByName("album")

    def getArtist(self) -> str | None:
        return self.__item.getByName("artist")

    def getIsDir(self) -> str | None:
        return self.__item.getByName("isDir")

    def getCoverArt(self) -> str | None:
        return self.__item.getByName("coverArt")

    def getCreated(self) -> str | None:
        return self.__item.getByName("created")

    def getDuration(self) -> str | None:
        return self.__item.getByName("duration")

    def getBitRate(self) -> str | None:
        return self.__item.getByName("bitRate")
    
    def getTrack(self) -> str | None:
        return self.__item.getByName("track")

    def getYear(self) -> str | None:
        return self.__item.getByName("year")

    def getSize(self) -> str | None:
        return self.__item.getByName("size")

    def getSuffix(self) -> str | None:
        return self.__item.getByName("suffix")
    
    def getContentType(self) -> str | None:
        return self.__item.getByName("contentType")

    def getIsVideo(self) -> str | None:
        return self.__item.getByName("isVideo")

    def getPath(self) -> str | None:
        return self.__item.getByName("path")

    def getAlbumId(self) -> str | None:
        return self.__item.getByName("albumId")

    def getArtistId(self) -> str | None:
        return self.__item.getByName("artistId")

    def getType(self) -> str | None:
        return self.__item.getByName("type")

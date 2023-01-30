from .item import Item

class Song:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getId()

    def getTitle(self) -> str | None:
        return self.__item.getByName("title")

    def getArtist(self) -> str | None:
        return self.__item.getByName("artist")

    def getArtistId(self) -> str | None:
        return self.__item.getByName("artistId")

    def getAlbum(self) -> str | None:
        return self.__item.getByName("album")

    def getAlbumId(self) -> str | None:
        return self.__item.getByName("albumId")

    def getYear(self) -> str | None:
        return self.__item.getByName("year")

    def getDiscNumber(self) -> str | None:
        return self.__item.getByName("discNumber")

    def getTrack(self) -> str | None:
        return self.__item.getByName("track")

    def getCoverArt(self) -> str | None:
        return self.__item.getByName("coverArt")

    def getContentType(self) -> str | None:     
        return self.__item.getByName("contentType")

    def getBitRate(self) -> str | None:
        return self.__item.getByName("bitRate")

    def getSuffix(self) -> str | None:
        return self.__item.getByName("suffix")

    def getDuration(self) -> str | None:
        return self.__item.getByName("duration")

    def getParent(self) -> str | None:        
        return self.__item.getByName("parent")

    def getGenre(self) -> str | None:        
        return self.__item.getByName("genre")

    def getPath(self) -> str | None:
        return self.__item.getByName("path")
        
    def getCreated(self) -> str | None:        
        return self.__item.getByName("created")

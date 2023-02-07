from .item import Item

class Song:

    __dict_name : str = "song"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        select_item : self.__item
        if self.__item.isResponse() and Song.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[Song.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item : Item = select_item

    def getId(self) -> str | None:
        return self.__select_item.getId()

    def getTitle(self) -> str | None:
        return self.__select_item.getByName("title")

    def getArtist(self) -> str | None:
        return self.__select_item.getByName("artist")

    def getArtistId(self) -> str | None:
        return self.__select_item.getByName("artistId")

    def getAlbum(self) -> str | None:
        return self.__select_item.getByName("album")

    def getAlbumId(self) -> str | None:
        return self.__select_item.getByName("albumId")

    def getYear(self) -> str | None:
        return self.__select_item.getByName("year")

    def getDiscNumber(self) -> str | None:
        return self.__select_item.getByName("discNumber")

    def getTrack(self) -> str | None:
        return self.__select_item.getByName("track")

    def getCoverArt(self) -> str | None:
        return self.__select_item.getByName("coverArt")

    def getContentType(self) -> str | None:     
        return self.__select_item.getByName("contentType")

    def getBitRate(self) -> str | None:
        return self.__select_item.getByName("bitRate")

    def getSuffix(self) -> str | None:
        return self.__select_item.getByName("suffix")

    def getDuration(self) -> str | None:
        return self.__select_item.getByName("duration")

    def getParent(self) -> str | None:        
        return self.__select_item.getByName("parent")

    def getGenre(self) -> str | None:        
        return self.__select_item.getByName("genre")

    def getPath(self) -> str | None:
        return self.__select_item.getByName("path")
        
    def getCreated(self) -> str | None:        
        return self.__select_item.getByName("created")

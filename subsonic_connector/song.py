from .item import Item
from .multi_value import get_multi

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

    def getItem(self): return self.__select_item

    def getId(self) -> str:
        return self.__select_item.getId()

    def getTitle(self) -> str:
        return self.__select_item.getByName("title")

    def getArtist(self) -> str:
        return self.__select_item.getByName("artist")

    def getArtistId(self) -> str:
        return self.__select_item.getByName("artistId")

    def getAlbum(self) -> str:
        return self.__select_item.getByName("album")

    def getAlbumId(self) -> str:
        return self.__select_item.getByName("albumId")

    def getYear(self) -> str:
        return self.__select_item.getByName("year")

    def getDiscNumber(self) -> str:
        return self.__select_item.getByName("discNumber")

    def getTrack(self) -> str:
        return self.__select_item.getByName("track")

    def getCoverArt(self) -> str:
        return self.__select_item.getByName("coverArt")

    def getContentType(self) -> str:     
        return self.__select_item.getByName("contentType")

    def getBitRate(self) -> int:
        return self.__select_item.getByName("bitRate")

    def getSuffix(self) -> str:
        return self.__select_item.getByName("suffix")

    def getDuration(self) -> int:
        return self.__select_item.getByName("duration")

    def getParent(self) -> str:        
        return self.__select_item.getByName("parent")

    def getGenre(self) -> str:        
        genre_list : list[str] = self.__get_genres()
        return genre_list[0] if genre_list and len(genre_list) > 0 else None

    def getGenres(self) -> list[str]:
        return self.__get_genres()

    def __get_genres(self) -> list[str]:
        return get_multi(self.__select_item, "genre", "genres", "name")

    def getPath(self) -> str:
        return self.__select_item.getByName("path")
        
    def getCreated(self) -> str:        
        return self.__select_item.getByName("created")

    def getStarred(self) -> str:        
        return self.__select_item.getByName("starred")

from .item import Item
from .song import Song
from .multi_value import get_multi

class Album:

    __key_title : str = "title"
    __key_name : str = "name"

    __dict_name : str = "album"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        select_item = self.__item
        if self.__item.isResponse() and Album.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[Album.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item : Item = select_item

    def getItem(self): return self.__select_item

    def getId(self) -> str:
        return self.__select_item.getByName("id")

    def getArtist(self) -> str:
        return self.__select_item.getByName("artist")

    def getArtistId(self) -> str:
        return self.__select_item.getByName("artistId")

    def getCoverArt(self) -> str:
        return self.__select_item.getByName("coverArt")

    def getTitle(self) -> str:
        title : str = self.__select_item.getByName(Album.__key_title)
        if not title:
            title : str = self.__select_item.getByName(Album.__key_name)
        return title

    def getGenre(self) -> str:
        genre_list : list[str] = self.__get_genres()
        return genre_list[0] if genre_list and len(genre_list) > 0 else None
    
    def getGenres(self) -> list[str]:
        return self.__get_genres()

    def __get_genres(self) -> list[str]:
        return get_multi(self.__select_item, "genre", "genres", "name")

    def getYear(self) -> int:
        return self.__select_item.getByName("year")

    def getOriginalReleaseDate(self) -> str:
        return self.__select_item.getByName("originalReleaseDate")

    def getDuration(self) -> int:
        return self.__select_item.getByName("duration")

    def getSongCount(self) -> int:
        return self.__select_item.getByName("songCount")

    def getStarred(self) -> str:        
        return self.__select_item.getByName("starred")

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.__select_item.getList(["song"])))

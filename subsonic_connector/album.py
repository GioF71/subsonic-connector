from .item import Item
from .song import Song

class Album:

    __dict_name : str = "album"

    def __init__(self, data : dict):
        item : Item = Item(data)
        select_item : item
        if item.isResponse() and Album.__dict_name in data:
            self.__is_response = True
            self.__response = item
            select_item = Item(data[Album.__dict_name])
            self.__key_title = "name"
        else:
            self.__is_response = False
            self.__response = None
            select_item = item
            self.__key_title = "title"
        self.__item : Item = select_item

    def getId(self) -> str | None:
        return self.__item.getByName("id")

    def getArtist(self) -> str | None:
        return self.__item.getByName("artist")

    def getArtistId(self) -> str | None:
        return self.__item.getByName("artistId")

    def getCoverArt(self) -> str | None:
        return self.__item.getByName("coverArt")

    def getTitle(self) -> str | None:
        return self.__item.getByName(self.__key_title)

    def getGenre(self) -> str | None:
        return self.__item.getByName("genre")

    def getDuration(self) -> str:
        return self.__item.getByName("duration")

    def getSongCount(self) -> str:
        return self.__item.getByName("songCount")

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.__item.getList(["song"])))

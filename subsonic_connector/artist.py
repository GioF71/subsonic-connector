from .item import Item
from .album import Album

class Artist:

    __dict_name : str = "artist"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        select_item : self.__item
        if self.__item.isResponse() and Artist.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[Artist.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item : Item = select_item

    def getId(self) -> str | None:
        return self.__select_item.getId()

    def getName(self) -> str | None:
        return self.__select_item.getByName("name")

    def getAlbumCount(self) -> str | None:
        return self.__select_item.getByName("albumCount")

    def getArtistImageUrl(self) -> str | None:
        return self.__select_item.getByName("artistImageUrl")

    def getAlbumList(self) -> list:
        albumList : list = self.__select_item.getList(["album"])
        return list(map(lambda x : Album(x), albumList))

from .item import Item

class Genre:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getName(self) -> str | None:
        return self.__item.getByName("value")

    def getAlbumCount(self) -> str | None:
        return self.__item.getByName("albumCount")

    def getSongCount(self) -> str | None:
        return self.__item.getByName("songCount")
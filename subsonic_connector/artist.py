from .item import Item
from .album import Album

class Artist:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getId()

    def getName(self) -> str | None:
        return self.__item.getByName("name")

    def getAlbumCount(self) -> str | None:
        return self.__item.getByName("albumCount")

    def getArtistImageUrl(self) -> str | None:
        return self.__item.getByName("artistImageUrl")

    def getAlbumList(self) -> list:
        albumList : list = self.__item.getList(["artist", "album"])
        return list(map(lambda x : Album(x), albumList))

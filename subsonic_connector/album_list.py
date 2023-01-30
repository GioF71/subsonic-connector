from .item import Item
from .album import Album

class AlbumList:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getAlbums(self) -> list[Album]:
        l : list = self.__item.getList(["albumList", "album"])
        return list(map(lambda x : Album(x), l))
from .item import Item
from .album import Album

class AlbumList(Item):

    def __init__(self, data : dict):
        super().__init__(data, )

    def getAlbums(self) -> list[Album]:
        l : list = self.getList(["albumList", "album"])
        return list(map(lambda x : Album(x), l))
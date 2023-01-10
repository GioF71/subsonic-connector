from item_list import ItemList
from album import Album

class AlbumList(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["albumList", "album"])

    def getAlbums(self) -> list[Album]:
        l : list = self.getList()
        result : list[Album] = []
        for c in l:
            a : Album = Album(c)
            result.append(a)
        return result

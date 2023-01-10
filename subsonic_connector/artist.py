from item import Item
from item_list import ItemList
from album import Album

class Artist(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getName(self) -> str:
        return self.getByName("name")

    def getAlbumCount(self) -> int:
        return self.getByName("albumCount")

    def getArtistImageUrl(self) -> int:
        return self.getByName("artistImageUrl")

    def getAlbumList(self) -> list:
        itemList : ItemList = ItemList(self.getData(), ["artist", "album"])
        l : list = itemList.getList()
        result : list[Album] = []
        for c in l:
            result.append(Album(c))
        return result


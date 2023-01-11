from .item import Item
from .item_list import ItemList
from .artist_list_item import ArtistListItem

class ArtistsInitial(ItemList):

    def __init__(self, data : dict, list_path = ["artist"]):
        super().__init__(data, list_path)

    def getName(self) -> str | None:
        return self.getByName("name")

    def getArtistListItems(self) -> list[ArtistListItem]:
        l : list = self.getList()
        result : list[ArtistListItem] = []
        for c in l:
            a : ArtistListItem = ArtistListItem(c)
            result.append(a)
        return result

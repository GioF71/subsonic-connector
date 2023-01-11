from .item_list import ItemList
from .artist_list_item import ArtistListItem
from .artists_initial import ArtistsInitial

class Artists(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["artists", "index"])

    def getArtistListInitials(self) -> list[ArtistsInitial]:
        l : list = self.getList()
        result : list[ArtistsInitial] = []
        for c in l:
            a : ArtistsInitial = ArtistsInitial(c)
            result.append(a)
        return result

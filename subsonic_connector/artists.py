from .item_list import ItemList
from .artists_initial import ArtistsInitial

class Artists(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["artists", "index"])

    def getArtistListInitials(self) -> list[ArtistsInitial]:
        l : list = self.getList()
        result : list[ArtistsInitial] = []
        for c in l: result.append(ArtistsInitial(c))
        return result

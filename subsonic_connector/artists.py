from .item import Item
from .artists_initial import ArtistsInitial

class Artists(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getArtistListInitials(self) -> list[ArtistsInitial]:
        return list(map(
            lambda x : ArtistsInitial(x), 
            self.getList(["artists", "index"])))
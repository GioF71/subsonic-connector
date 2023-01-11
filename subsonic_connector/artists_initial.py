from .item import Item
from .artist_list_item import ArtistListItem

class ArtistsInitial(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getName(self) -> str | None:
        return self.getByName("name")

    def getArtistListItems(self) -> list[ArtistListItem]:
        return list(map(
            lambda x : ArtistListItem(x), 
            self.getList(["artist"])))
from .item import Item
from .artist_list_item import ArtistListItem

class ArtistsInitial:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getName(self) -> str | None:
        return self.__item.getByName("name")

    def getArtistListItems(self) -> list[ArtistListItem]:
        return list(map(
            lambda x : ArtistListItem(x), 
            self.__item.getList(["artist"])))
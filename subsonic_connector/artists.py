from .item import Item
from .artists_initial import ArtistsInitial

class Artists:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getItem(self): return self.__item

    def getArtistListInitials(self) -> list[ArtistsInitial]:
        return list(map(
            lambda x : ArtistsInitial(x), 
            self.__item.getList(["artists", "index"])))
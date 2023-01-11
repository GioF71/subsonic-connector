from .item import Item
from .item_list import ItemList

from .album import Album
from .song import Song

class SearchResult(Item):

    __main_element : str = "searchResult2"

    def __init__(self, data : dict):
        super().__init__(data)

    def getAlbums(self) -> list[Album]:
        l : list = ItemList(
            self.getData(), 
            [SearchResult.__main_element, "album"]).getList()
        result : list[Album] = []
        for c in l: result.append(Album(c))
        return result

    def getSongs(self) -> list[Song]:
        l : list = ItemList(
            self.getData(), 
            [SearchResult.__main_element, "song"]).getList()
        result : list[Song] = []
        for c in l: result.append(Song(c))
        return result
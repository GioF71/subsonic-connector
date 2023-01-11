from .item import Item
from .album import Album
from .song import Song

class SearchResult(Item):

    __main_element : str = "searchResult2"

    def __init__(self, data : dict):
        super().__init__(data)

    def getAlbums(self) -> list[Album]:
        return list(map(
            lambda x : Album(x), 
            self.getList([SearchResult.__main_element, "album"])))

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.getList([SearchResult.__main_element, "song"])))

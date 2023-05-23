from .item import Item
from .artist import Artist
from .album import Album
from .song import Song

class SearchResult:

    __main_element : str = "searchResult2"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getArtists(self) -> list[Artist]:
        return list(map(
            lambda x : Artist(x), 
            self.__item.getList([SearchResult.__main_element, "artist"])))

    def getAlbums(self) -> list[Album]:
        return list(map(
            lambda x : Album(x), 
            self.__item.getList([SearchResult.__main_element, "album"])))

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.__item.getList([SearchResult.__main_element, "song"])))

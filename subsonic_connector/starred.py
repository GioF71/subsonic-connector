from .item import Item
from .artist import Artist
from .album import Album
from .song import Song


class Starred:

    __first_entry_name: str = "starred2"

    def __init__(self, data: dict):
        self.__item: Item = Item(data)

    def getItem(self):
        return self.__item

    def getArtists(self) -> list[Artist]:
        return list(map(
            Artist,
            self.__item.getList([Starred.__first_entry_name, "artist"])))

    def getAlbums(self) -> list[Album]:
        return list(map(
            Album,
            self.__item.getList([Starred.__first_entry_name, "album"])))

    def getSongs(self) -> list[Song]:
        return list(map(
            Song,
            self.__item.getList([Starred.__first_entry_name, "song"])))

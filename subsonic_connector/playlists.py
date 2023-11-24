from .item import Item
from .playlist import Playlist

class Playlists:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getItem(self): return self.__item

    def getPlaylists(self) -> list[Playlist]:
        return list(map(
            lambda x : Playlist(x), 
            self.__item.getList(["playlists", "playlist"])))
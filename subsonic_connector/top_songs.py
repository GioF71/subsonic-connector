from .item import Item
from .song import Song

class TopSongs:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.__item.getList(["topSongs", "song"])))
from .item import Item
from .song import Song

class SimilarSongs:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.__item.getList(["similarSongs2", "song"])))
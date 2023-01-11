from .item import Item
from .song import Song

class RandomSongs(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.getList(["randomSongs", "song"])))
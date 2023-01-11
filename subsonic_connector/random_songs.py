from .item_list import ItemList
from .song import Song

class RandomSongs(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["randomSongs", "song"])

    def getSongs(self) -> list[Song]:
        return list(map(lambda x : Song(x), self.getList()))
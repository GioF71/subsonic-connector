from .item_list import ItemList

class RandomSongs(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["randomSongs", "song"])

    def getSongs(self) -> list:
        return self.getList()

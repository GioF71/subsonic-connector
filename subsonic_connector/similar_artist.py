from .item import Item

class SimilarArtist:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getItem(self): return self.__item

    def getId(self) -> str:
        return self.__item.getByName("id")

    def getName(self) -> str:
        return self.__item.getByName("name")



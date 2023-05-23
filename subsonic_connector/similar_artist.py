from .item import Item

class SimilarArtist:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getByName("id")

    def getName(self) -> str | None:
        return self.__item.getByName("name")



from .item import Item
from .genre import Genre

class Genres:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getItem(self): return self.__item

    def getGenres(self) -> list[Genre]:
        return list(map(
            lambda x : Genre(x), 
            self.__item.getList(["genres", "genre"])))
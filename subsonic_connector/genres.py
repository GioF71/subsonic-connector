from .item import Item
from .genre import Genre

class Genres:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getGenres(self) -> list[Genre]:
        return list(map(
            lambda x : Genre(x), 
            self.__item.getList(["genres", "genre"])))
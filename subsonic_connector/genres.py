from .item import Item
from .genre import Genre

class Genres(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getGenres(self) -> list[Genre]:
        l : list = self.getList(["genres", "genre"])
        return list(map(lambda x : Genre(x), l))
from .item_list import ItemList
from .genre import Genre

class Genres(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["genres", "genre"])

    def getGenres(self) -> list[Genre]:
        return list(map(lambda x : Genre(x), self.getList()))
from .response import Response
from .item import Item
from .genre import Genre

class Genres(Response):

    def __init__(self, data : dict):
        super().__init__(Item(data))

    def getGenres(self) -> list[Genre]:
        l : list = self.getItem().getList(["genres", "genre"])
        return list(map(lambda x : Genre(x), l))
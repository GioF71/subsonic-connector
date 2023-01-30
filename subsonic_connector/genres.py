from .item import Item
from .response import Response
from .genre import Genre

class Genres:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        self.__response : Response = Response(data)

    def getResponse(self) -> Response:
        return self.__response

    def getGenres(self) -> list[Genre]:
        return list(map(
            lambda x : Genre(x), 
            self.__item.getList(["genres", "genre"])))
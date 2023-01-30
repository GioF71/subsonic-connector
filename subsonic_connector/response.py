from .item import Item

class Response:
    
    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getStatus(self) -> str | None:
        return self.__item.getByName("status")

    def getVersion(self) -> str | None:
        return self.__item.getByName("version")
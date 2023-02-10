from .item import Item

#from typing import Dict, Generic, TypeVar
from typing import Generic, TypeVar

T = TypeVar("T")

class Response(Generic[T]):

    def __init__(self, data : dict, t : T):
        self.__item : Item = Item(data)
        self.__t = t

    def getObj(self) -> T:
        return self.__t

    def getStatus(self) -> str | None:
        return self.__item.getByName("status")

    def getVersion(self) -> str | None:
        return self.__item.getByName("version")
    
    def isOk(self) -> bool:
        return self.getStatus() == "ok"
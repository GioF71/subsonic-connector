from .item import Item

class ItemList(Item):

    def __init__(self, data : dict, list_path : list[str]):
        super().__init__(data)
        self.__list_path = list_path

    def getList(self) -> list:
        result = self.getData()
        for path in self.__list_path:
            result = result[path]
            if not result: raise Exception("Null item found")
        if not isinstance(result, list): raise Exception("No list found at the specified path")
        return list(result)

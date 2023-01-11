class Item:

    def __init__(self, data : dict):
        self.__data = data

    def getData(self) -> dict:
        return self.__data

    def getByName(self, name : str, defaultValue = None):
        return (self.getData()[name]
            if name in self.getData() 
            else defaultValue)

    def getId(self) -> str | None:
        return self.getByName("id")

    def getList(self, path : list[str]) -> list:
        result = self.getData()
        for current_path in path:
            result = result[current_path]
            if not result: raise Exception("Null item found")
        if not isinstance(result, list): raise Exception("No list found at the specified path")
        return list(result)

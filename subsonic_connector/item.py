class Item:

    def __init__(self, data : dict):
        self.__data = data

    def getData(self) -> dict[str, any]:
        return self.__data

    def isResponse(self) -> bool:
        return (
            "status" in self.getData() and
            "version" in self.getData())

    def hasName(self, name : str) -> bool:
        return name in self.getData()

    def getByName(self, name : str, defaultValue = None) -> any:
        return (self.getData()[name]
            if name in self.getData() 
            else defaultValue)

    def getListByName(self, name : str, defaultValue = []) -> list[dict[str, any]]:
        return (self.getData()[name]
            if name in self.getData() 
            else defaultValue)
    
    def getId(self) -> str:
        return self.getByName("id")

    def getList(self, path : list[str], allowEmpty = True) -> list:
        result = self.getData()
        intermediate : str = ""
        for current_path in path:
            if not type(result) == dict:
                raise Exception(
                    "Intermediate path [{}] does not match a dictionary"
                        .format(intermediate))
            result = (result[current_path] 
                if current_path in result 
                else None)
            if not result and not allowEmpty: raise Exception(
                "Null item found for [{}] in [{}]".format(
                    current_path, 
                    type(self).__name__))
            if not result: return []
            intermediate = current_path
        if not isinstance(result, list): raise Exception(
            "No list found at the specified path")
        return list(result)

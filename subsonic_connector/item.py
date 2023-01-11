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
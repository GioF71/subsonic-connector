from .item import Item

class InternetRadioStation:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str:
        return self.__item.getByName("id")

    def getName(self) -> str:
        return self.__item.getByName("name")

    def getStreamUrl(self) -> str:
        return self.__item.getByName("streamUrl")

    def getHomePageUrl(self) -> str:
        return self.__item.getByName("homePageUrl")
from .item import Item

class InternetRadioStation:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getByName("id")

    def getName(self) -> str | None:
        return self.__item.getByName("name")

    def getStreamUrl(self) -> str | None:
        return self.__item.getByName("streamUrl")

    def getHomePageUrl(self) -> str | None:
        return self.__item.getByName("homePageUrl")
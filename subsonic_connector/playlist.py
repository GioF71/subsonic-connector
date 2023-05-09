from .item import Item
from .playlist_entry import PlaylistEntry

class Playlist:

    __dict_name : str = "playlist"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        select_item : self.__item
        if self.__item.isResponse() and Playlist.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[Playlist.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item : Item = select_item

    def getId(self) -> str | None:
        return self.__select_item.getByName("id")

    def getName(self) -> str | None:
        return self.__select_item.getByName("name")

    def getCreated(self) -> str | None:
        return self.__select_item.getByName("created")

    def getChanged(self) -> str | None:
        return self.__select_item.getByName("changed")

    def getCoverArt(self) -> str | None:
        return self.__select_item.getByName("coverArt")
    
    def getDuration(self) -> str | None:
        return self.__select_item.getByName("duration")
    
    def getOwner(self) -> str | None:
        return self.__select_item.getByName("owner")
    
    def getPublic(self) -> str | None:
        return self.__select_item.getByName("public")
    
    def getSongCount(self) -> str | None:
        return self.__select_item.getByName("songCount")

    def getEntries(self) -> list[PlaylistEntry]:
        result : list[PlaylistEntry] = list(map(
            lambda x : PlaylistEntry(x), 
            self.__select_item.getList(["entry"])))
        return result

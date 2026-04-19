from .item import Item
# from .playlist_entry import PlaylistEntry


class MusicFolder:

    __dict_name: str = "musicFolder"

    def __init__(self, data: dict):
        self.__item: Item = Item(data)
        select_item: Item
        if self.__item.isResponse() and MusicFolder.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[MusicFolder.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item: Item = select_item

    def getItem(self): return self.__select_item

    def getId(self) -> str:
        return self.__select_item.getByName("id")

    def getName(self) -> str:
        return self.__select_item.getByName("name")

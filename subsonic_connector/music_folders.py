from .item import Item
from .music_folder import MusicFolder


class MusicFolders:

    def __init__(self, data: dict):
        self.__item: Item = Item(data)

    def getItem(self): return self.__item

    def getMusicFolders(self) -> list[MusicFolder]:
        return list(map(
            lambda x: MusicFolder(x),
            self.__item.getList(["musicFolders", "musicFolder"])))

from .item import Item

class Genre(Item):

    def __init__(self, dict : dict):
        super().__init__(dict)

    def getName(self) -> str | None:
        return self.getByName("value")

    def getAlbumCount(self) -> str | None:
        return self.getByName("albumCount")

    def getSongCount(self) -> str | None:
        return self.getByName("songCount")
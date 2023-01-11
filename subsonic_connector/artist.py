from .item import Item
from .album import Album

class Artist(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getName(self) -> str | None:
        return self.getByName("name")

    def getAlbumCount(self) -> str | None:
        return self.getByName("albumCount")

    def getArtistImageUrl(self) -> str | None:
        return self.getByName("artistImageUrl")

    def getAlbumList(self) -> list:
        albumList : list = self.getList(["artist", "album"])
        return list(map(lambda x : Album(x), albumList))

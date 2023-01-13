from .item import Item

class ArtistListItem(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getName(self) -> str | None:
        return self.getByName("name")

    def getAlbumCount(self) -> str | None:
        return self.getByName("albumCount")

    def getArtistImageUrl(self) -> str | None:
        return self.getByName("artistImageUrl")

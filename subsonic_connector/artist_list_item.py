from .item import Item

class ArtistListItem:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str | None:
        return self.__item.getId()

    def getName(self) -> str | None:
        return self.__item.getByName("name")

    def getAlbumCount(self) -> str | None:
        return self.__item.getByName("albumCount")

    def getCoverArt(self) -> str | None:
        return self.__item.getByName("coverArt")

    def getArtistImageUrl(self) -> str | None:
        return self.__item.getByName("artistImageUrl")

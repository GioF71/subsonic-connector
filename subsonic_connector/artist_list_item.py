from .item import Item

class ArtistListItem:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getId(self) -> str:
        return self.__item.getId()

    def getName(self) -> str:
        return self.__item.getByName("name")

    def getAlbumCount(self) -> str:
        return self.__item.getByName("albumCount")

    def getCoverArt(self) -> str:
        return self.__item.getByName("coverArt")

    def getArtistImageUrl(self) -> str:
        return self.__item.getByName("artistImageUrl")

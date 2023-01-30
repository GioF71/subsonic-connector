from .item import Item
from .song import Song

class Album(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getArtist(self) -> str | None:
        return self.getByName("artist")

    def getArtistId(self) -> str | None:
        return self.getByName("artistId")

    def getCoverArt(self) -> str | None:
        return self.getByName("coverArt")

    def getTitle(self) -> str | None:
        return self.getByName("title")

    def getGenre(self) -> str | None:
        return self.getByName("genre")

    def getSongs(self) -> list[Song]:
        return list(map(
            lambda x : Song(x), 
            self.getList(["song"])))

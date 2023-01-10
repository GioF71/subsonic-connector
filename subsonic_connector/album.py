from item import Item

class Album(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getArtist(self) -> str:
        return self.getByName("artist")

    def getArtistId(self) -> str:
        return self.getByName("artistId")

    def getCoverArt(self) -> str:
        return self.getByName("coverArt")

    def getTitle(self) -> str:
        return self.getByName("title")

    def getGenre(self) -> str:
        return self.getByName("genre")
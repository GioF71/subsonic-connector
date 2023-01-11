from .item import Item

class Song(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getTitle(self) -> str | None:
        return self.getByName("title")

    def getArtist(self) -> str | None:
        return self.getByName("artist")

    def getArtistId(self) -> str | None:
        return self.getByName("artistId")

    def getAlbum(self) -> str | None:
        return self.getByName("album")

    def getAlbumId(self) -> str | None:
        return self.getByName("albumId")

    def getYear(self) -> str | None:
        return self.getByName("year")

    def getDiscNumber(self) -> str | None:
        return self.getByName("discNumber")

    def getTrack(self) -> str | None:
        return self.getByName("track")

    def getCoverArt(self) -> str | None:
        return self.getByName("coverArt")

    def getContentType(self) -> str | None:     
        return self.getByName("contentType")

    def getBitRate(self) -> str | None:
        return self.getByName("bitRate")

    def getSuffix(self) -> str | None:
        return self.getByName("suffix")

    def getDuration(self) -> str | None:
        return self.getByName("duration")

    def getParent(self) -> str | None:        
        return self.getByName("parent")

    def getGenre(self) -> str | None:        
        return self.getByName("genre")

    def getPath(self) -> str | None:
        return self.getByName("path")
        
    def getCreated(self) -> str | None:        
        return self.getByName("created")

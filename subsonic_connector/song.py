from item import Item

class Song(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getTitle(self) -> str:
        return self.getByName("title")

    def getArtist(self) -> str:
        return self.getByName("artist")

    def getArtistId(self) -> str:
        return self.getByName("artistId")

    def getAlbum(self) -> str:
        return self.getByName("album")

    def getAlbumId(self) -> str:
        return self.getByName("albumId")

    def getYear(self) -> str:
        return self.getByName("year")

    def getDiscNumber(self) -> str:
        return self.getByName("discNumber")

    def getTrack(self) -> str:
        return self.getByName("track")

    def getCoverArt(self) -> str:
        return self.getByName("coverArt")

    def getContentType(self) -> str:     
        return self.getByName("contentType")

    def getBitRate(self) -> str:
        return self.getByName("bitRate")

    def getSuffix(self) -> str:
        return self.getByName("suffix")

    def getDuration(self) -> str:
        return self.getByName("duration")

    def getParent(self) -> str:        
        return self.getByName("parent")

    def getGenre(self) -> str:        
        return self.getByName("genre")

    def getPath(self) -> str:
        return self.getByName("path")
        
    def getCreated(self) -> str:        
        return self.getByName("created")

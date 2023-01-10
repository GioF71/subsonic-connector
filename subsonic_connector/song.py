from item import Item

class Song(Item):

    def __init__(self, data : dict):
        super().__init__(data)

    def getTitle(self):
        return self.getByName("title")

    def getArtist(self):
        return self.getByName("artist")

    def getArtistId(self):
        return self.getByName("artistId")

    def getAlbum(self):
        return self.getByName("album")

    def getAlbumId(self):
        return self.getByName("albumId")

    def getYear(self):
        return self.getByName("year")

    def getDiscNumber(self):
        return self.getByName("discNumber")

    def getTrack(self):
        return self.getByName("track")

    def getCoverArt(self):
        return self.getByName("coverArt")

    def getContentType(self):        
        return self.getByName("contentType")

    def getBitRate(self):        
        return self.getByName("bitRate")

    def getSuffix(self):        
        return self.getByName("suffix")

    def getDuration(self):        
        return self.getByName("duration")

    def getParent(self):        
        return self.getByName("parent")

    def getGenre(self):        
        return self.getByName("genre")

    def getCreated(self):        
        return self.getByName("created")

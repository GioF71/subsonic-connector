class ArtistCover:

    def __init__(self, album_id : str, cover_art : str):
        self.album_id = album_id
        self.cover_art = cover_art

    def getAlbumId(self):
        return self.album_id

    def getCoverArt(self):
        return self.cover_art
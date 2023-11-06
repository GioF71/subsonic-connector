class ArtistCover:

    def __init__(self, artist_id : str, artist_art_url : str, album_id : str = None):
        self._artist_id : str = artist_id
        self._artist_art_url : str = artist_art_url
        self._album_id : str = album_id

    def getArtistId(self) -> str:
        return self._artist_id

    def getArtistArtUrl(self) -> str:
        return self._artist_art_url
    
    def getAlbumId(self) -> str:
        return self._album_id

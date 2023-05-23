from .item import Item
from .similar_artist import SimilarArtist

class ArtistInfo:

    __dict_name : str = "artistInfo"

    def __init__(self, data : dict):
        self.__item : Item = Item(data)
        select_item : self.__item
        if self.__item.isResponse() and ArtistInfo.__dict_name in data:
            self.__is_response = True
            self.__response = self.__item
            select_item = Item(data[ArtistInfo.__dict_name])
        else:
            self.__is_response = False
            self.__response = None
            select_item = self.__item
        self.__select_item : Item = select_item

    def getBiography(self) -> str | None:
        return self.__select_item.getByName("biography")

    def getMusicBrainzId(self) -> str | None:
        return self.__select_item.getByName("musicBrainzId")

    def getLastFmUrl(self) -> str | None:
        return self.__select_item.getByName("lastFmUrl")

    def getSmallImageUrl(self) -> str | None:
        return self.__select_item.getByName("smallImageUrl")

    def getMediumImageUrl(self) -> str | None:
        return self.__select_item.getByName("mediumImageUrl")

    def getLargeImageUrl(self) -> str | None:
        return self.__select_item.getByName("largeImageUrl")

    def getSimilarArtists(self) -> list[SimilarArtist]:
        return list(map(
            lambda x : SimilarArtist(x), 
            self.__select_item.getList(["similarArtist"])))

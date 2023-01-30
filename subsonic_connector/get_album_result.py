from .item import Item
from .song import Song
from .response import Response

class GetAlbumResult:

    def __init__(self, data):
        self.__response = Response(data)
        self.__item = Item(data["album"])

    def getData(self) -> dict:
        return self.__item.getData()

    def getTitle(self) -> str:
        return self.__item.getByName("name")

    def getArtist(self) -> str:
        return self.__item.getByName("artist")

    def getArtistId(self) -> str:
        return self.__item.getByName("artistId")

    def getCoverArt(self) -> str:
        return self.__item.getByName("coverArt")

    def getDuration(self) -> str:
        return self.__item.getByName("duration")

    def getId(self) -> str:
        return self.__item.getByName("id")

    def getSongs(self) -> list:
        song_list : list = self.__item.getList(["song"])
        return list(map(lambda x : Song(x), song_list))

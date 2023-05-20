from .item import Item
from .internet_radio_station import InternetRadioStation

class InternetRadioStations:

    def __init__(self, data : dict):
        self.__item : Item = Item(data)

    def getStations(self) -> list[InternetRadioStation]:
        return list(map(
            lambda x : InternetRadioStation(x), 
            self.__item.getList(["internetRadioStations", "internetRadioStation"])))
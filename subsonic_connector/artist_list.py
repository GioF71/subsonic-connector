from item_list import ItemList

class ArtistList(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["artists", "index"])

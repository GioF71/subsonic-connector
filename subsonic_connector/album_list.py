from item_list import ItemList

class AlbumList(ItemList):

    def __init__(self, data : dict):
        super().__init__(data, ["albumList", "album"])

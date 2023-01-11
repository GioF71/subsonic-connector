from .item import Item

class Response:
    
    def __init__(self, item : Item):
        self.item = item

    def getItem(self):
        return self.item

    def getStatus(self) -> str | None:
        return self.getItem().getByName("status")
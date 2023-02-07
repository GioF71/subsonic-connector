from enum import Enum

class ListType(Enum):
    RANDOM = 0, "random"
    NEWEST = 1, "newest"
    HIGHEST = 2, "highest"
    FREQUENT = 3, "frequent"
    RECENT = 4, "recent"
    STARRED = 5, "starred"
    ALPHABETICAL_BY_NAME = 6, "alphabeticalByName"
    ALPHABETICAL_BY_ARTIST = 7, "alphabeticalByArtist"
    BY_YEAR = 8, "byYear"
    BY_GENRE = 9, "byGenre"

    def __init__(self, num, argValue : str):
        self.num = num
        self.argValue = argValue

    def getArgValue(self):
        return self.argValue
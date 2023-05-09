from subsonic_connector.default_config import DefaultConfiguration

import random, string


class RandomPasswordConfiguration(DefaultConfiguration):

    def __randomword(self, length : int):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def getPassword(self) -> str:
        return self.__randomword(32)

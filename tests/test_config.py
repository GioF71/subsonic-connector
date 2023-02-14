from subsonic_connector.configuration import Configuration
from subsonic_connector.default_config import DefaultConfiguration

import os

class TestConfig:

    def connector_configuration(self) -> Configuration:
        return DefaultConfiguration()

    def searchArgument(self) -> str:
        return os.getenv("SEARCH_ARGUMENT")
    
    def get_genre(self) -> str:
        return os.getenv("USE_GENRE")
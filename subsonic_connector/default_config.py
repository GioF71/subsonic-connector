from .configuration import ConfigurationInterface

import libsonic

import os

class DefaultConfiguration(ConfigurationInterface):

    def __getParameter(self, name : str, default : str = None) -> str:
        return os.getenv(name, default)
    
    def getBaseUrl(self) -> str:
        return self.__getParameter("SUBSONIC_SERVER_URL")
    
    def getPort(self) -> str:
        return self.__getParameter("SUBSONIC_SERVER_PORT")
    
    def getUserName(self) -> str:
        return self.__getParameter("SUBSONIC_USERNAME")
    
    def getPassword(self) -> str:
        return self.__getParameter("SUBSONIC_PASSWORD")
    
    def getLegacyAuth(self) -> bool:
        legacy_auth_enabled_str : str = self.__getParameter("SUBSONIC_LEGACYAUTH", "false")
        if not legacy_auth_enabled_str.lower() in ['true', 'false']: 
            raise Exception(f"Invalid value for SUBSONIC_LEGACYAUTH [{legacy_auth_enabled_str}]")
        return legacy_auth_enabled_str == "true"

    def getApiVersion(self) -> str:
        return self.__getParameter("SUBSONIC_API_VERSION", libsonic.API_VERSION)

    def getAppName(self) -> str:
        return self.__getParameter("SUBSONIC_APP_NAME", "subsonic-connector")
    

    

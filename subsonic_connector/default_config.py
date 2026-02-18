import libsonic
import os
from dotenv import dotenv_values

from .configuration import ConfigurationInterface


class DefaultConfiguration(ConfigurationInterface):

    def __init__(self):
        # custom headers?
        self.__custom_headers: dict[str, str] = {}
        custom_headers_file_name = self.__getParameter("SUBSONIC_CUSTOM_HEADERS_FILE_NAME")
        if custom_headers_file_name:
            custom_headers: dict[str, str] = dotenv_values(custom_headers_file_name)
            self.__custom_headers = custom_headers

    def __getParameter(self, name: str, default: str = None) -> str:
        return os.getenv(name, default)

    def getBaseUrl(self) -> str:
        return self.__getParameter("SUBSONIC_SERVER_URL")

    def getPort(self) -> str:
        return self.__getParameter("SUBSONIC_SERVER_PORT")

    def getServerPath(self) -> str:
        return self.__getParameter("SUBSONIC_SERVER_PATH")

    def getUserName(self) -> str:
        return self.__getParameter("SUBSONIC_USERNAME")

    def getPassword(self) -> str:
        return self.__getParameter("SUBSONIC_PASSWORD")

    def getLegacyAuth(self) -> bool:
        legacy_auth_enabled_str: str = self.__getParameter(
            name="SUBSONIC_LEGACY_AUTH")
        if not legacy_auth_enabled_str:
            legacy_auth_enabled_str = self.__getParameter(
                name="SUBSONIC_LEGACYAUTH")
        if not legacy_auth_enabled_str:
            legacy_auth_enabled_str = "false"
        if not legacy_auth_enabled_str.lower() in ['true', 'false']:
            raise Exception("Invalid value for "
                            f"SUBSONIC_LEGACY_AUTH [{legacy_auth_enabled_str}]")
        return legacy_auth_enabled_str == "true"

    def getSalt(self) -> str:
        return None

    def getToken(self) -> str:
        return None

    def getUserAgent(self) -> str:
        return self.__getParameter("SUBSONIC_USER_AGENT")

    def getCustomHeaders(self) -> dict[str, str]:
        # return self.__custom_headers
        custom_headers_file_name = self.__getParameter("SUBSONIC_CUSTOM_HEADERS_FILE_NAME")
        # print(f"custom_headers_file_name [{custom_headers_file_name}]")
        if custom_headers_file_name:
            custom_headers: dict[str, str] = dotenv_values(custom_headers_file_name)
            # print(f"custom_headers [{custom_headers}]")
            return custom_headers
        return {}

    def getApiVersion(self) -> str:
        return self.__getParameter(
            name="SUBSONIC_API_VERSION",
            default=libsonic.API_VERSION)

    def getAppName(self) -> str:
        return self.__getParameter("SUBSONIC_APP_NAME", "subsonic-connector")

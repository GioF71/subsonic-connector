class ConfigurationMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'getBaseUrl') and 
                callable(subclass.getBaseUrl) and
                hasattr(subclass, 'getPort') and
                callable(subclass.getPort) and
                hasattr(subclass, 'getUserName') and
                callable(subclass.getUserName) and
                hasattr(subclass, 'getPassword') and
                callable(subclass.getPassword) and
                hasattr(subclass, 'getApiVersion') and
                callable(subclass.getApiVersion) and
                hasattr(subclass, 'getAppName') and
                callable(subclass.getAppName))

class ConfigurationInterface:
    def getBaseUrl(self) -> str: pass
    def getPort(self) -> int: pass
    def getUserName(self) -> str: pass
    def getPassword(self) -> str: pass
    def getApiVersion(self) -> str: pass
    def getAppName(self) -> str: pass

class Configuration(metaclass = ConfigurationMeta):
    pass

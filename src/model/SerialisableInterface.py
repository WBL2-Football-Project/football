from typing import Any
from abc import abstractmethod

class SerialisableInterface:
    systemController=Any

    @abstractmethod
    def getSystemController(self):
        return self.__class__.systemController

    @abstractmethod
    def getDb(self):
        return self.__class__.systemController.getDb()
    
    @abstractmethod
    def getApp(self):
        return self.__class__.systemController.getApp()

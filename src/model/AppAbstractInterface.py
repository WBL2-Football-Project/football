from abc import abstractmethod

class AppAbstractInterface:
    @abstractmethod
    def startApplicationLoop(self):
        raise Exception("APPAbstractInterface error: startApplicationLoop method not implemented")

    @abstractmethod
    def setSystemController(self,systemController):
        raise Exception("APPAbstractInterface error: setSystemController method not implemented")

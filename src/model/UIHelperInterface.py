from abc import abstractmethod

class UIHelperInterface:
    def __init__(self,uiHelperImplementation):
        self.implementationObj=uiHelperImplementation

    @abstractmethod
    def startApplicationLoop(self):
        raise Exception("GuiHelperInterface error: startApplicationLoop method not implemented")

    @abstractmethod
    def setSystemController(self,systemController):
        raise Exception("GuiHelperInterface error: setSystemController method not implemented")

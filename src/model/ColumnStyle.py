from enum import Enum
# from SystemControllerAbstract import SystemControllerAbstract


class JustifyEnum(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class ColumnStyle:
    def __init__(self, systemController, name="", visualName="", justify: JustifyEnum = JustifyEnum.LEFT, primaryKey: bool = False):
        self.systemController = systemController
        self.name = name
        self.visualName = self.name if len(visualName) == 0 else visualName
        self.justify = justify
        self.primaryKey = primaryKey

    def getName(self):
        return self.name

    def getVisualName(self):
        return self.visualName

    def getJustify(self):
        return self.justify

    def getJustifyForUI(self):
        return self.systemController.getApp().convertJustifyToUI(self.justify)

    def getPrimaryKey(self):
        return self.primaryKey

from enum import Enum
from typing import Optional

class LayoutTypesEnum(Enum):
    HorizontalStack='HorizontalStack'
    VerticalStack='VerticalStack'
    Grid='Grid'

# exception related to WidgetDefinition class
class ExceptionWidgetDefinition(Exception):
    def __init__(self, message='WidgetDefinition Exception'):
        super().__init__(f"ERROR(WidgetDefinition): {message}")

class WidgetDefinition:
    def __init__(self,layoutType:Optional[LayoutTypesEnum]=None,widgetDefinitionList=None):
        if layoutType==None:
            layoutType = LayoutTypesEnum.VerticalStack
        self.layoutType = layoutType
        self.widgetDefinitionList=widgetDefinitionList if widgetDefinitionList!=None else [] # list of all subsequent widgets definitions
        self.widgetGrid=[] # if layoutType is grid, here we have 2 dimensions array which should contain every widgetDefinition in right cell

    def addWidget(self,widgetDefinition,gridY:Optional[int]=None,gridX:Optional[int]=None):
        self.widgetDefinitionList.append(widgetDefinition)
        if self.layoutType==LayoutTypesEnum.Grid:
            if gridX!=None and gridY!=None:
                self._putWidgetIntoRightCell(gridY,gridX,widgetDefinition)
            else:
                raise ExceptionWidgetDefinition('addWidget call without gridX or gridY specified')
        return self

    def _putWidgetIntoRightCell(self,gridY,gridX,widgetDefinition):
        while len(self.widgetGrid)<gridY:
            self.widgetGrid+=[None]
        while len(self.widgetGrid[gridY])<gridX:
            self.widgetGrid[gridY]+=[None]
        self.widgetDefinitionList[gridY][gridX]=widgetDefinition

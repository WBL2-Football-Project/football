from enum import Enum
from typing import Optional,List
from Widget import *

class LayoutTypesEnum(Enum):
    """Enum definition for LayoutTypes
        LayoutTypesEnum.HorizontalStack
        LayoutTypesEnum.VerticalStack
        LayoutTypesEnum.Grid
    """
    HorizontalStack='HorizontalStack'
    VerticalStack='VerticalStack'
    Grid='Grid'

# exception related to WidgetDefinition class
class ExceptionWidgetDefinition(Exception):
    """Exceptions for WidgetDefinition class"""
    def __init__(self, message='WidgetDefinition Exception'):
        """Launch an exception, e.g.
        ```python
        raise ExceptionWidgetDefinition('The exception/bug short description')
        ```
        """
        super().__init__(f"ERROR(WidgetDefinition): {message}")

class WidgetDefinition:
    """Widget definition class, holds details about designed view layout and every widget expected in there."""
    def __init__(self,layoutType:Optional[LayoutTypesEnum]=None,widgetsList:Optional[List[Widget]]=None):
        """WidgetDefinition __init__ method. You can give it layoutType and widgetDefinitionList instantly here or create a new class instance and call addWidget() method later.
        Rapid WidgetDefinition is possible for simple layout widget list, e.g. Horizontal in which we just put the list of subsequent widgets.
        To use grid-type view, in which widgets are positioned by posY,posX, addWidgetMethod must be used to this.

        Args:
            layoutType (Optional[LayoutTypesEnum], optional): View layout type refers to LayoutTypesEnum. Defaults to None.
            widgetDefinitionList (_type_, optional): List of widget definition objects to be putted into layout. Defaults to None.
        """
        if layoutType==None:
            layoutType = LayoutTypesEnum.VerticalStack
        if not widgetsList is None and layoutType==LayoutTypesEnum.Grid:
            raise ExceptionWidgetDefinition('for Grid layout definition you need to call addWidget() method')
        self.layoutType = layoutType
        self.widgetsList=widgetsList if widgetsList!=None else [] # list of all subsequent widgets definitions
        self.widgetGrid=[] # if layoutType is grid, here we have 2 dimensions array which should contain every widgetDefinition in right cell

    def addWidget(self,widget:Widget,gridY:int,gridX:int):
        """Add new widget to WidgetDefinition object with grid position.

        Args:
            widget (Widget): Widget object instance to add
            gridY (int): position on the vertical axis (Y), first item index is 0 
            gridX (int): position on the horizontal axis (X), first item index is 0

        Raises:
            ExceptionWidgetDefinition: 
                'addWidget call without gridX or gridY specified'

        Returns:
            WidgetDefinition itself: reference to self, you can contineously call addWidget in one like e.g. widgetDefinition.addWidget(...).addWidget(...)...
        """
        self.widgetsList.append(widget)
        if self.layoutType==LayoutTypesEnum.Grid:
            if gridX!=None and gridY!=None:
                self._putWidgetIntoRightCell(gridY,gridX,widget)
            else:
                raise ExceptionWidgetDefinition('addWidget call without gridX or gridY specified')
        return self

    def _putWidgetIntoRightCell(self,gridY,gridX,widget):
        while len(self.widgetGrid)<gridY:
            self.widgetGrid+=[None]
        while len(self.widgetGrid[gridY])<gridX:
            self.widgetGrid[gridY]+=[None]
        self.widgetsList[gridY][gridX]=widget

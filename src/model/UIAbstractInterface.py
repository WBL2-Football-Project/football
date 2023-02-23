from abc import abstractmethod
from typing import Optional,Callable,Any,List
from enum import Enum
from WidgetDefinition import *

# exception related to DBAbstractInterface class
class ExceptionUIAbstractInterface(Exception):
    def __init__(self, message='UIAbstractInterface Exception'):
        super().__init__(f"ERROR(UIAbstractInterface): {message}")

class UIAbstractInterface:
    """Interface class with abstract methods. Need to be implemented by the actual UI managing class which defines all the abstract methods.

    Raises:
        ExceptionUIAbstractInterface: no <method-name> method defined
    """
    @abstractmethod
    def createNewDialog(self, widgetDefinitionObj:WidgetDefinition):
        """Creates a new dialog window on screen and puts widgets in it basing on the @widgetDefinitionObj.

        Args:
            widgetDefinitionObj (WidgetDefinition): _description_

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        raise ExceptionUIAbstractInterface("no createNewDialog method defined")

    @abstractmethod
    def chooseRecordFromList(self, table, filterFunc:Callable[[Any],List[Any]]):
        raise ExceptionUIAbstractInterface("no chooseRecordFromList method defined")

    @abstractmethod
    def inputDataFromUser(self, widgetDefinitionList):
        raise ExceptionUIAbstractInterface("no inputDataFromUser method defined")

    @abstractmethod
    def showInfoMessage(self, title, message):
        raise ExceptionUIAbstractInterface("no showInfoMessage method defined")

    @abstractmethod
    def showErrorMessage(self, title, message):
        raise ExceptionUIAbstractInterface("no showErrorMessage method defined")

    @abstractmethod
    def getCountOfRecordsInTable(self, table):
        raise ExceptionUIAbstractInterface("no getCountOfRecordsInTable method defined")

    @abstractmethod
    def createDialogYesNo(self, title, question): 
        raise ExceptionUIAbstractInterface("no createDialogYesNo method defined")

    @abstractmethod
    def displayListOfRecordsWithExtendedDetails(self, recordList):
        raise ExceptionUIAbstractInterface("no displayListOfRecordsWithExtendedDetails method defined")

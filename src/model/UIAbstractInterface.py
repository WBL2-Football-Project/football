from abc import abstractmethod
from typing import Optional,Callable,Any,List
from enum import Enum
from WidgetDefinition import *
from Serialisable import *
from GroupWithGamesScheduled import *
from SchedulesWithPlay import *

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
        """Prepare creation of a new dialog window on screen, saving widgetDefinitionObj.

        Args:
            widgetDefinitionObj (WidgetDefinition): _description_

        Raises:
            ExceptionUIAbstractInterface: no createNewDialog method defined
        """
        raise ExceptionUIAbstractInterface("no createNewDialog method defined")
    
    @abstractmethod
    def createDialogWithNeededWidgets(self):
        """Setup widgets in new dialog window and activate it on screen for to interact with user."""
        raise ExceptionUIAbstractInterface("no createDialogWithNeededWidgets method defined")

    @abstractmethod
    def chooseRecordFromList(self, table:Serialisable, filterFunc:Optional[Callable[[Any],List[Any]]]=None):
        """Create a window with the list of records from chosen table and let the user select one of them.

        Args:
            table (Serialisable): the class object inherited from the Serialisable class, representing the data in the table in the application database
            filterFunc (Callable[[Any],List[Any]],Optional): _description_

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        raise ExceptionUIAbstractInterface("no chooseRecordFromList method defined")

    @abstractmethod
    def inputDataFromUser(self):
        """Hand out the control of window UI and all created widgets to user for waiting for they answer.
        """
        raise ExceptionUIAbstractInterface("no inputDataFromUser method defined")

    @abstractmethod
    def showInfoMessage(self, title, message):
        """Showing new modal window on screen designed for information message.

        Args:
            title (str): title of the window
            message (str): message text

        """
        raise ExceptionUIAbstractInterface("no showInfoMessage method defined")

    @abstractmethod
    def showErrorMessage(self, title, message):
        """Showing new modal window on screen designed for error message.

        Args:
            title (str): title of the window
            message (str): message text

        """
        raise ExceptionUIAbstractInterface("no showErrorMessage method defined")

    @abstractmethod
    def createDialogYesNo(self, title, question): 
        """Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
        User have to choose one option to close the window.

        Args:
            title (str): title of the window
            message (str): message text

        """
        raise ExceptionUIAbstractInterface("no createDialogYesNo method defined")

    @abstractmethod
    def displayStatisticsForGroupAndItsGamesScheduled(self,dataStruct:List[GroupWithGamesScheduled]):
        raise ExceptionUIAbstractInterface("no displayStatisticsForGroupAndItsGamesScheduled method defined")

    @abstractmethod
    def displayStatisticsForPlayoffScheduledGames(self,dataStruct:List[SchedulesWithPlay]):
        raise ExceptionUIAbstractInterface("no displayStatisticsForPlayoffScheduledGames method defined")

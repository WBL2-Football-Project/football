from abc import abstractmethod
from typing import Optional,Callable,Any,List
from enum import Enum
import inspect
from Serialisable import *
from GroupWithGamesScheduled import *
from SchedulesWithPlay import *
from Teams import Teams
from Users import Users
from Play import Play
from AccountRights import AccountRights

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
    def refreshMainWindowView(self,login:str,rights:AccountRights):
        """The rights changed event handler which is called every time when current account rights of the user are changed to rebuild the UI interface."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def getMainFrame(self):
        """Return the tkinter main window frame reference.

        Raises:
            ExceptionUIAbstractInterface: no getMainFrame method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def dialogForNewTeam(dataObj:Teams) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - teamID
        - name

        Args:
            dataObj (Teams): Teams class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForNewTeam method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def dialogForEditTeam(dataObj:Teams) -> bool:
        """Create dialog window with controls for input edit data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - name

        Args:
            dataObj (Teams): Teams class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForEditTeam method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def refereeDialogForNewUser(self,dataObj:Users,parentFrame:Any) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - login
        - password
        - rights (AccountRights)

        Args:
            dataObj (Users): Users class instance

        Raises:
            ExceptionUIAbstractInterface: no refereeDialogForNewUser method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def dialogForNewUser(self,dataObj:Users,parentFrame:Optional[Any]=None) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - login
        - password

        Args:
            dataObj (Users): Users class instance
            parentFrame (Any): if given a parent frame is used for embed every needed widgets in there, it not - new modal window is created for controls

        Raises:
            ExceptionUIAbstractInterface: no dialogForNewUser method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def refereeDialogForUserRights(self,dataObj:Users) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - rights (AccountRights)
        - password

        Args:
            dataObj (Users): Users class instance

        Raises:
            ExceptionUIAbstractInterface: no refereeDialogForUserRights method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def dialogForEditPlay(dataObj:Play) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - team1GoalsScored (int)
        - team2GoalsScored (int)
        - team1GoalsMissed (int)
        - team2GoalsMissed (int)
        - team1YellowCards (int)
        - team2YellowCards (int)
        - isPlayCompleted (bool)

        Args:
            dataObj (Users): Users class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForEditPlay method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    @abstractmethod
    def dialogForAppLoginOrRegister(dataObj:Play) -> bool:
        """Create dialog window with controls for input new data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        dual tabs layout:
        - "login to app"
            -> dialogForNewUser
        - "register to app"
            -> dialogForNewUser

        Args:
            dataObj (Users): Users class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForAppLoginOrRegister method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")
        
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
    def createDialogYesNo(self, title, question) -> bool: 
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

from abc import abstractmethod
from typing import Optional,Callable,Any,List,Dict
from enum import Enum
import inspect
from AccountRights import AccountRights
from ColumnStyle import JustifyEnum
from ExceptionUIAbstractInterface import ExceptionUIAbstractInterface
from ColumnStyle import ColumnStyle

class UIAbstractInterface:
    """Interface class with abstract methods. Need to be implemented by the actual UI managing class which defines all the abstract methods.

    Raises:
        ExceptionUIAbstractInterface: no <method-name> method defined
    """

    @abstractmethod
    def refreshMainWindowView(self,login:str,rights:AccountRights):
        """The rights changed event handler which is called every time when current account rights of the user are changed to rebuild the UI interface."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def getMainFrame(self) -> Any:
        """Return the tkinter main window frame reference.

        Raises:
            ExceptionUIAbstractInterface: no getMainFrame method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def getMainCanvasFrame(self) -> Any:
        """return the main canvas frame for use to application dialogs.

        Returns:
            UI frame type: return current UI handle to main canvas frame for use to application dialogs
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
    
    @abstractmethod
    def clearMainCanvas(self):
        """Do clear the main canvas before replacing the view with widgets."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
    
    @abstractmethod
    def dialogForNewTeam(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def dialogForEditTeam(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Create dialog window with controls for input edit data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - name

        Args:
            dataObj (Teams): Teams class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForEditTeam method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeDialogForNewUser(self,data,actions:Dict[str,Callable],frame) -> bool:
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def dialogForNewUser(self,data,actions:Dict[str,Callable],frame) -> bool:
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeDialogForUserRights(self,data,actions:Dict[str,Callable],frame) -> bool:
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def dialogForEditPlay(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs) -> bool:
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def dialogForAppLoginOrRegister(data, actions:Dict[str,Callable], parentFrame:Any=None):
        """Create dialog window with controls for input login,password data with additional button for launch register new account.

        Args:
            data (Users): Users class instance
            actions (Dict[str,Callable]): handler for actions of interface: name of id of action and callable for call
            parentFrame : None for open new modal window or handler of UI where to put the dialog controls
        Raises:
            ExceptionUIAbstractInterface: no dialogForAppLoginOrRegister method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
        
    @abstractmethod
    def chooseRecordFromList(self, title:str, headers: List[ColumnStyle], fieldsObj_list: List[Dict[str,Any]], actions:Dict[str,Callable], parentFrame):
    # def chooseRecordFromList(self, table, filterFunc:Optional[Callable[[Any],List[Any]]]=None):
        """Create a window with the list of records from chosen table and let the user select one of them.

        Args:
            table (Serialisable): the class object inherited from the Serialisable class, representing the data in the table in the application database
            filterFunc (Callable[[Any],List[Any]],Optional): condition function to filter the records

        Raises:
            ExceptionUIAbstractInterface: function not implemented
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def showInfoMessage(self, title, message):
        """Showing new modal window on screen designed for information message.

        Args:
            title (str): title of the window
            message (str): message text
            frame: frame of the window handler specific for the UI implementation
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def showErrorMessage(self, title, message):
        """Showing new modal window on screen designed for error message.

        Args:
            title (str): title of the window
            message (str): message text
            frame: frame of the window handler specific for the UI implementation
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def createDialogYesNo(self, title, question) -> bool: 
        """Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
        User have to choose one option to close the window.

        Args:
            title (str): title of the window
            message (str): message text

        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def displayStatisticsForGroupAndItsGamesScheduled(self,dataStruct):
        """_summary_

        Args:
            dataStruct (List[GroupWithGamesScheduled]): _description_

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def displayStatisticsForPlayoffScheduledGames(self,dataStruct):
        """_summary_

        Args:
            dataStruct (List[SchedulesWithPlay]): _description_

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def userMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Create dialog window with application menu with user rights:
            - show match order groups status
            - show match order playoff tree
            - register account
        Raises:
            ExceptionUIAbstractInterface: no method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Create dialog window with application menu with user rights:
            - change user rights
            - edit team data
            - define teams
            - record games data
            - reset application data
            - show match order groups status
            - show match order playoff tree
            - register account
        Raises:
            ExceptionUIAbstractInterface: no method defined
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def destroyMainFrame(self):
        """Destroy the main window and the application."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def convertJustifyToUI(self,justify:JustifyEnum) -> Any:
        """Convert JustifyEnum value to UI specific representation"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def modalDialog(self,title:str,fun:Callable,data:Dict[str,Any],actions:Dict[str,Callable],parentFrame:Any=None,checkFun:Optional[Callable[[Dict],bool]]=None,*args,**kwargs):
        """Create a modal dialog with visual controls generated by given wireframes method, actions procedures and check data function

        Args:
            title (str): window title
            fun (Callable): wireframe function to generate visual controls
            data (Dict[str,Any]): incoming data for generated visual controls as dictionary
            actions (Dict[str,Callable]): named actions Dict with handlers to call to cover specific behavior
            parentFrame (Any, optional): UI specific window frame handler to connect to for dialog. Defaults to None.
            checkFun (Optional[Callable[[Dict],bool]], optional): function to check results data from dialog before it will be closed. Defaults to None.

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

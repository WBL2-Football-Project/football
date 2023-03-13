from abc import abstractmethod
from typing import Dict,Optional,Callable,Any
from Users import Users

class SystemControllerInterface:
    @abstractmethod
    def userMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Generates the application menu for user rights
        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Generates the application menu for referee rights
        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def saveAccount(self,data,*args,**kwargs) -> bool:
        """Transfer State to save user data into the database.

        Args:
            data (Users): users data to save into the database

        Raises:
            ExceptionUIAbstractInterface: not implemented

        Returns:
            bool: True if successful, False otherwise
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def registerAccount(self,data,actions:Dict[str,Callable],embedded:bool=False):
        """User of referee register account. For empty database tables firstly created account is always with highest referee rights.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def defineTeam(self,embeded:bool=True):
        """Define team. This method can be called only with referee rights account."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeEditTeamData(self,embedded:bool=True):
        """Edit team data. This method can be called only with referee rights account."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def calculateGroupPhaseSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        """Calculate group phase schedule. This method can be called only with referee rights account.
        To calculate group phase schedule use the 'Calculate Group Phase Schedule' sequence diagram.
        When done correctly, in the database should be group records and every group phase games schedule saved.
        Controller is transfering this call to @Schedule.calculateGroupPhaseSchedule()

        References: 
            Group
            Schedule
            Schedule.calculateGroupPhaseSchedule()
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def calculatePlayoffPhaseSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        """Calculate playoff phase schedule only if the group phase is already calculated. 
        This method can be called only with referee rights account.
        To calculate playoff phase schedule use the 'Calculate Playoff Phase Schedule' sequence diagram.
        When done correctly, in the database should be every playoff game scheduled with NULL team1/2 ID's 
        but with virtual team1/2 completed for future games with unknown yes compatitors.
        Controller is transfering this call to @Schedule.calculatePlayoffPhaseSchedule()

        References: 
            Schedule
            Schedule.calculateGroupPhaseSchedule()
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def recordGamesDataList(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def recordGamesData(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeResetApplicationData(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        """Reset application data. This method can be called only with referee rights account.
        After this operation is completed, the database is completely cleared and the application works again like during the first run.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def loginToApp(self,data,actions:Dict[str,Callable],embedded:bool=True):
        """Classic login/password authentication. After the data are taken, the application have to check with database if access should be granted.
        Additionally, the application keep the rights level for the account (user or referee rights account)

        - create new dialog window for getting: login, password (refer to UIAbstractInterface create new dialog)
        - get rights from database (refer to DBAbstractInterface get rights from db) and show error message if access isn't granted then go back to login dialog
        - update the login status (refer to SystemController loginStatus)
        - start the application main screen with features access depending on the account rights
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def logoutFromAccount(self,data,actions:Dict[str,Callable],embedded:bool=True):
        """Logout from the current account."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def showMatchOrderGroupsStatus(self):
        """User or referee both can watch the current groups status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def showMatchOrderPlayOffTree(self):
        """User or referee both can watch the current play-off-tree status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def teamsAmountLessThen16(self):
        """Return True if the saved number of teams in the database is less then 16"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def changeUserRights(self,embedded:bool=True):
        """Change the rights for specific users. This call should be transferred to the User.changeUserRights method"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore


    @abstractmethod
    def getRightsFromDb(self,data,*args,**kwargs) -> bool:
        """Transfer State, checks permissions with the database and returns result.

        Args:
            data (Users): users data

        Returns:
            bool: True if successful, False otherwise
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def saveTeam(self,data,*args,**kwargs) -> bool:
        """Transfer State, check new Team record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def refereeEditTeamDataList(self,data,actions:Dict[str,Callable],embedded:bool=False) -> bool:
        """Creates list of Team records on screen with option to edit it."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def saveEditedTeam(self,data,*args,**kwargs):
        """Saves team edited data with checking it before.

        Args:
            data (Dict): dict of all the data after editing
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
    
    @abstractmethod
    def changeUserRightsList(self,data,actions:Dict[str,Callable],embedded:bool=False) -> bool:
        """Creates list of user on screen with option to edit it.

        Args:
            data: not used
            actions (Dict[str,Callable]): action list to send to dialog for manage behaviors
            embedded (bool, optional): not used. Defaults to False.

        Raises:
            ExceptionUIAbstractInterface: _description_

        Returns:
            bool: _description_
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
    
    @abstractmethod
    def saveUserRightChanges(self,data,*args,**kwargs):
        """Saves user edited data with checking it before.

        Args:
            data (Dict): dict of all the data after editing
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    def clearForSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

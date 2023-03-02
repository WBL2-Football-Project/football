import inspect
from typing import Optional
from DBAbstractInterface import *
from UIAbstractInterface import *
from StateMachine import *
from LoginStatus import *
from AppControlInterface import *

# exception related to SystemController class
class ExceptionSystemController(Exception):
    def __init__(self, message='SystemController Exception'):
        super().__init__(f"ERROR(SystemController): {message}")

class SystemController(StateMachine):
    """Main system controller for the application definition. The application instance could start after this controller will be initiated.
    """
    
    def __init__(self, dbControl:DBAbstractInterface, appControl:AppControlInterface):
        """System controller initialisation method with dependency injection convention.
        To successfully create this controller you need to pass two implementation classes, one for DB and the other for UI purposes.
        Every calls to DB or UI have to be made through self.dbImplementationObj and self.uiImplementationObj instances.
        SystemController parent class is StateMachine which keep the information about the current state of the controller and the application,
        including: is user logged in, what kind of rights is granted and is entire schedule of plays generated. The rest of called actions should
        use this information as a source of current application state. Some of actions would change the StateMachine, e.g. loginToApp() or 
        refereeCalculateSchedule() methods.

        Fields:
            dbImplementationObj (DBAbstractInterface) : ready to use object for managing database, which is the implementation class for DBAbstractInterface
            appControl (UIAbstractInterface,APPAbstractInterface) : ready to use object for managing user interface, which is the implementation class for (UIAbstractInterface,APPAbstractInterface)
            loginStatus (LoginStatus) : login status object which keeps the current login status and user permissions to the application and database
        """
        super()
        if not isinstance(dbControl,DBAbstractInterface):
            raise ExceptionSystemController("dbControl must be a DBAbstractInterface implementation")
        if not isinstance(appControl,AppControlInterface):
            raise ExceptionSystemController("appControl must be a AppControl implementation")

        self.dbControl = dbControl
        self.appControl = appControl
        self.loginStatus:LoginStatus = LoginStatus() # default login status (no user identification and no rights to the application and database)
        self.loginStatus.setRightsChangedEventHandler(self.appControl.refreshMainWindowView)

        # starting the main loop of the application independently of the type of user interface chosen (gui/console)
        self.getApp().setSystemController(self)
        self.getApp().startApplicationLoop()

    def getApp(self) -> AppControlInterface:
        """Return the AppControl implementation for UIAbstractInterface and AppAbstractInterface

        Returns:
            AppControlInterface: the helper object used to create the UI interface implementation
        """
        return self.appControl
    
    def getDb(self) -> DBAbstractInterface:
        """Return the implementation for DBAbstractInterface

        Returns:
            DBAbstractInterface: the helper object used to create the UI interface implementation
        """
        return self.dbControl
    
    def registerAccount(self):
        """User of referee register account. For empty database tables firsty created account is always with highest referee rights.
        
        - if not logged in, call user register account
            - if empty database - save the first account with referee rights
        - elif logged in rights are referee
            - call referee register account
        - elif logged in rights are user
            - call user register account
        
        """

        _changes=False
        _user=Users() # empty users instance for holding the data
        # if self.loginStatus.rights == AccountRights.NotLoggedIn:
        #     _changes=self.getApp().dialogForNewUser(_user,self.getApp().getMainFrame())
        #     if self.getDb().getCountOfRecordsInTable(Users)==0:
        #            _user.rights = AccountRights.RefereeRights
        #     # TODO: save the user

        # elif self.loginStatus.rights == AccountRights.UserRights:
        #     _changes=self.getApp().dialogForNewUser(_user,self.getApp().getMainFrame())
        #     # TODO: save the user

        # elif self.loginStatus.rights == AccountRights.RefereeRights:
        #     _changes=self.getApp().refereeDialogForNewUser(_user,self.getApp().getMainFrame())
        #     # TODO: save the user

        # else:
        #     raise ExceptionUIAbstractInterface(f"unknown current rights of an account")
        _changes=self.getApp().refereeDialogForNewUser(_user,self.getApp().getMainFrame()) # temporary for test UI

        if _changes:
            self.loginStatus.loginStatus(_user.login,self.getDb().getRightsFromDb(_user.login,_user.password))

    def defineTeam(self):
        """Define team. This method can be called only with referee rights account."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def refereeEditTeamData(self):
        """Edit team data. This method can be called only with referee rights account."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def calculateGroupPhaseSchedule(self):
        """Calculate group phase schedule. This method can be called only with referee rights account.
        To calculate group phase schedule use the 'Calculate Group Phase Schedule' sequence diagram.
        When done correctly, in the database should be group records and every group phase games schedule saved.
        Controller is transfering this call to @Schedule.calculateGroupPhaseSchedule()

        References: 
            Group
            Schedule
            Schedule.calculateGroupPhaseSchedule()
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def calculatePlayoffPhaseSchedule(self):
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
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def recordGamesData(self):
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def refereeResetApplicationData(self):
        """Reset application data. This method can be called only with referee rights account.
        After this operation is completed, the database is completely cleared and the application works again like during the first run.
        """
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def loginToApp(self,embed:bool=False):
        """Classic login/password authentication. After the data are taken, the application have to check with database if access should be granted.
        Additionally, the application keep the rights level for the account (user or referee rights account)
        
        - create new dialog window for getting: login, password (refer to UIAbstractInterface create new dialog)
        - get rights from database (refer to DBAbstractInterface get rights from db) and show error message if access isn't granted then go back to login dialog
        - update the login status (refer to SystemController loginStatus)
        - start the application main screen with features access depending on the account rights
        """
        
        _user=Users() # empty users instance for holding the data
        if not embed:
            if self.getApp().dialogForNewUser(_user,self.getApp().getMainFrame()):
                self.loginStatus.loginStatus(_user.login,self.getDb().getRightsFromDb(_user.login,_user.password))
        else:
            self.getApp().dialogForNewUser(_user)        

    def showMatchOrderGroupsStatus(self):
        """User or referee both can watch the current groups status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def showMatchOrderPlayOffTree(self):
        """User or referee both can watch the current play-off-tree status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def teamsAmountLessThen16(self):
        """Return True if the saved number of teams in the database is less then 16"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

    def changeUserRights(self):
        """Change the rights for specific users. This call should be transferred to the User.changeUserRights method"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined")

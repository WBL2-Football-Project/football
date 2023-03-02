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
        """User of referee register account. For empty database tables firsty created account is always with highest referee rights."""
        pass

    def defineTeam(self):
        """Define team. This method can be called only with referee rights account."""
        pass

    def refereeEditTeamData(self):
        """Edit team data. This method can be called only with referee rights account."""
        pass

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
        pass

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
        pass

    def recordGamesData(self):
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        pass

    def refereeResetApplicationData(self):
        """Reset application data. This method can be called only with referee rights account.
        After this operation is completed, the database is completely cleared and the application works again like during the first run.
        """
        pass

    def loginToApp(self):
        """Classic login/password authentication. After the data are taken, the application have to check with database if access should be granted.
        Additionally, the application keep the rights level for the account (user or referee rights account)"""
        pass

    def showMatchOrderGroupsStatus(self):
        """User or referee both can watch the current groups status of teams."""
        pass

    def showMatchOrderPlayOffTree(self):
        """User or referee both can watch the current play-off-tree status of teams."""
        pass

    def teamsAmountLessThen16(self):
        """Return True if the saved number of teams in the database is less then 16"""
        pass

    def changeUserRights(self):
        """Change the rights for specific users. This call should be transferred to the User.changeUserRights method"""
        pass

from DBAbstractInterface import *
from UIAbstractInterface import *
from StateMachine import *

# exception related to SystemController class
class ExceptionSystemController(Exception):
    def __init__(self, message='SystemController Exception'):
        super().__init__(f"ERROR(SystemController): {message}")

class SystemController(StateMachine):
    """Main system controller for the application definition. The application instance could start after this controller will be initiated.
    """
    
    def __init__(self, DBImplementationObj:DBAbstractInterface, UIImplementationObj:UIAbstractInterface):
        """System controller initialisation method with dependency injection convention.
        To successfully create this controller you need to pass two implementation classes, one for DB and the other for UI purposes.
        Every calls to DB or UI have to be made through self.dbImplementationObj and self.uiImplementationObj instances.
        SystemController parent class is StateMachine which keep the information about the current state of the controller and the application,
        including: is user logged in, what kind of rights is granted and is entire schedule of plays generated. The rest of called actions should
        use this information as a source of current application state. Some of actions would change the StateMachine, e.g. loginToApp() or 
        refereeCalculateSchedule() methods.
        """
        super()
        if not isinstance(DBImplementationObj,DBAbstractInterface):
            raise ExceptionSystemController("DbImplementationObj must be a DBAbstractInterface")
        if not isinstance(UIImplementationObj,UIAbstractInterface):
            raise ExceptionSystemController("UIAbstractInterface must be a UIAbstractInterface")

        self.dbImplementationObj = DBImplementationObj
        self.uiImplementationObj = UIImplementationObj

    def registerAccount(self):
        """User of referee register account. For empty database tables firsty created account is always with highest referee rights."""
        pass

    def refereeDefineTeam(self):
        """Define team. This method can be called only with referee rights account."""
        pass

    def refereeEditTeamData(self):
        """Edit team data. This method can be called only with referee rights account."""
        pass

    def refereeCalculateSchedule(self):
        """Calculate schedule. This method can be called only with referee rights account."""
        pass

    def refereeRecordGamesData(self):
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
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

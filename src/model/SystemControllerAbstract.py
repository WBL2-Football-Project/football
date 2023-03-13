import inspect
from typing import Optional
from DBAbstractInterface import *
from UIAbstractInterface import *
from ApplicationState import *
from LoginStatus import *
from AppControlInterface import *
from FootballStateMachine import *
from SystemControllerInterface import *
from ExceptionSystemController import *
from StateMachineInterface import StateMachineInterface

class SystemControllerAbstract(ApplicationState,SystemControllerInterface):

    def __init__(self, dbControl: DBAbstractInterface, appControl: AppControlInterface, stateMachine: StateMachineInterface):
        """System controller initialisation method with dependency injection convention.
        To successfully create this controller you need to pass two implementation classes, one for DB and the other for UI purposes.
        Every calls to DB or UI have to be made through self.dbImplementationObj and self.uiImplementationObj instances.
        SystemController parent class is ApplicationState which keep the information about the current state of the controller and the application,
        including: is user logged in, what kind of rights is granted and is entire schedule of plays generated. The rest of called actions should
        use this information as a source of current application state. Some of actions would change the v, e.g. loginToApp() or 
        refereeCalculateSchedule() methods.

        Fields:
            dbImplementationObj (DBAbstractInterface) : ready to use object for managing database, which is the implementation class for DBAbstractInterface
            appControl (UIAbstractInterface,APPAbstractInterface) : ready to use object for managing user interface, which is the implementation class for (UIAbstractInterface,APPAbstractInterface)
            loginStatus (LoginStatus) : login status object which keeps the current login status and user permissions to the application and database
        """
        ApplicationState.__init__(self)
        if not isinstance(dbControl,DBAbstractInterface):
            raise ExceptionSystemController("dbControl must be a DBAbstractInterface implementation")
        if not isinstance(appControl,AppControlInterface):
            raise ExceptionSystemController("appControl must be a AppControl implementation")

        self.dbControl:DBAbstractInterface = dbControl
        self.appControl:AppControlInterface = appControl
        self.loginStatus:LoginStatus = LoginStatus() # default login status (no user identification and no rights to the application and database)
        self.loginStatus.setRightsChangedEventHandler(self.appControl.refreshMainWindowView)

        # staring dbControl class
        self.dbControl.setSystemController(self) # put the system controller ref to dbControl
        self.dbControl.startDatabase(self) # start the database

        # set the system controller access to UI implementation
        self.getApp().setSystemController(self) # put the system controller ref to appControl

        # initialise the FootballStateMachine
        self.stateMachine=stateMachine
        self.stateMachine.setSystemController(self) # put the system controller ref to
        self.stateMachine.initialise() # initialize the definition of state machine for the application

        # start the main loop of the application
        self.getApp().startApplicationLoop() # start the UI

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

    @abstractmethod
    def exitApp(self,*args,**kwargs):
        """Close the entire application."""
        if self.getApp().createDialogYesNo('Exit','Do you want to exit the application?'):
            self.getApp().destroyMainFrame()
            exit(0)

    # @abstractmethod
    # def switchMainCanvasView(self, dialogFun:Callable, data, actions:Dict[str,Callable], parentFrame:Any=None, clear:bool=True) -> Any:
    #     parentFrame=parentFrame if parentFrame is not None else self.getApp().getMainCanvasFrame()
    #     print('parentFrame: ',parentFrame)
    #     if clear: 
    #         self.appControl.clearMainCanvas()
    #     self.getApp().getMainFrame().after(50, dialogFun(data,actions,parentFrame))


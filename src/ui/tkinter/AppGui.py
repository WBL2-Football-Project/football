import os
import sys
from typing import Optional,List,Any,Callable
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from model import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import simpledialog
from tkinter import messagebox
from ModalDialog import ModalDialog
from DialogEmbedWidgets import DialogEmbedWidgets

# starting tkinter helper class
class AppGui(AppControlInterface,tk.Tk):
    def __init__(self):
        """Fields:

            self.systemController (SystemController) : system controller class instance - the core of the control of the application access
                not accessible from iside the __init__ method, but from all the others yes
        """
        # self.systemController:Optional[SystemController]=None

        tk.Tk.__init__(self) # initialisation of the Tk library

        # e.g. root window title and dimension
        self.title("Football Tournament Tracker")

        # e.g. or - set geometry (width x height)
        self.geometry('800x600')

    # AppAbstractInterface implementation shown below:

    def startApplicationLoop(self):

        self.refreshMainWindowView(self.systemController.loginStatus.login,self.systemController.loginStatus.rights)

        # Execute Tkinter window mainloop
        self.mainloop()

    def setSystemController(self, systemController):
        self.systemController = systemController

    def rightsChangedEventHandler(self, login:str, rights:AccountRights):
        print("rightsChangedEventHandler",login,rights)
        self.refreshMainWindowView(login, rights)

    # UIAbstractInterface implementation methods shown below:

    def refreshMainWindowView(self,login:str, rights:AccountRights) -> None:
        # TODO: add the code to remove any unnecessary widgets from main window view when existed (e.g. next call during changing the login information)

        print("refreshMainWindowView")
        if self.systemController.loginStatus.rights == AccountRights.NotLoggedIn:
            # Buid the main window of the application
            # loginToAppButton=tk.Button(self,text='Login')
            # loginToAppButton.pack(padx=35,pady=35)
            # loginToAppButton.bind("<Button-1>",lambda event: self.systemController.loginToApp())

            loginToAppButton=tk.Button(self,text='Register')
            loginToAppButton.pack(padx=35,pady=35)
            loginToAppButton.bind("<Button-1>",lambda event: self.systemController.registerAccount())

            self.systemController.loginToApp(embed=True)
        
        elif self.systemController.loginStatus.rights == AccountRights.UserRights:
            # Build the main window of the application for common user rights access
            # TODO: implement
            pass

        elif self.systemController.loginStatus.rights == AccountRights.RefereeRights:
            # Build the main window of the application for referee rights access
            # TODO: implement
            pass

        else:
            self.showErrorMessage("Error","Error: unknown rights!")
            exit(-1) # exit with error code -1 when rights level unrecognised

    def getMainFrame(self):
        """Return the tkinter main window frame reference."""
        return self
    
    def dialogForNewTeam(self,parentFrame:tk.Frame,dataObj:Teams) -> bool:
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
        _result=False
        return _result

    def dialogForEditTeam(self,parentFrame:tk.Frame,dataObj:Teams) -> bool:
        """Create dialog window with controls for input edit data fields matching the dataObj class instance fields.
        Eventually the dialog set all required dataObj fields (sent by references) with the user specified values 
        and return True if the dialog is confirmed or False otherwise.

        - name

        Args:
            dataObj (Teams): Teams class instance

        Raises:
            ExceptionUIAbstractInterface: no dialogForEditTeam method defined
        """
        _result=False
        return _result

    def refereeDialogForNewUser(self,dataObj:Users,parentFrame:tk.Frame) -> bool:
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
        _result=False

        _result=False
        _appGuiSelf=self

        # opening the modal dialog window for getting the values
        class _modalForNewUser(ModalDialog):
            def __init__(self,parent,login:str,password:str):
                self.login:str=login
                self.password:str=password
                super().__init__(parent,"Login to app",self.showResults)
            
            def showResults(self,result): # shows the results for every vehicle price offer
                if result==True:
                    print("result True")
                    # values checking
                    if len(self.loginVar.get()) != 0 and len(self.passwordVar.get()) != 0: 
                        print("everything's good")
                        # everything is good, we can proceed accepting it and return
                        self.login=self.loginVar.get()
                        self.password=self.passwordVar.get()
                        _result=result
                    else:
                        print("problem with values")
                        # values have to be changed
                        _appGuiSelf.showErrorMessage("Error!","Both login and password cannot be empty.")
                        result=False # return False means the dialog will not be closed until the user repairs the values or close the dialog by 'Cancel' button

                print("return result",result)
                return result # False means, dialog can never be closed by clicking OK button, user have to choose Cancel to close the windows
            
            def body(self, frame): # designs the window widgets
                self.__frame=frame

                # login
                tk.Label(frame,text='Login:').grid(row=0,column=0,columnspan=2,ipady=10,sticky='w')
                self.loginVar=tk.StringVar(frame,self.login)
                tk.Entry(frame,textvariable=self.loginVar).grid(row=1,column=0,columnspan=2,ipady=10,sticky='ew')

                # password
                tk.Label(frame,text='Password:').grid(row=2,column=0,columnspan=2,ipady=10,sticky='w')
                self.passwordVar=tk.StringVar(frame,self.password)
                tk.Entry(frame,textvariable=self.passwordVar).grid(row=3,column=0,columnspan=2,ipady=10,sticky='ew')

                return frame

        _obj=_modalForNewUser(self,dataObj.login,dataObj.password) 
        if _obj.getResult():
            dataObj.login=_obj.login
            dataObj.password=_obj.password
            _result=_obj.getResult()

        return _result

    def dialogForNewUser(self,dataObj:Users,parentFrame:Optional[tk.Frame]=None) -> bool:
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
        _result=False
        _appGuiSelf=self

        if not parentFrame==None:
            # opening the modal dialog window for getting the values
            class _modalForNewUser(ModalDialog):
                def __init__(self,parent,login:str,password:str):
                    self.login:str=login
                    self.password:str=password
                    super().__init__(parent,"Login to app",self.showResults)
                
                def showResults(self,result): # shows the results for every vehicle price offer
                    if result==True:
                        print("result True")
                        # values checking
                        if len(self.loginVar.get()) != 0 and len(self.passwordVar.get()) != 0: 
                            print("everything's good")
                            # everything is good, we can proceed accepting it and return
                            self.login=self.loginVar.get()
                            self.password=self.passwordVar.get()
                            _result=result
                        else:
                            print("problem with values")
                            # values have to be changed
                            _appGuiSelf.showErrorMessage("Error!","Both login and password cannot be empty.")
                            result=False # return False means the dialog will not be closed until the user repairs the values or close the dialog by 'Cancel' button

                    print("return result",result)
                    return result # False means, dialog can never be closed by clicking OK button, user have to choose Cancel to close the windows
                
                def body(self, frame): # designs the window widgets
                    self.__frame=frame

                    # login
                    tk.Label(frame,text='Login:').grid(row=0,column=0,columnspan=2,ipady=10,sticky='w')
                    self.loginVar=tk.StringVar(frame,self.login)
                    tk.Entry(frame,textvariable=self.loginVar).grid(row=1,column=0,columnspan=2,ipady=10,sticky='ew')

                    # password
                    tk.Label(frame,text='Password:').grid(row=2,column=0,columnspan=2,ipady=10,sticky='w')
                    self.passwordVar=tk.StringVar(frame,self.password)
                    tk.Entry(frame,textvariable=self.passwordVar).grid(row=3,column=0,columnspan=2,ipady=10,sticky='ew')

                    return frame

            _obj=_modalForNewUser(self,dataObj.login,dataObj.password) 
            if _obj.getResult():
                dataObj.login=_obj.login
                dataObj.password=_obj.password
                _result=_obj.getResult()
        else:
            # embeding the fields into the given tk frame to manage it
            # TODO: implement it by changing the ModalDialog class for the same behaviour but without opening the separate modal window

            class _embedForNewUser(DialogEmbedWidgets):
                def __init__(self,parent,login:str,password:str):
                    self.login:str=login
                    self.password:str=password
                    super().__init__(parent,"Login to app",self.showResults)
                
                def showResults(self,result): # shows the results for every vehicle price offer
                    if result==True:
                        print("result True")
                        # values checking
                        if len(self.loginVar.get()) != 0 and len(self.passwordVar.get()) != 0: 
                            print("everything's good")
                            # everything is good, we can proceed accepting it and return
                            self.login=self.loginVar.get()
                            self.password=self.passwordVar.get()
                            _result=result
                        else:
                            print("problem with values")
                            # values have to be changed
                            _appGuiSelf.showErrorMessage("Error!","Both login and password cannot be empty.")
                            result=False # return False means the dialog will not be closed until the user repairs the values or close the dialog by 'Cancel' button

                    print("return result",result)
                    return result # False means, dialog can never be closed by clicking OK button, user have to choose Cancel to close the windows
                
                def body(self, frame): # designs the window widgets
                    self.__frame=frame

                    # login
                    tk.Label(frame,text='Login:').grid(row=0,column=0,columnspan=2,ipady=10,sticky='w')
                    self.loginVar=tk.StringVar(frame,self.login)
                    tk.Entry(frame,textvariable=self.loginVar).grid(row=1,column=0,columnspan=2,ipady=10,sticky='ew')

                    # password
                    tk.Label(frame,text='Password:').grid(row=2,column=0,columnspan=2,ipady=10,sticky='w')
                    self.passwordVar=tk.StringVar(frame,self.password)
                    tk.Entry(frame,textvariable=self.passwordVar).grid(row=3,column=0,columnspan=2,ipady=10,sticky='ew')

                    return frame


            _obj=_embedForNewUser(self,dataObj.login,dataObj.password) # TODO: remove it after exchancing the ModalDialog class, described line up
            if _obj.getResult():
                dataObj.login=_obj.login
                dataObj.password=_obj.password
                _result=_obj.getResult()

        return _result

    def refereeDialogForUserRights(self,parentFrame:tk.Frame,dataObj:Users) -> bool:
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
        _result=False
        return _result

    def dialogForEditPlay(self,parentFrame:tk.Frame,dataObj:Play) -> bool:
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
        _result=False
        return _result

    def dialogForAppLoginOrRegister(self,parentFrame:tk.Frame,dataObj:Play) -> bool:
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
        _result=False
        return _result

    def chooseRecordFromList(self, parentFrame:tk.Frame, table:Serialisable, filterFunc:Optional[Callable[[Any],List[Any]]]=None):
        """Create a window with the list of records from chosen table and let the user select one of them.

        Args:
            table (Serialisable): the class object inherited from the Serialisable class, representing the data in the table in the application database
            filterFunc (Callable[[Any],List[Any]],Optional): _description_

        Raises:
            ExceptionUIAbstractInterface: _description_
        """
        pass

    def showInfoMessage(self, title, message):
        """Showing new modal window on screen designed for information message.

        Args:
            title (str): title of the window
            message (str): message text

        """
        pass

    def showErrorMessage(self, title, message):
        """Showing new modal window on screen designed for error message.

        Args:
            title (str): title of the window
            message (str): message text

        """
        pass

    def createDialogYesNo(self, title, question) -> bool: 
        """Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
        User have to choose one option to close the window.

        Args:
            title (str): title of the window
            message (str): message text

        """
        _result=False
        return _result

    def displayStatisticsForGroupAndItsGamesScheduled(self,dataStruct:List[GroupWithGamesScheduled]):
        pass

    def displayStatisticsForPlayoffScheduledGames(self,dataStruct:List[SchedulesWithPlay]):
        pass

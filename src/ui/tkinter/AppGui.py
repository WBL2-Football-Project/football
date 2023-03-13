from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
from model import *
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import wireframes
from ExceptionUIAbstractInterface import ExceptionUIAbstractInterface
from ModalDialog import ModalDialog

# starting tkinter helper class
class AppGui(AppControlInterface, tk.Tk):
    def __init__(self):
        """Fields:

            self.systemController (SystemController) : system controller class instance - the core of the control of the application access
                not accessible from iside the __init__ method, but from all the others yes
        """
        # self.systemController:Optional[SystemController]=None

        tk.Tk.__init__(self)  # initialisation of the Tk library

        # e.g. root window title and dimension
        self.title("Football Tournament Tracker")
        self.mainCanvasFrame=self._genNewMainCanvasFrame()

        # e.g. or - set geometry (width x height)
        self.geometry('800x600')

    # AppAbstractInterface implementation shown below:

    def _genNewMainCanvasFrame(self):
        self.mainCanvasFrame=tk.Frame(self) #,highlightbackground="blue", highlightthickness=2)
        self.mainCanvasFrame.pack(fill=tk.BOTH, expand=1)
        self.testButton=tk.Button(self,text="List database")
        self.testButton.pack()
        self.testButton.bind('<Button-1>',lambda event: self.systemController.getDb().listDbContentToConsole())
        return self.mainCanvasFrame

    def getMainCanvasFrame(self) -> Any:
        return self.mainCanvasFrame
    
    def clearMainCanvas(self):
        self.mainCanvasFrame.destroy()
        self.testButton.destroy()
        self.mainCanvasFrame=self._genNewMainCanvasFrame()
    
    def startApplicationLoop(self):

        self.systemController.stateMachine.start()

        # self.refreshMainWindowView(
        #     self.systemController.loginStatus.login, self.systemController.loginStatus.rights)

        # Execute Tkinter window mainloop
        self.mainloop()

    def setSystemController(self, systemController):
        self.systemController = systemController

    def rightsChangedEventHandler(self, login: str, rights: AccountRights):
        print("rightsChangedEventHandler", login, rights)
        self.refreshMainWindowView(login, rights)

    def refreshMainWindowView(self, login: str, rights: AccountRights) -> None:
        # TODO: add the code to remove any unnecessary widgets from main window view when existed (e.g. next call during changing the login information)

        print("refreshMainWindowView")
        if self.systemController.loginStatus.rights == AccountRights.NotLoggedIn:
            # Buid the main window of the application
            # loginToAppButton=tk.Button(self,text='Login')
            # loginToAppButton.pack(padx=35,pady=35)
            # loginToAppButton.bind("<Button-1>",lambda event: self.systemController.loginToApp())

            loginToAppButton = tk.Button(self, text='Register')
            loginToAppButton.pack(padx=35, pady=35)
            loginToAppButton.bind(
                "<Button-1>", lambda event: self.systemController.registerAccount())

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
            self.showErrorMessage("Error", "Error: unknown rights!")
            exit(-1)  # exit with error code -1 when rights level unrecognised

    def getMainFrame(self):
        """Return the tkinter main window frame reference."""
        return self
    
    def destroyMainFrame(self):
        self.destroy()

    def convertJustifyToUI(self,justify:JustifyEnum) -> Any:
        """Convert JustifyEnum value to UI specific representation"""
        if justify==JustifyEnum.LEFT:
            return tk.E
        elif justify==JustifyEnum.RIGHT:
            return tk.W
        elif justify==JustifyEnum.CENTER:
            return tk.CENTER
        else:
            raise ExceptionUIAbstractInterface(f'convertJustifyToUI error: {justify} not recognized')

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

        _parentFrame=self.getMainFrame()
        class SimpleModalDialog(ModalDialog):
            def __init__(self,parent,genDialogFun:Callable,actions:Dict[str,Callable],title:str,incomeData:Dict[str,Any],checkFun:Optional[Callable]=None):
                self.incomeData=incomeData
                self.tkVars={ k:tk.StringVar(parent,v) for k,v in incomeData.items() }
                self.checkFun=checkFun
                self.resultDataDict={}
                self.genDialogFun=genDialogFun
                super().__init__(parent,title,self.showResults)
            
            def showResults(self,result): # shows the results for every vehicle price offer
                if result==True:
                    self.resultDataDict={ k:v.get() for k,v in self.tkVars.items() }
                    if self.checkFun!=None and not self.checkFun(self.resultDataDict):
                        return False
                    self.setResult(self.resultDataDict)
                    print(f'SimpleModalDialog result True: {self.resultDataDict}')
                return result # False means, dialog can never be closed by clicking OK button, user have to choose Cancel to close the windows
            
            def body(self, frame): # designs the window widgets
                self.__frame=frame
                self.genDialogFun(self.incomeData,actions,frame,self.tkVars)
                return frame

        print("call the CheckOfferDialog")
        _dlg=SimpleModalDialog(_parentFrame,fun,actions,title,data,checkFun)
        result=_dlg.getResult()
        print("FROM MAIN PROCESS, result:",result)

        if type(result)==bool and not result and actions!=None and 'cancel' in actions:
            print('proceeding cancel button')
            actions['cancel']()
        elif actions!=None and 'ok' in actions:
            print('priceeding ok action')
            actions['ok'](result)
        
        return result


    # the rest of UIAbstractInterface implementation is  - L O A D E D -  from sub-module 'wireframes', shown below:

# add all defined wireframes to AppGui class methods: 
setattr(AppGui,"chooseRecordFromList",lambda self,*args,**kwargs:wireframes.chooseRecordFromList(*args,**kwargs))
setattr(AppGui,"createDialogYesNo",lambda self,title,question:wireframes.createDialogYesNo(title,question,self))
setattr(AppGui,"dialogForEditPlay",lambda self,*args,**kwargs:wireframes.dialogForEditPlay(*args,**kwargs))
setattr(AppGui,"dialogForNewTeam",lambda self,*args,**kwargs:wireframes.dialogForNewTeam(*args,**kwargs))
setattr(AppGui,"dialogForEditTeam",lambda self,*args,**kwargs:wireframes.dialogForEditTeam(*args,**kwargs))
setattr(AppGui,"dialogForNewUser",lambda self,*args,**kwargs:wireframes.dialogForNewUser(*args,**kwargs))
setattr(AppGui,"displayStatisticsForGroupAndItsGamesScheduled",lambda self,*args,**kwargs:wireframes.displayStatisticsForGroupAndItsGamesScheduled(*args,**kwargs))
setattr(AppGui,"displayStatisticsForPlayoffScheduledGames",lambda self,*args,**kwargs:wireframes.displayStatisticsForPlayoffScheduledGames(*args,**kwargs))
setattr(AppGui,"refereeDialogForNewUser",lambda self,*args,**kwargs:wireframes.refereeDialogForNewUser(*args,**kwargs))
setattr(AppGui,"refereeDialogForUserRights",lambda self,*args,**kwargs:wireframes.refereeDialogForUserRights(*args,**kwargs))
setattr(AppGui,"showErrorMessage",lambda self,title,content:wireframes.showErrorMessage(title,content,self))
setattr(AppGui,"showInfoMessage",lambda self,title,content:wireframes.showInfoMessage(title,content,self))
setattr(AppGui,"dialogForAppLoginOrRegister",lambda self,*args,**kwargs:wireframes.dialogForAppLoginOrRegister(*args,**kwargs))
setattr(AppGui,"userMenu",lambda self,*args,**kwargs:wireframes.userMenu(*args,**kwargs))
setattr(AppGui,"refereeMenu",lambda self,*args,**kwargs:wireframes.refereeMenu(*args,**kwargs))

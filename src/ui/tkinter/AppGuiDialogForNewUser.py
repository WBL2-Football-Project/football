import os
import sys
from typing import Optional,List,Any,Callable
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from ModalDialog import ModalDialog

class AppGuiDialogForNewUser:
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

        class _DialogForNewUser(ModalDialog):
            def __init__(self,parent,login:str,password:str):
                self.login:str=login
                self.password:str=password
                super().__init__(parent,"Login to app",self.showResults)
            
            def showResults(self,result): # shows the results for every vehicle price offer
                if result==True:
                    # values checking
                    if len(self.login) != 0 and len(self.password) != 0: 
                        # everything is good, we can proceed accepting it and return
                        self.login=self.loginVar.get()
                        self.password=self.passwordVar.get()
                        _result=result
                    else:
                        # values have to be changed
                        _appGuiSelf.showErrorMessage("Error!","Both login and password cannot be empty.")
                        result=False # return False means the dialog will not be closed until the user repairs the values or close the dialog by 'Cancel' button

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

        if parentFrame==None:
            # opening the modal dialog window for getting the values
            _DialogForNewUser(self,dataObj.login,dataObj.password) 

        else:
            # embeding the fields into the given tk frame to manage it
            # TODO: implement it by changing the ModalDialog class for the same behaviour but without opening the separate modal window
            _DialogForNewUser(self,dataObj.login,dataObj.password) # TODO: remove it after exchancing the ModalDialog class, described line up

        return _result

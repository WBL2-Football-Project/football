from abc import abstractmethod
from typing import Callable,Optional
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import simpledialog
from tkinter import messagebox

# helper class to manage universal Dialog Windows
class DialogEmbedWidgets:
    def __init__(self, parent, title, resultFun:Optional[Callable[[bool],bool]]=None):
        """Constructor for DialogEmbedWidgets which placing the widgets into given parent tk.Frame.

        Args:
            parent (tk.Frame): the parent frame to which the dialog is connected
            title (str): window title
            resultFun (bool, optional): End of modal dialog window result handler function. Defaults to None. 
                If given, the result function have to return one of the values:
                    - True if the dialog should be destroyed
                    - False if not
        """
        self.parent=parent
        self.__result=False
        self.__resultFun=resultFun
        self.dialogFrame=tk.Frame(self.parent)
        self.dialogFrame.pack(side=tk.TOP,anchor='nw')
        self.buttonboxFrame=tk.Frame(self.parent)
        self.buttonboxFrame.pack(side=tk.BOTTOM,anchor='nw')
        self.body(self.dialogFrame)
        self.buttonbox(self.buttonboxFrame)
        
    @abstractmethod
    def body(self,frame):
        raise Exception('DialogEmbedWidgets error: no body() method defined')

    def getResult(self): 
        """Returns the result of the dialog.

        Returns:
            bool: result of the dialog
        """
        return self.__result
    
    def onOK(self,event):
        """End of the dialog window by pushing the OK button - event handler.

        Args:
            event (tk.Event): automatically generated by the tk library event
        """
        self.__result=True
        if self.__resultFun!=None:
            self._proceedExit=self.__resultFun(self.__result)
        if type(self._proceedExit) != bool or self._proceedExit:
            self.dialogFrame.destroy()
            self.buttonboxFrame.destroy()
    
    def onCancel(self,event):
        """End of the dialog window by pushing the cancel button - event handler.

        Args:
            event (tk.Event): automatically generated by the tk library event
        """
        self.__result=False
        if self.__resultFun!=None:
            self.__resultFun(self.__result)
        self.dialogFrame.destroy()
        self.buttonboxFrame.destroy()
    
    def buttonbox(self,frame):
        """Dialog windows footer standard cancel/ok buttons to finalise the dialog.
        (this methid could be overwritten in inheritance code if needed)
        """
        self.__onOKButton = tk.Button(frame, text='OK', width=5)
        self.__onOKButton.pack(side="left",padx=5,pady=5)
        self.__onCancelButton = tk.Button(frame, text='Cancel', width=5)
        self.__onCancelButton.pack(side="right",padx=5,pady=5)
        self.__onOKButton.bind("<Button-1>", lambda event: self.onOK(event))
        self.__onCancelButton.bind("<Button-1>", lambda event: self.onCancel(event))

if __name__ == "__main__":

    # dialog window class to manage offer checking feature
    class SampleSimpleModalDialog(DialogEmbedWidgets):
        # constructor
        #	selectedVehiclesList - the list of vehicles to do offer checking
        #	businessLoginObj=None - reference to class providing methods to handle of vehicles
        def __init__(self,parent):
            self.foo='aaa'
            self.bar='bbb'
            super().__init__(parent,"Login to app",self.showResults)
        
        def showResults(self,result): # shows the results for every vehicle price offer
            if result==True:
                self.foo=self._foo_ref.get()
                self.bar=self._bar_ref.get()
            print(f"FROM INSIDE OF CHECKOFFERDIALOG, data {'confirmed: '+self.foo+', '+self.bar if result else 'unconfirmed'}")
            return result # False means, dialog can never be closed by clicking OK button, user have to choose Cancel to close the windows
        
        def body(self, frame): # designs the window widgets
            self.__frame=frame

            # foo label
            _label1=tk.Label(frame,text='Login:')
            _label1.grid(row=0,column=0,columnspan=2,ipady=10,sticky='w')

            self._foo_ref=tk.StringVar(frame,"")
            self._foo_ref.set(self.foo)
            _foo_entry=tk.Entry(frame,textvariable=self._foo_ref)
            _foo_entry.grid(row=1,column=0,columnspan=2,ipady=10,sticky='ew')

            _label2=tk.Label(frame,text='Password:')
            _label2.grid(row=2,column=0,columnspan=2,ipady=10,sticky='w')

            self._bar_ref=tk.StringVar(frame,"")
            self._bar_ref.set(self.bar)
            _bar_entry=tk.Entry(frame,textvariable=self._bar_ref)
            _bar_entry.grid(row=3,column=0,columnspan=2,ipady=10,sticky='ew')

            return frame

    root=tk.Tk() # initialisation of the Tk library
    SampleSimpleModalDialog(root)

    tk.mainloop()

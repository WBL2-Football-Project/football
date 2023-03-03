import os
import sys
from typing import Optional,List,Any,Callable,Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from model import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import simpledialog
from tkinter import messagebox

tkVars={} # helper variable

# Exported dialog procedure:
def refereeDialogForUserRights(fieldsObj,onClickOk,parentFrame):
    """Create dialog window for input fields:
        - rights (AccountRights)
        - password
    """
    global stringVars
    
    global tkVars
    tkVars["password"]=tk.StringVar(parentFrame,fieldsObj.password)
    tkVars["rights"]=tk.StringVar(parentFrame,fieldsObj.rights)

    # TODO: widget for login
    # TODO: widget for password
    # TODO: widget for rights

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.login=""
            self.password=""
            self.rights=""
    fields=Fields()
    def onClickOk(*vars):
        print("Returned:",vars)

    refereeDialogForUserRights(fields,onClickOk,mainFrame)
    onOKButton=tk.Button(mainFrame, text='OK', width=5)
    onOKButton.grid(row=20,column=0,columnspan=2,sticky='w')
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"password":tkVars["password"].get(),"rights":tkVars["rights"].get()}))

    mainFrame.mainloop()

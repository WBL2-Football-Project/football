from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
# from model import *
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))
from AccountRights import AccountRights

tkVars = {}  # helper variable

# Exported dialog procedure:

def refereeDialogForUserRights(data, actions, parentFrame, tkVars:Dict={}):
    """Create dialog window for input fields:
        - rights (AccountRights)
        - password
    """
    tkVars["password"] = tk.StringVar(parentFrame, data["password"])
    tkVars["rights"] = tk.StringVar(parentFrame, data["rights"])

    rightsList=[ {'key':c.value,'value':c.name} for c in filter(lambda x: x!=AccountRights.NotLoggedIn,AccountRights) ]
    print('rightsList',rightsList)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    tk.Label(parentFrame, text="Password", font=('Helvetica', 10)).grid(row=2, pady=(10, 5))
    tk.Entry(parentFrame, width=40,textvariable=tkVars["password"]).grid(ipady=5, row=3)

    radioButtonsFrame = tk.Frame(parentFrame)
    radioButtonsFrame.grid(row=4, pady=15)
    radioButtonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    _rightsRadio=[]
    _col=0
    for rdef in rightsList:
        tk.Radiobutton(radioButtonsFrame, text=rdef['key'],variable=tkVars["rights"], value=rdef['value']).grid(row=0, column=_col, sticky='w')
        _col+=1


    # TODO: widget for rights


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.login = ""
            self.password = ""
            self.rights = ""
    fields = Fields()

    def onClickOk(*vars):
        print("Returned:", vars)

    refereeDialogForUserRights(fields, onClickOk, mainFrame)

    mainFrame.mainloop()

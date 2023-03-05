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


tkVars = {}  # helper variable

# Exported dialog procedure:


def refereeDialogForUserRights(fieldsObj, onClickOk, parentFrame):
    """Create dialog window for input fields:
        - rights (AccountRights)
        - password
    """
    global stringVars

    global tkVars
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["rights"] = tk.StringVar(parentFrame, fieldsObj.rights)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    userRightsFrame = tk.Frame(parentFrame)
    userRightsFrame.grid()

    passwordLabel = tk.Label(
        userRightsFrame, text="Password", font=('Helvetica', 10)).grid(row=2, pady=(10, 5))

    password = tk.Entry(userRightsFrame, width=40,
                        textvariable=tkVars["password"])
    password.grid(ipady=5, row=3)

    buttonsFrame = tk.Frame(userRightsFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=20)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind(
        "<Button-1>", lambda event: onClickOk({"password": tkVars["password"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: userRightsFrame.destroy())

    # TODO: widget for login
    # TODO: widget for password
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

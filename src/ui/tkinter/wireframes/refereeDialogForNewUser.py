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


def refereeDialogForNewUser(fieldsObj, onClickOk, parentFrame):
    """Create dialog window for input fields:
        - login
        - password
        - rights (AccountRights)
    """
    global stringVars

    global tkVars
    tkVars["login"] = tk.StringVar(parentFrame, fieldsObj.login)
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["rights"] = tk.StringVar(parentFrame, fieldsObj.rights)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    usernameLabel = tk.Label(
        parentFrame, text="Username", font=('Helvetica', 10)).grid(row=0, pady=(10, 5))

    username = tk.Entry(parentFrame, width=40, textvariable=tkVars["login"])
    username.grid(ipady=5, row=1)

    passwordLabel = tk.Label(
        parentFrame, text="Password", font=('Helvetica', 10)).grid(row=2, pady=(10, 5))

    password = tk.Entry(parentFrame, width=40, textvariable=tkVars["password"])
    password.grid(ipady=5, row=3)

    radioButtonsFrame = tk.Frame(parentFrame)
    radioButtonsFrame.grid(row=4, pady=15)
    radioButtonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    refereeRadio = tk.Radiobutton(radioButtonsFrame, text="Referee",
                                  variable=tkVars["rights"], value='Referee Rights').grid(row=0, column=0, sticky='w')

    userRadio = tk.Radiobutton(radioButtonsFrame, text="User",
                               variable=tkVars["rights"], value='User Rights').grid(row=0, column=1, sticky='w')

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=20)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"login": tkVars["login"].get(
    ), "password": tkVars["password"].get(), "rights": tkVars["rights"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: parentFrame.destroy())


# TODO: widget for login
# TODO: widget for password
# TODO: widget for rights


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new user")
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

    refereeDialogForNewUser(fields, onClickOk, mainFrame)

    mainFrame.mainloop()

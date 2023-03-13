from AccountRights import AccountRights
from tkinter import messagebox
from tkinter import simpledialog
from .constants import *
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


# def refereeDialogForNewUser(fieldsObj, onClickOk, parentFrame):
def refereeDialogForNewUser(fieldsObj, actions, parentFrame):
    """Create dialog window for input fields:
        - login
        - password
        - rights (AccountRights)
    """
    global tkVars
    rightsList = [{'key': c.name, 'value': c.value} for c in filter(
        lambda x: x != AccountRights.NotLoggedIn, AccountRights)]
    tkVars["login"] = tk.StringVar(parentFrame, fieldsObj.login)
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["rights"] = tk.StringVar(parentFrame, fieldsObj.rights)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # newUserFrame = tk.Frame(parentFrame)
    # newUserFrame.grid()

    usernameLabel = tk.Label(parentFrame, text="Username", font=(
        FONT, 10)).grid(row=0, pady=(10, 5))

    username = tk.Entry(parentFrame, width=40,
                        textvariable=tkVars["login"], font=(FONT, 10))
    username.grid(ipady=5, row=1)

    passwordLabel = tk.Label(parentFrame, text="Password", font=(
        FONT, 10)).grid(row=2, pady=(10, 5))

    password = tk.Entry(parentFrame, width=40,
                        textvariable=tkVars["password"], show="*", font=(FONT, 10))
    password.grid(ipady=5, row=3)

    radioButtonsFrame = tk.Frame(parentFrame)
    radioButtonsFrame.grid(row=4, pady=15)
    radioButtonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    _rightsRadio = []
    _col = 0
    for rdef in rightsList:
        tk.Radiobutton(radioButtonsFrame, text=rdef['value'], variable=tkVars['rights'], value=rdef['key'], font=(FONT, 10)).grid(
            row=0, column=_col, sticky='w')
        _col += 1

    # refereeRadio = tk.Radiobutton(radioButtonsFrame, text="Referee",variable=tkVars["rights"], value='Referee Rights').grid(row=0, column=0, sticky='w')
    # userRadio = tk.Radiobutton(radioButtonsFrame, text="User",variable=tkVars["rights"], value='User Rights').grid(row=0, column=1, sticky='w')

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='Add User', width=20,
                           background=PRIMARY_COLOUR, foreground='#FFFFFF', font=(FONT, 10))
    onOKButton.grid(row=0, column=0, ipadx=2, ipady=2)
    if actions != None and 'ok' in actions:
        onOKButton.bind("<Button-1>", lambda event: actions['ok']({"login": tkVars["login"].get(
        ), "password": tkVars["password"].get(), "rights": AccountRights[tkVars["rights"].get()]}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20,
                               background=SECONDARY_COLOUR, foreground='#FFFFFF', font=(FONT, 10))
    onCancelButton.grid(row=0, column=1, padx=15, ipadx=2, ipady=2)
    if actions != None and 'cancel' in actions:
        onCancelButton.bind(
            "<Button-1>", lambda event: actions['cancel']())


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

    def onCancel(*vars):
        print("Cancel")
        exit(0)

    refereeDialogForNewUser(
        fields, {'ok': onClickOk, 'cancel': onCancel}, mainFrame)

    mainFrame.mainloop()

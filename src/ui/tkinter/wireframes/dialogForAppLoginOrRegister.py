from StateMachine import State
from tkinter import messagebox
from tkinter import simpledialog
from .constants import *
import tkinter.font as tkfont
from tkinter import ttk
#from model import *
import tkinter as tk
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src', 'model')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

print(os.getcwd(), os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'src', 'model')))


tkVars = {}  # helper variable

# Exported dialog procedure:


def dialogForAppLoginOrRegister(fieldsObj, actions: Dict[str, Callable], parentFrame: Any = None):
    """Create dialog window for input fields:
        - login
        - password
    """
    global tkVars
    tkVars["login"] = tk.StringVar(parentFrame, fieldsObj.login)
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    usernameLabel = tk.Label(parentFrame, text="Username", font=(
        FONT, 10)).grid(row=0, pady=(10, 5))
    username = tk.Entry(parentFrame, width=40,
                        textvariable=tkVars["login"], font=(FONT, 10)).grid(ipady=5, row=1)

    passwordLabel = tk.Label(parentFrame, text="Password", font=(
        FONT, 10)).grid(row=2, pady=(10, 5))
    password = tk.Entry(parentFrame, width=40,
                        textvariable=tkVars["password"], show="*", font=(FONT, 10)).grid(ipady=5, row=3)

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='Login', width=20,
                           background=PRIMARY_COLOUR, foreground="#FFFFFF", font=('FONT', 10))
    onOKButton.grid(row=0, padx=15, ipadx=2, ipady=2)
    if 'ok' in actions:
        onOKButton.bind("<Button-1>", lambda event: actions['ok'](
            {"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    # Cancel Button
    # onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20, background='#15161B', foreground="#FFFFFF", font=('FONT', 10))
    # onCancelButton.grid(row=0, column=0, padx=15, sticky='w')
    # if 'cancel' in actions:
    #     onCancelButton.bind("<Button-1>", lambda event: actions['cancel']()) # old: onCancelButton.bind("<Button-1>", lambda event: newUserFrame.destroy())

    # Register Button
    onRegisterButton = tk.Button(buttonsFrame, text='Don\'t have an account?',
                                 width=20, background=PRIMARY_COLOUR, foreground="#FFFFFF", font=(FONT, 10))
    onRegisterButton.grid(row=2, padx=15, pady=15, ipadx=2, ipady=2)
    if 'register' in actions:
        onRegisterButton.bind("<Button-1>", lambda event: actions['register'](
            {"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    footerFrame = tk.Frame(parentFrame)
    footerFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    footerFrame.rowconfigure(1, weight=1)
    footerFrame.grid(row=6)

    appNameLabel = tk.Label(
        footerFrame, text="TourneyTracker", foreground=SECONDARY_COLOUR)
    appNameLabel.grid(row=2)

    appVersionLabel = tk.Label(
        footerFrame, text="Version 1.0.0", foreground=SECONDARY_COLOUR)
    appVersionLabel.grid(row=3)


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for dialogForAppLoginOrRegister")
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

    dialogForAppLoginOrRegister(fields, {"ok": onClickOk, "cancel": lambda event: print(
        'onCancel'), "register": lambda event: print('onRegister')}, mainFrame)

    mainFrame.mainloop()

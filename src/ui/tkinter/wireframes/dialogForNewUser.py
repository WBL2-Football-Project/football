from StateMachine import State
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from .constants import *
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


def dialogForNewUser(fieldsObj, actions: Dict[str, Callable], parentFrame=None):
    """Create dialog window for input fields:
        - login
        - password
    """
    global stringVars

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
    onOKButton = tk.Button(buttonsFrame, text='Register', width=20,
                           background=PRIMARY_COLOUR, foreground="#FFFFFF", font=(FONT, 10))
    onOKButton.grid(row=0, column=0, ipadx=2, ipady=2)
    if 'ok' in actions:
        onOKButton.bind("<Button-1>", lambda event: actions['ok'](
            {"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20,
                               background=SECONDARY_COLOUR, foreground="#FFFFFF", font=(FONT, 10))
    onCancelButton.grid(row=0, column=1, padx=15, ipady=2, ipadx=2)
    onCancelButton.bind("<Button-1>", lambda event: actions['cancel']())


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

    dialogForNewUser(fields, {"ok": onClickOk}, mainFrame)

    mainFrame.mainloop()

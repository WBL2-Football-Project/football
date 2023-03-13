from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
#from model import *
import tkinter as tk
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')))

print(os.getcwd(),os.path.abspath(os.path.join(os.path.dirname(__file__), 'src', 'model')))

from StateMachine import State

tkVars = {}  # helper variable

# Exported dialog procedure:


def dialogForNewUser(fieldsObj, actions:Dict[str,Callable], parentFrame=None):
    """Create dialog window for input fields:
        - login
        - password
    """
    global stringVars

    global tkVars
    tkVars["login"] = tk.StringVar(parentFrame, fieldsObj.login)
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)

    usernameLabel = tk.Label(parentFrame, text="Username", font=('Helvetica', 10)).grid(row=0, pady=(10, 5))
    username = tk.Entry(parentFrame, width=40, textvariable=tkVars["login"]).grid(ipady=5, row=1)

    passwordLabel = tk.Label(parentFrame, text="Password", font=('Helvetica', 10)).grid(row=2, pady=(10, 5))
    password = tk.Entry(parentFrame, width=40,textvariable=tkVars["password"]).grid(ipady=5, row=3)

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    
    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=20)
    onOKButton.grid(row=0, column=0)
    if 'ok' in actions:
        onOKButton.bind("<Button-1>", lambda event: actions['ok']({"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
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

    dialogForNewUser(fields,{"ok":onClickOk},mainFrame)

    mainFrame.mainloop()

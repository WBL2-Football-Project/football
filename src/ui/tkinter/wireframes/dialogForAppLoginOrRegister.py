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
def dialogForAppLoginOrRegister(fieldsObj, actions:Dict[str,Callable], parentFrame:Any=None):
    """Create dialog window for input fields:
        - login
        - password
    """
    global tkVars
    tkVars["login"] = tk.StringVar(parentFrame, fieldsObj.login)
    tkVars["password"] = tk.StringVar(parentFrame, fieldsObj.password)

    # parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    usernameLabel = tk.Label(parentFrame, text="Username", font=('Helvetica', 10)).grid(row=0, pady=(10, 5), columnspan=3, sticky='ew')
    username = tk.Entry(parentFrame, width=40, textvariable=tkVars["login"]).grid(ipady=5, row=1,columnspan=3, sticky='ew')

    passwordLabel = tk.Label(parentFrame, text="Password", font=('Helvetica', 10)).grid(row=2, pady=(10, 5), columnspan=3, sticky='ew')
    password = tk.Entry(parentFrame, width=40, textvariable=tkVars["password"]).grid(ipady=5, row=3, columnspan=3, sticky='ew')

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK')
    onOKButton.grid(row=0, column=2, padx=15, sticky='e')
    if 'ok' in actions:
        onOKButton.bind("<Button-1>", lambda event: actions['ok']({"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    # Register Button
    onRegisterButton = tk.Button(buttonsFrame, text='Register')
    onRegisterButton.grid(row=0, column=1, padx=15, sticky='ew')
    if 'register' in actions:
        onRegisterButton.bind("<Button-1>", lambda event: actions['register']({"login": tkVars["login"].get(), "password": tkVars["password"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel')
    onCancelButton.grid(row=0, column=0, padx=15, sticky='w')
    if 'cancel' in actions:
    	onCancelButton.bind("<Button-1>", lambda event: actions['cancel']()) # old: onCancelButton.bind("<Button-1>", lambda event: newUserFrame.destroy())

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

    dialogForAppLoginOrRegister(fields,{"ok":onClickOk, "cancel":lambda event: print('onCancel'), "register":lambda event: print('onRegister')},mainFrame)

    mainFrame.mainloop()

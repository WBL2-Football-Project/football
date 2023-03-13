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


# Exported dialog procedure:
def dialogForNewTeam(data, actions:Dict[str,Callable], parentFrame):
    """Create dialog window for input fields:
        - teamID
        - name
    """

    tkVars={}
    tkVars["teamID"] = tk.StringVar(parentFrame, data.teamID)
    tkVars["name"] = tk.StringVar(parentFrame, data.name)

    tk.Label(parentFrame, text="Team ID", font=('Helvetica', 10)).grid(row=1)
    tk.Spinbox(parentFrame, from_=0, to_=10000, textvariable=tkVars["teamID"], width=10).grid(row=2, ipady=5)

    tk.Label(parentFrame, text="Team Name", font=('Helvetica', 10)).grid(row=3, pady=(10, 5))
    tk.Entry(parentFrame, width=40, textvariable=tkVars["name"]).grid(ipady=5, row=4)

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=20)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind("<Button-1>", lambda event: actions['ok']({"teamID": tkVars["teamID"].get(), "name": tkVars["name"].get()}))

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
            self.teamID = ""
            self.name = ""
    fields = Fields()

    def onClickOk(*vars):
        print("Returned:", vars)

    actions={'ok':onClickOk, 'cancel':exit(0)}
    
    dialogForNewTeam(fields, actions, mainFrame)

    mainFrame.mainloop()

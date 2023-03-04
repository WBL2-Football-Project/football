from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
#from model import *
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


def dialogForEditTeam(fieldsObj, onClickOk, parentFrame):
    """Create dialog window for input fields:
        - name
    """
    global tkVars
    tkVars["name"] = tk.StringVar(parentFrame, fieldsObj.name)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    teamNameLabel = tk.Label(
        parentFrame, text="Team Name", font=('Helvetica', 10)).grid(row=3, pady=(10, 5))

    teamName = tk.Entry(parentFrame, width=40, textvariable=tkVars["name"])
    teamName.grid(ipady=5, row=4)

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=20)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind(
        "<Button-1>", lambda event: onClickOk({"name": tkVars["name"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: parentFrame.destroy())


if __name__ == "__main__":
    mainFrame = tk.Tk()
    mainFrame.title("Dialog")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.name = ""
    fields = Fields()

    def onClickOk(*name):
        print("name", name)

    dialogForEditTeam(fields, onClickOk, mainFrame)

    mainFrame.mainloop()

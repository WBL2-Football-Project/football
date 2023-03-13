from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
from constants import *
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


def dialogForEditTeam(data, actions, parentFrame, tkVars: Dict):
    """Create dialog window for input fields:
        - name
    """
    tkVars["name"] = tk.StringVar(parentFrame, data["name"])

    tk.Label(parentFrame, text="Team Name", font=(
        FONT, 10)).grid(row=3, pady=(10, 5))
    tk.Entry(parentFrame, width=40,
             textvariable=tkVars["name"], font=(FONT, 10)).grid(ipady=5, row=4)


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

    tkVars = {}
    dialogForEditTeam(fields, onClickOk, mainFrame, tkVars)

    mainFrame.mainloop()

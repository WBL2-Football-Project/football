import os
import sys
from typing import Optional,List,Any,Callable,Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from model import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import simpledialog
from tkinter import messagebox

tkVars={} # helper variable

# Exported dialog procedure:
def dialogForEditPlay(fieldsObj,onClickOk,parentFrame):
    """Create dialog window for input fields:
        - team1GoalsScored (int)
        - team2GoalsScored (int)
        - team1GoalsMissed (int)
        - team2GoalsMissed (int)
        - team1YellowCards (int)
        - team2YellowCards (int)
        - isPlayCompleted (bool)
    """
    global stringVars
    
    global tkVars
    tkVars["team1GoalsScored"]=tk.StringVar(parentFrame,fieldsObj.password)
    tkVars["team2GoalsScored"]=tk.StringVar(parentFrame,fieldsObj.rights)
    tkVars["team1GoalsMissed"]=tk.StringVar(parentFrame,fieldsObj.password)
    tkVars["team2GoalsMissed"]=tk.StringVar(parentFrame,fieldsObj.rights)
    tkVars["team1YellowCards"]=tk.StringVar(parentFrame,fieldsObj.password)
    tkVars["team2YellowCards"]=tk.StringVar(parentFrame,fieldsObj.rights)
    tkVars["isPlayCompleted"]=tk.StringVar(parentFrame,fieldsObj.rights)

    # TODO: widget for login
    # TODO: widget for password
    # TODO: widget for rights

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.login=""
            self.password=""
            self.rights=""
    fields=Fields()
    def onClickOk(*vars):
        print("Returned:",vars)

    dialogForEditPlay(fields,onClickOk,mainFrame)
    onOKButton=tk.Button(mainFrame, text='OK', width=5)
    onOKButton.grid(row=20,column=0,columnspan=2,sticky='w')
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"team1GoalsScored":tkVars["team1GoalsScored"].get(),"team2GoalsScored":tkVars["team2GoalsScored"].get(),"team1GoalsMissed":tkVars["team1GoalsMissed"].get(),"team2GoalsMissed":tkVars["team2GoalsMissed"].get(),"team1YellowCards":tkVars["team1YellowCards"].get(),"team2YellowCards":tkVars["team2YellowCards"].get(),"isPlayCompleted":tkVars["isPlayCompleted"].get()}))

    mainFrame.mainloop()
    

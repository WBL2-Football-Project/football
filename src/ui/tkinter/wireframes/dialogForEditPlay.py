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


# Exported dialog procedure:
def dialogForEditPlay(fieldsObj, actions, parentFrame, tkVars:Dict):
    """Create dialog window for input fields:
        - team1GoalsScored (int)
        - team2GoalsScored (int)
        # - team1GoalsMissed (int)
        # - team2GoalsMissed (int)
        - team1YellowCards (int)
        - team2YellowCards (int)
        - isPlayCompleted (bool)
    """

    tkVars["team1GoalsScored"] = tk.StringVar(
        parentFrame, fieldsObj['team1GoalsScored'])
    tkVars["team2GoalsScored"] = tk.StringVar(
        parentFrame, fieldsObj['team2GoalsScored'])
    # tkVars["team1GoalsMissed"] = tk.StringVar(
    #     parentFrame, fieldsObj['team1GoalsMissed'])
    # tkVars["team2GoalsMissed"] = tk.StringVar(
    #     parentFrame, fieldsObj['team2GoalsMissed'])
    tkVars["team1YellowCards"] = tk.StringVar(
        parentFrame, fieldsObj['team1YellowCards'])
    tkVars["team2YellowCards"] = tk.StringVar(
        parentFrame, fieldsObj['team1YellowCards'])
    tkVars["isPlayCompleted"] = tk.StringVar(
        parentFrame, fieldsObj['isPlayCompleted'])

    # Goals Scored
    goalScoredFrame = tk.Frame(parentFrame)
    goalScoredFrame.grid(row=1, column=0, padx=10)

    tk.Label(goalScoredFrame, text="Goals Scored",
             font=(FONT, 10)).grid(row=0, pady=10)

    tk.Label(goalScoredFrame, text="Team 1").grid(row=1, column=0)
    tk.Spinbox(goalScoredFrame, from_=0, to_=10000,
               textvariable=tkVars["team1GoalsScored"], width=10, font=(FONT, 10)).grid(row=2, column=0, ipady=5)

    tk.Label(goalScoredFrame, text="Team 2",
             font=(FONT, 10)).grid(row=1, column=2)
    tk.Spinbox(goalScoredFrame, from_=0, to_=10000,
               textvariable=tkVars["team2GoalsScored"], width=10, font=(FONT, 10)).grid(row=2, column=2, ipady=5)

    # # Goals Missed
    # goalMissedFrame = tk.Frame(parentFrame)
    # goalMissedFrame.grid(row=1, column=1, padx=10)

    # tk.Label(goalMissedFrame, text="Goals Missed",
    #          font=(FONT, 10)).grid(row=0, pady=10)

    # tk.Label(goalMissedFrame, text="Team 1",
    #          font=(FONT, 10)).grid(row=1, column=0)
    # tk.Spinbox(goalMissedFrame, from_=0, to_=10000,
    #            textvariable=tkVars["team1GoalsMissed"], width=10, font=(FONT, 10)).grid(row=2, column=0, ipady=5)

    # tk.Label(goalMissedFrame, text="Team 2",
    #          font=(FONT, 10)).grid(row=1, column=2)
    # tk.Spinbox(goalMissedFrame, from_=0, to_=10000,
    #            textvariable=tkVars["team2GoalsMissed"], width=10, font=(FONT, 10)).grid(row=2, column=2, ipady=5)

    # Yellow Cards
    yellowCardsFrame = tk.Frame(parentFrame)
    yellowCardsFrame.grid(row=1, column=1, padx=10)

    tk.Label(yellowCardsFrame, text="Yellow Cards",
             font=(FONT, 10)).grid(row=0, pady=10)

    tk.Label(yellowCardsFrame, text="Team 1",
             font=(FONT, 10)).grid(row=1, column=0)
    tk.Spinbox(yellowCardsFrame, from_=0, to_=10000,
               textvariable=tkVars["team1YellowCards"], width=10, font=(FONT, 10)).grid(row=2, column=0, ipady=5)

    tk.Label(yellowCardsFrame, text="Team 2",
             font=(FONT, 10)).grid(row=1, column=2)
    tk.Spinbox(yellowCardsFrame, from_=0, to_=10000,
               textvariable=tkVars["team2YellowCards"], width=10, font=(FONT, 10)).grid(row=2, column=2, ipady=5)

    # Play Completed
    radioButtonsFrame = tk.Frame(parentFrame)
    radioButtonsFrame.grid(row=2, column=1, padx=10)

    tk.Label(radioButtonsFrame, text="Is Completed",
             font=(FONT, 10)).grid(row=0, pady=10)

    tk.Radiobutton(radioButtonsFrame, text="Yes",
                   variable=tkVars["isPlayCompleted"], value='Yes', font=(FONT, 10)).grid(row=1, column=0)
    tk.Radiobutton(radioButtonsFrame, text="No",
                   variable=tkVars["isPlayCompleted"], value='No', font=(FONT, 10)).grid(row=1, column=1)

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=3, pady=25, column=0)

    # # OK BUTTON
    # onOKButton = tk.Button(buttonsFrame, text='Save', width=10)
    # onOKButton.grid(row=0, column=1, sticky='w')
    # onOKButton.bind("<Button-1>", lambda event: actions['ok']({"team1GoalsScored": tkVars["team1GoalsScored"].get(), "team2GoalsScored": tkVars["team2GoalsScored"].get(), "team1GoalsMissed": tkVars["team1GoalsMissed"].get(
    # ), "team2GoalsMissed": tkVars["team2GoalsMissed"].get(), "team1YellowCards": tkVars["team1YellowCards"].get(), "team2YellowCards": tkVars["team2YellowCards"].get(), "isPlayCompleted": tkVars["isPlayCompleted"].get()}))

    # # Cancel Button
    # onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=10)
    # onCancelButton.grid(row=0, column=0, padx=15, sticky='w')
    # onCancelButton.bind(
    #     "<Button-1>", lambda event: actions['cancel']())


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

    dialogForEditPlay(fields, onClickOk, mainFrame)

    mainFrame.mainloop()

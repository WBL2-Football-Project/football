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

# Exported dialog procedure:


def dialogForEditPlay(fieldsObj, onClickOk, parentFrame):
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
    tkVars["team1GoalsScored"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["team2GoalsScored"] = tk.StringVar(parentFrame, fieldsObj.rights)
    tkVars["team1GoalsMissed"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["team2GoalsMissed"] = tk.StringVar(parentFrame, fieldsObj.rights)
    tkVars["team1YellowCards"] = tk.StringVar(parentFrame, fieldsObj.password)
    tkVars["team2YellowCards"] = tk.StringVar(parentFrame, fieldsObj.rights)
    tkVars["isPlayCompleted"] = tk.StringVar(parentFrame, fieldsObj.rights)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    editPlayFrame = tk.Frame(parentFrame)
    editPlayFrame.grid(sticky="nsew")


# Goals Scored
    goalScoredFrame = tk.Frame(editPlayFrame)
    goalScoredFrame.grid(row=1, column=0)

    goalScoredLabel = tk.Label(
        goalScoredFrame, text="Goals Scored", font=('Helvetica', 10))
    goalScoredLabel.grid(row=0, pady=10)

    team1label = tk.Label(goalScoredFrame, text="Team 1").grid(row=1, column=0)
    team1Goals = tk.Spinbox(goalScoredFrame, from_=0, to_=10000,
                            textvariable=tkVars["team1GoalsScored"], width=10)
    team1Goals.grid(row=2, column=0, ipady=5)

    team2label = tk.Label(goalScoredFrame, text="Team 2").grid(row=1, column=2)
    team2Goals = tk.Spinbox(goalScoredFrame, from_=0, to_=10000,
                            textvariable=tkVars["team2GoalsScored"], width=10)
    team2Goals.grid(row=2, column=2, ipady=5)

# Goals Missed
    goalMissedFrame = tk.Frame(editPlayFrame)
    goalMissedFrame.grid(row=1, column=1)

    goalMissedLabel = tk.Label(
        goalMissedFrame, text="Goals Missed", font=('Helvetica', 10))
    goalMissedLabel.grid(row=0, pady=10)

    team1label = tk.Label(goalMissedFrame, text="Team 1").grid(row=1, column=0)
    team1GoalsMissed = tk.Spinbox(goalMissedFrame, from_=0, to_=10000,
                                  textvariable=tkVars["team1GoalsMissed"], width=10)
    team1GoalsMissed.grid(row=2, column=0, ipady=5)

    team2label = tk.Label(goalMissedFrame, text="Team 2").grid(row=1, column=2)
    team2GoalsMissed = tk.Spinbox(goalMissedFrame, from_=0, to_=10000,
                                  textvariable=tkVars["team2GoalsMissed"], width=10)
    team2GoalsMissed.grid(row=2, column=2, ipady=5)

# Yellow Cards
    yellowCardsFrame = tk.Frame(editPlayFrame)
    yellowCardsFrame.grid(row=2, column=0)

    yellowCardsLabel = tk.Label(
        yellowCardsFrame, text="Yellow Cards", font=('Helvetica', 10))
    yellowCardsLabel.grid(row=0, pady=10)

    team1label = tk.Label(
        yellowCardsFrame, text="Team 1").grid(row=1, column=0)
    team1YellowCards = tk.Spinbox(yellowCardsFrame, from_=0, to_=10000,
                                  textvariable=tkVars["team1YellowCards"], width=10)
    team1YellowCards.grid(row=2, column=0, ipady=5)

    team2label = tk.Label(
        yellowCardsFrame, text="Team 2").grid(row=1, column=2)
    team2YellowCards = tk.Spinbox(yellowCardsFrame, from_=0, to_=10000,
                                  textvariable=tkVars["team2YellowCards"], width=10)
    team2YellowCards.grid(row=2, column=2, ipady=5)

# Play Completed
    radioButtonsFrame = tk.Frame(editPlayFrame)
    radioButtonsFrame.grid(row=2, column=1)

    isCompletedLabel = tk.Label(radioButtonsFrame, text="Is Completed")
    isCompletedLabel.grid(row=0, pady=10)

    yesRadioButtton = tk.Radiobutton(radioButtonsFrame, text="Yes",
                                     variable=tkVars["isPlayCompleted"], value='Yes').grid(row=1, column=0)

    noRadioButton = tk.Radiobutton(radioButtonsFrame, text="No",
                                   variable=tkVars["isPlayCompleted"], value='No').grid(row=1, column=1)

    buttonsFrame = tk.Frame(editPlayFrame)
    buttonsFrame.grid(row=3, pady=25, column=0)
    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='Save', width=10)
    onOKButton.grid(row=0, column=1, sticky='w')
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"team1GoalsScored": tkVars["team1GoalsScored"].get(), "team2GoalsScored": tkVars["team2GoalsScored"].get(), "team1GoalsMissed": tkVars["team1GoalsMissed"].get(
    ), "team2GoalsMissed": tkVars["team2GoalsMissed"].get(), "team1YellowCards": tkVars["team1YellowCards"].get(), "team2YellowCards": tkVars["team2YellowCards"].get(), "isPlayCompleted": tkVars["isPlayCompleted"].get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=10)
    onCancelButton.grid(row=0, column=0, padx=15, sticky='w')
    onCancelButton.bind(
        "<Button-1>", lambda event: editPlayFrame.destroy())


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

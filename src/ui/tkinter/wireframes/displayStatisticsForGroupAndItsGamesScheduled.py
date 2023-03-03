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

# Exported dialog procedure:
def displayStatisticsForGroupAndItsGamesScheduled(dataStruct:List[GroupWithGamesScheduled],parentFrame):
    """
        Creates the statistics window showing the list of every group content, including schedules for games.
            
        GroupWithGamesSchedules object fields:
            groupID (int)=0 : the group ID
            groupName (str)="" : the group name
            team1PlayCounter (int)=0 : the amount of plays completed for team 1
            team2PlayCounter (int)=0 : the amount of plays completed for team 2
            team3PlayCounter (int)=0 : the amount of plays completed for team 3
            team1Score (int)=0 : the team 1 score
            team2Score (int)=0 : the team 2 score
            team3Score (int)=0 : the team 3 score
            team1ID (int) : the team 1 ID
            team2ID (str) : the team 2 ID
            team3ID (int) : the team 3 ID
            team1GoalsScored (int)=0 : the team 1 goals scored
            team2GoalsScored (int)=0 : the team 2 goals scored
            team3GoalsScored (int)=0 : the team 3 goals scored
            team1GoalsMissed (int)=0 : the team 1 goals missed
            team2GoalsMissed (int)=0 : the team 2 goals missed
            team3GoalsMissed (int)=0 : the team 3 goals missed
            team1YellowCards (int)=0 : the team 1 yellow cards
            team2YellowCards (int)=0 : the team 2 yellow cards
            team3YellowCards (int)=0 : the team 3 yellow cards
            isGroupCompleted (bool)=false : true if all the games in this group was already completed
            scheduleList (List[Schedule]) : the schedule list containing the coresponding Play record data

    """


    # TODO: create the dialog

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    group_with_games_scheduled_list:List[GroupWithGamesScheduled]=[] # to get if from system constroller OR greate objects GroupWithGamesScheduled manually
    displayStatisticsForGroupAndItsGamesScheduled(group_with_games_scheduled_list,mainFrame)

    mainFrame.mainloop()

from GroupWithGamesScheduled import GroupWithGamesScheduled, PlayWithSchedule
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
# from model import *
from constants import *
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
def displayStatisticsForGroupAndItsGamesScheduled(dataStruct: List[GroupWithGamesScheduled], actions: Dict[str, Callable], parentFrame):
    """
        Creates the statistics window showing the list of every group content, including schedules for games.

        GroupWithGamesSchedules object fields:
            groupID (int)=0 : the group ID
            groupName (str)="" : the group name
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
            play1 (PlayWithSchedule) : the play1 record extended by 'schedule' field containing the schedule data
            play2 (PlayWithSchedule) : the play2 record extended by 'schedule' field containing the schedule data
            play3 (PlayWithSchedule) : the play3 record extended by 'schedule' field containing the schedule data

    """
    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    groupStageFrame = tk.Frame(parentFrame)
    groupStageFrame.grid()

    legendLabel = tk.Label(
        groupStageFrame, text="GS - Goals Scored\t\tGM - Goals Missed\nYC - Yellow Cards\t\tP - Points")
    legendLabel.grid(row=0, padx=10, pady=10)

    col: int = 0
    row: int = 1

    for idx, group in enumerate(dataStruct):
        groupFrame = tk.Frame(groupStageFrame)
        groupFrame.grid(row=row, column=col, pady=10, padx=10)

        col += 1
        if col > 1:
            col = 0
            row += 1

        groupLabel = tk.Label(groupFrame, text=f"Group {idx+1}")
        groupLabel.grid(row=0)

        groupTable = ttk.Treeview(
            groupFrame, columns="c1, c2, c3, c4", height=5)

        groupTable.heading('#0', text='Team')  # Team ID
        groupTable.heading('#1', text='GS')  # Goals Scored
        groupTable.heading('#2', text='GM')  # Goals Missed
        groupTable.heading('#3', text='YC')  # Yellow Cards
        groupTable.heading('#4', text='P')  # Points
        groupTable.column('#0', width=50, anchor=tk.CENTER)
        groupTable.column('#1', width=50, anchor=tk.CENTER)
        groupTable.column('#2', width=50, anchor=tk.CENTER)
        groupTable.column('#3', width=50, anchor=tk.CENTER)
        groupTable.column('#4', width=50, anchor=tk.CENTER)

        groupTable.grid(row=1)

        groupTable.insert('', 'end', text=group.team1ID,
                          values=(group.team1GoalsScored,
                                  group.team1GoalsMissed, group.team1YellowCards, group.team1Score))  # group.teams1PlayCounter

        groupTable.insert('', 'end', text=group.team2ID,
                          values=(group.team2GoalsScored,
                                  group.team2GoalsMissed, group.team2YellowCards,  group.team2Score))  # group.teams2PlayCounter

        groupTable.insert('', 'end', text=group.team3ID,
                          values=(group.team3GoalsScored,
                                  group.team3GoalsMissed, group.team3YellowCards, group.team3Score))  # group.teams3PlayCounter

    buttonsFrame = tk.Frame(groupStageFrame)
    buttonsFrame.grid(row=20, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # Cancel Button
    onCancelButton = tk.Button(
        buttonsFrame, text='Close', width=20, background=SECONDARY_COLOUR, font=(FONT, 10), foreground='#FFFFFF')
    onCancelButton.grid(row=0, column=1, padx=15,
                        ipadx=2, ipady=2, columnspan=5)
    onCancelButton.bind(
        "<Button-1>", lambda event: actions['cancel']())


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

# Classes for Testing UI
    class Group:
        """Class representing every single group in group phase of tournament"""

        def __init__(self):
            self.groupID: int = 0
            self.groupName: str = ""
            self.team1ID: int = 0
            self.team2ID: int = 0
            self.team3ID: int = 0
            self.teams1PlayCounter: int = 0
            self.teams2PlayCounter: int = 0
            self.teams3PlayCounter: int = 0
            self.team1Score: int = 0
            self.team2Score: int = 0
            self.team3Score: int = 0
            self.team1GoalsScored: int = 0
            self.team2GoalsScored: int = 0
            self.team3GoalsScored: int = 0
            self.team1GoalsMissed: int = 0
            self.team2GoalsMissed: int = 0
            self.team3GoalsMissed: int = 0
            self.team1YellowCards: int = 0
            self.team2YellowCards: int = 0
            self.team3YellowCards: int = 0

    class GroupWithGamesScheduled(Group):
        """A group structure extended by list of related games scheduled objects including the play records for each schedule."""

        def __init__(self, group):

            self.groupID: int = group.groupID
            self.groupName: str = group.groupName
            self.team1ID: int = group.team1ID
            self.team2ID: int = group.team2ID
            self.team3ID: int = group.team3ID
            self.teams1PlayCounter: int = group.teams1PlayCounter
            self.teams2PlayCounter: int = group.teams2PlayCounter
            self.teams3PlayCounter: int = group.teams3PlayCounter
            self.team1Score: int = group.team1Score
            self.team2Score: int = group.team2Score
            self.team3Score: int = group.team3Score
            self.team1GoalsScored: int = group.team1GoalsScored
            self.team2GoalsScored: int = group.team2GoalsScored
            self.team3GoalsScored: int = group.team3GoalsScored
            self.team1GoalsMissed: int = group.team1GoalsMissed
            self.team2GoalsMissed: int = group.team2GoalsMissed
            self.team3GoalsMissed: int = group.team3GoalsMissed
            self.team1YellowCards: int = group.team1YellowCards
            self.team2YellowCards: int = group.team2YellowCards
            self.team3YellowCards: int = group.team3YellowCards

# Classes for Testing UI

    group1 = Group()
    group1.team1ID = 1
    group1.team2ID = 2
    group1.team3ID = 3

    group2 = Group()
    group3 = Group()
    group4 = Group()
    group5 = Group()

    testData1 = GroupWithGamesScheduled(group1)
    testData2 = GroupWithGamesScheduled(group2)
    testData3 = GroupWithGamesScheduled(group3)
    testData4 = GroupWithGamesScheduled(group4)
    testData5 = GroupWithGamesScheduled(group5)

    # to get if from system constroller OR greate objects GroupWithGamesScheduled manually
    group_with_games_scheduled_list: List = [
        testData1, testData2, testData3, testData4]
    displayStatisticsForGroupAndItsGamesScheduled(
        group_with_games_scheduled_list, mainFrame)

    mainFrame.mainloop()

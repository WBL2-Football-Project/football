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
def displayStatisticsForPlayoffScheduledGames(dataStruct:List[SchedulesWithPlay],parentFrame):
    """
        Creates the statistics window showing the list of every group content, including schedules for games.
            
        SchedulesWithPlay object fields:
			scheduleID (int) : schedule ID
			playID (int) : corresponding play object ID
			play (int) : corresponding play object full data
			date (datetime) : scheduled date
			timeOfDay (TimeOfDay) : time of the day whene the game is scheduled
			isPlayCompleted (bool) : True means the game is completed, False - we don't have results yet
			isGroupPhase (bool) : True means this game is for group phase of tournament, False - playoff phase of tournament

    """
    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    playOffFrame = tk.Frame(parentFrame)
    playOffFrame.grid()

    scheduleFrame = tk.Frame(playOffFrame)
    scheduleFrame.grid(row=0)

    for idx, game in enumerate(dataStruct):
        gameFrame = tk.Frame(scheduleFrame)
        gameFrame.grid()

    buttonsFrame = tk.Frame(playOffFrame)
    buttonsFrame.grid(row=20, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")


    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Close', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: playOffFrame.destroy())

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    group_with_games_scheduled_list:List[SchedulesWithPlay]=[] # to get if from system constroller OR greate objects SchedulesWithPlay manually
    displayStatisticsForPlayoffScheduledGames(group_with_games_scheduled_list,mainFrame)

    mainFrame.mainloop()

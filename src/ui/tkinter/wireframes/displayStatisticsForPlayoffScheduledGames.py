from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))
from model import *
from datetime import datetime
from typing import Optional, List, Any, Callable, Dict
import inspect
from SchedulesWithPlay import SchedulesWithPlay
from Play import Play
from Teams import Teams

# Exported dialog procedure:

def displayStatisticsForPlayoffScheduledGames(dataStruct:List[SchedulesWithPlay], actions:Dict[str,Callable], parentFrame):
    """
        Creates the statistics window showing the list of every group content, including schedules for games.
        SchedulesWithPlay object fields follow SchedulesWithPlay class definition:

			scheduleID (int) : schedule ID
			playID (int) : corresponding play object ID
			play (int) : corresponding play object full data
			date (datetime) : scheduled date
			timeOfDay (TimeOfDay) : time of the day whene the game is scheduled
			isPlayCompleted (bool) : True means the game is completed, False - we don't have results yet
			isGroupPhase (bool) : True means this game is for group phase of tournament, False - playoff phase of tournament
			team1 (Teams) : team full data
			team2 (Teams) : team full data

    """
    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    playOffFrame = tk.Frame(parentFrame)
    playOffFrame.grid(row=2)

    groupStageFrame = tk.Frame(playOffFrame)
    groupStageFrame.grid(row=0)
    groupStageFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    groupStageLabel = tk.Label(groupStageFrame, text="Group Stage")
    groupStageLabel.grid(row=0, pady=(10, 0), column=0)

    playOffStageFrame = tk.Frame(playOffFrame)
    playOffStageFrame.grid(row=2, column=0)
    playOffStageFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    playOffStageLabel = tk.Label(playOffStageFrame, text="Play-Offs")
    playOffStageLabel.grid(row=0)

    knockoutRoundFrame = tk.Frame(playOffStageFrame)
    knockoutRoundFrame.grid(row=2)
    knockoutLabel = tk.Label(knockoutRoundFrame, text="Knock-out")
    knockoutLabel.grid(row=0)

    quaterFinalFrame = tk.Frame(playOffStageFrame)
    quaterFinalFrame.grid(row=3)
    quaterFinalLabel = tk.Label(quaterFinalFrame, text="Quater-Finals")
    quaterFinalLabel.grid(row=0)

    semiFinalFrame = tk.Frame(playOffStageFrame)
    semiFinalFrame.grid(row=4)
    semiFinalLabel = tk.Label(semiFinalFrame, text="Semi-Finals")
    semiFinalLabel.grid(row=0)

    _3rdPlaceFrame = tk.Frame(playOffStageFrame)
    _3rdPlaceFrame.grid(row=5)
    _3rdPlaceLabel = tk.Label(_3rdPlaceFrame, text="3rd Place Final")
    _3rdPlaceLabel.grid(row=0)

    FinalFrame = tk.Frame(playOffStageFrame)
    FinalFrame.grid(row=6)
    FinalLabel = tk.Label(FinalFrame, text="Finals")
    FinalLabel.grid(row=0)

    groupCol: int = 0
    groupRow: int = 1

    knockoutCol: int = 0
    knockoutRow: int = 1

    quaterCol: int = 0
    quaterRow: int = 1

    semiCol: int = 0
    semiRow: int = 1

    finalCol: int = 0
    finalRow: int = 1

    for idx, game in enumerate(dataStruct):
        # if game.isGroupPhase:
        #     playFrame = tk.Frame(
        #         groupStageFrame, borderwidth=2, relief="groove")
        #     playFrame.grid(row=groupRow, column=groupCol, padx=10, pady=10)

        #     team1 = tk.Label(
        #         playFrame, text=f"{game.play.team1Name} - {game.play.team1GoalsScored}")
        #     team1.grid(row=0)

        #     team2 = tk.Label(
        #         playFrame, text=f"{game.play.team2Name} - {game.play.team2GoalsScored}")
        #     team2.grid(row=1)

        #     groupCol += 1
        #     if groupCol > 3:
        #         groupCol = 0
        #         groupRow += 1
        # else:
        if not game.isGroupPhase:
            # match game.play.is round:
            #     case "Knockout":
            #         frame = knockoutRoundFrame
            #         playFrame = tk.Frame(
            #             frame, borderwidth=2, relief="groove")
            #         playFrame.grid(
            #             row=knockoutRow, column=knockoutCol, padx=10, pady=10)

            #         team1 = tk.Label(
            #             playFrame, text=f"{game.play.team1Name} - {game.play.team1GoalsScored}")
            #         team1.grid(row=0)

            #         team2 = tk.Label(
            #             playFrame, text=f"{game.play.team2Name} - {game.play.team2GoalsScored}")
            #         team2.grid(row=1)

            #         knockoutCol += 1
            #         if knockoutCol > 3:
            #             knockoutCol = 0
            #             knockoutRow += 1

                # case "QuaterFinal":
                #     frame = quaterFinalFrame
                #     playFrame = tk.Frame(
                #         frame, borderwidth=2, relief="groove")
                #     playFrame.grid(
                #         row=quaterRow, column=quaterCol, padx=10, pady=10)

                #     team1 = tk.Label(
                #         playFrame, text=f"{game.play.team1Name} - {game.play.team1GoalsScored}")
                #     team1.grid(row=0)

                #     team2 = tk.Label(
                #         playFrame, text=f"{game.play.team2Name} - {game.play.team2GoalsScored}")
                #     team2.grid(row=1)

                #     quaterCol += 1
                #     if quaterCol > 3:
                #         quaterCol = 0
                #         quaterRow += 1

            if game.play.isQuarterFinal:
                frame = quaterFinalFrame
                playFrame = tk.Frame(frame, borderwidth=2, relief="groove")
                playFrame.grid(row=quaterRow, column=quaterCol, padx=10, pady=10)

                team1 = tk.Label(playFrame, text=f"{game.team1.name} - {game.play.team1GoalsScored}")
                team1.grid(row=0)

                team2 = tk.Label(playFrame, text=f"{game.team2.name} - {game.play.team2GoalsScored}")
                team2.grid(row=1)

                quaterCol += 1
                if quaterCol > 3:
                    quaterCol = 0
                    quaterRow += 1

                # case "SemiFinal":
                #     frame = semiFinalFrame
                #     playFrame = tk.Frame(
                #         frame, borderwidth=2, relief="groove")
                #     playFrame.grid(
                #         row=semiRow, column=semiCol, padx=10, pady=10)

                #     team1 = tk.Label(
                #         playFrame, text=f"{game.play.team1Name} - {game.play.team1GoalsScored}")
                #     team1.grid(row=0)

                #     team2 = tk.Label(
                #         playFrame, text=f"{game.play.team2Name} - {game.play.team2GoalsScored}")
                #     team2.grid(row=1)

                #     semiCol += 1
                #     if semiCol > 3:
                #         semiCol = 0
                #         semiRow += 1

            if game.play.isSemiFinal:
                frame = semiFinalFrame
                playFrame = tk.Frame(frame, borderwidth=2, relief="groove")
                playFrame.grid(row=semiRow, column=semiCol, padx=10, pady=10)

                team1 = tk.Label(playFrame, text=f"{game.team1.name} - {game.play.team1GoalsScored}")
                team1.grid(row=0)

                team2 = tk.Label(playFrame, text=f"{game.team2.name} - {game.play.team2GoalsScored}")
                team2.grid(row=1)

                semiCol += 1
                if semiCol > 3:
                    semiCol = 0
                    semiRow += 1


                # case "Final":
                #     frame = FinalFrame
                #     playFrame = tk.Frame(
                #         frame, borderwidth=2, relief="groove")
                #     playFrame.grid(
                #         row=finalRow, column=finalCol, padx=10, pady=10)

                #     team1 = tk.Label(
                #         playFrame, text=f"{game.play.team1Name} - {game.play.team1GoalsScored}")
                #     team1.grid(row=0)

                #     team2 = tk.Label(
                #         playFrame, text=f"{game.play.team2Name} - {game.play.team2GoalsScored}")
                #     team2.grid(row=1)

                #     finalCol += 1
                #     if finalCol > 3:
                #         finalCol = 0
                #         finalRow += 1
            if game.play.is3rdPlaceFinal:
                frame = _3rdPlaceFrame
                playFrame = tk.Frame(frame, borderwidth=2, relief="groove")
                playFrame.grid(row=finalRow, column=finalCol, padx=10, pady=10)

                team1 = tk.Label(playFrame, text=f"{game.team1.name} - {game.play.team1GoalsScored}")
                team1.grid(row=0)

                team2 = tk.Label(playFrame, text=f"{game.team2.name} - {game.play.team2GoalsScored}")
                team2.grid(row=1)

                finalCol += 1
                if finalCol > 3:
                    finalCol = 0
                    finalRow += 1

            if game.play.isFinal:
                frame = FinalFrame
                playFrame = tk.Frame(frame, borderwidth=2, relief="groove")
                playFrame.grid(row=finalRow, column=finalCol, padx=10, pady=10)

                team1 = tk.Label(playFrame, text=f"{game.team1.name} - {game.play.team1GoalsScored}")
                team1.grid(row=0)

                team2 = tk.Label(playFrame, text=f"{game.team2.name} - {game.play.team2GoalsScored}")
                team2.grid(row=1)

                finalCol += 1
                if finalCol > 3:
                    finalCol = 0
                    finalRow += 1


    buttonsFrame = tk.Frame(playOffFrame)
    buttonsFrame.grid(row=20, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Close', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: actions['close']())


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    """Fields
            playID (int) : (PK) play record ID
            team1ID (Optional(int)) : (FK|None) team1 record ID (None at the tournament stage we don't know yet know which team to play)
            team2ID (Optional(int)) : (FK|None) team2 record ID (None at the tournament stage we don't know yet know which team to play)
            team1GoalsScored (int) : goals scored by team1 in the game
            team2GoalsScored (int) : goals scored by team2 in the game
            team1GoalsMissed (int) : goals missed by team1 in the game
            team2GoalsMissed (int) : goals missed by team2 in the game
            team1YellowCards (int) : yellow cards played by team1 in the game
            team2YellowCards (int) : yellow cards played by team2 in the game
            isPlayCompleted (bool) : indicates if the play is finished, False - still on
            revelantScheduleIDForTeam1 (int) : after the play is completed, the winner team1ID should be set in the coresponing future schedule ID object
            revelantScheduleIDForTeam2 (int) : after the play is completed, the winner team2ID should be set in the coresponing future schedule ID object
        """

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

    # Testing Purposes
    # class SchedulesWithPlay():
    #     """Schedule object with additional corresponding play object data
    #     """

    #     def __init__(self, scheduleID, playID, play, date, timeOfDay, isPlayCompleted, isGroupPhase, round):
    #         """Fields:
    #                 scheduleID (int) : schedule ID
    #                 playID (int) : corresponding play object ID
    #                 play (int) : corresponding play object full data
    #                 date (datetime) : scheduled date
    #                 timeOfDay (TimeOfDay) : time of the day whene the game is scheduled
    #                 isPlayCompleted (bool) : True means the game is completed, False - we don't have results yet
    #                 isGroupPhase (bool) : True means this game is for group phase of tournament, False - playoff phase of tournament
    #         """
    #         self.scheduleID = scheduleID
    #         self.playID = playID
    #         self.date = date
    #         self.timeOfDay = timeOfDay
    #         self.isPlayCompleted = isPlayCompleted
    #         self.isGroupPhase = isGroupPhase
    #         self.play = play
    #         self.round = round

    # class Play:
    #     def __init__(self, playID, team1ID, team2ID, team1Name, team2Name, team1GoalsScored, team2GoalsScored, team1GoalsMissed, team2GoalsMissed, team1YellowCards, team2YellowCards, isPlayCompleted):
    #         """Fields
    #             playID (int) : (PK) play record ID
    #             team1ID (Optional(int)) : (FK|None) team1 record ID (None at the tournament stage we don't know yet know which team to play)
    #             team2ID (Optional(int)) : (FK|None) team2 record ID (None at the tournament stage we don't know yet know which team to play)
    #             team1GoalsScored (int) : goals scored by team1 in the game
    #             team2GoalsScored (int) : goals scored by team2 in the game
    #             team1GoalsMissed (int) : goals missed by team1 in the game
    #             team2GoalsMissed (int) : goals missed by team2 in the game
    #             team1YellowCards (int) : yellow cards played by team1 in the game
    #             team2YellowCards (int) : yellow cards played by team2 in the game
    #             isPlayCompleted (bool) : indicates if the play is finished, False - still on
    #             revelantScheduleIDForTeam1 (int) : after the play is completed, the winner team1ID should be set in the coresponing future schedule ID object
    #             revelantScheduleIDForTeam2 (int) : after the play is completed, the winner team2ID should be set in the coresponing future schedule ID object
    #         """
    #         self.playID = playID
    #         self.team1ID = team1ID
    #         self.team2ID = team2ID
    #         self.team1Name = team1Name
    #         self.team2Name = team2Name
    #         self.team1GoalsScored = team1GoalsScored
    #         self.team2GoalsScored = team2GoalsScored
    #         self.team1GoalsMissed = team1GoalsMissed
    #         self.team2GoalsMissed = team2GoalsScored
    #         self.team1YellowCards = team1YellowCards
    #         self.team2YellowCards = team2YellowCards
    #         self.isPlayCompleted = isPlayCompleted

    date = datetime.today().strftime('%Y-%m-%d')
    # Testing Purposes

    # playID, team1ID, team2ID, team1Name, team2Name, team1GoalsScored, team2GoalsScored, team1GoalsMissed, team2GoalsMissed, team1YellowCards, team2YellowCards, isPlayCompleted
    game1 = Play(1, 1, 2, 'Manchester City','Manchester United', 5, 7, 0, 4, 0, 2, True)
    game2 = Play(1, 1, 2, 'Rangers','Celtic', 5, 7, 0, 4, 0, 2, True)
    game3 = Play(1, 1, 2, 'Real Madrid','Barcelona', 5, 7, 0, 4, 0, 2, True)
    game4 = Play(1, 1, 2, 'Bayern Munich','Borussia Dortmund', 5, 7, 0, 4, 0, 2, True)
    game5 = Play(1, 1, 2, 'Manchester City','Manchester United', 5, 7, 0, 4, 0, 2, True)
    game6 = Play(1, 1, 2, 'Manchester City','Manchester United', 5, 7, 0, 4, 0, 2, True)
    game7 = Play(1, 1, 2, 'Manchester City','Manchester United', 5, 7, 0, 4, 0, 2, True)
    game8 = Play(1, 1, 2, 'Manchester City','Manchester United', 5, 7, 0, 4, 0, 2, True)


    data1 = SchedulesWithPlay(1, 1, game1, date, 'Afternoon', True, True, None)
    data2 = SchedulesWithPlay(1, 2, game2, date, 'Afternoon', True, True, None)
    data3 = SchedulesWithPlay(1, 3, game3, date, 'Afternoon', True, True, None)
    data4 = SchedulesWithPlay(1, 4, game4, date, 'Afternoon', True, True, None)

    data5 = SchedulesWithPlay(1, 5, game5, date, 'Afternoon', True, False, 'Knockout')
    data6 = SchedulesWithPlay(1, 6, game6, date, 'Afternoon', True, False, 'Knockout')
    data7 = SchedulesWithPlay(1, 7, game7, date, 'Afternoon', True, False, 'QuaterFinal')
    data8 = SchedulesWithPlay(1, 8, game8, date, 'Afternoon', True, False, 'QuaterFinal')

    # to get if from system constroller OR greate objects SchedulesWithPlay manually
    group_with_games_scheduled_list: List[SchedulesWithPlay] = [
        data1, data2, data2, data4, data5, data6, data7, data8]
    displayStatisticsForPlayoffScheduledGames(group_with_games_scheduled_list, mainFrame)

    mainFrame.mainloop()

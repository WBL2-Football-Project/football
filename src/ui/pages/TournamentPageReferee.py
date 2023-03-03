import tkinter as tk
import tkinter.ttk as ttk
from api.Models.Tournament import Tournament
from api.Models.Team import Team
from api.Models.Match import Match
from .Widgets.PopUpModal import PopUpModal
import random
from datetime import datetime


class addNewTeamPopup(PopUpModal):
    def __init__(self, frame):
        super().__init__(frame, "Add New Team")

        label = tk.Label(self, text="Add Team")
        label.grid(row=0, column=1, pady=10, ipady=3, sticky=tk.E)

        self.teamName = tk.Entry(self, width=30)
        self.teamName.grid(row=1, column=1, pady=10,
                           ipady=5, sticky=tk.E)

    def confirmButton(self):
        team = Team(random.randint(0, 10000), self.teamName.get(),
                    self.frame.systemController.CURRENT_TOURNAMENT.tournamentID)

        self.frame.api.addTeam(team)
        self.destroy()


class TournamentPageReferee(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        # Root is reference to the GUI class that instantiated the window and system Controller object
        self.api = root.systemController.api
        self.systemController = root.systemController
        self.pack(fill="both", expand=True)

        headerFrame = tk.Frame(self)
        headerFrame.grid(row=0, pady=(10, 20))

        backButton = tk.Button(
            headerFrame, text="Back", background='#1537E7', foreground='#FFFFFF',
            width=20, command=lambda: self.api.back(self, 'Home'))
        backButton.grid(row=0, column=0, ipady=2,
                        padx=20, pady=10, sticky=tk.E)

        label = tk.Label(
            headerFrame, text=f"{self.systemController.CURRENT_TOURNAMENT.name}", font=('Helvetica', 13))
        label.grid(row=0, ipady=3, sticky=tk.E, column=1)

### TEAMS LIST SECTION  ###
        teamListFrame = tk.Frame(self, width=50, padx=20)
        teamListFrame.grid(row=2, column=0)

        addNewTeamButton = tk.Button(
            teamListFrame, text="Add new Team", foreground='#FFFFFF', background='#1537E7', width=20, command=lambda: addNewTeamPopup(self))
        addNewTeamButton.grid(row=0, column=0, ipady=1, padx=10)
        # TODO: replace this with getTeamList() function
        teams = [Team(1, "Team1", 1), Team(2, "Team2", 1),
                 Team(3, "Team3", 1), Team(4, "Team4", 1)]

        for team in teams:
            teamLabel = tk.Label(
                teamListFrame, text=f"{team.name}", font=('Helvetica', 13))
            teamLabel.grid(column=0, sticky=tk.W, padx=10, pady=5)

### TEAMS LIST SECTION  ###

### CURRENT MATCH SECTION ###

        currentMatchFrame = tk.Frame(self, width=50, padx=20)
        currentMatchFrame.grid(row=2, column=2)

        # TODO: implement getcurrentMatch function
        currentMatch = Match(
            1, teams[0], teams[1], 'Group', datetime.today().strftime('%Y-%m-%d'), 1)

        currentMatchLabel = tk.Label(
            currentMatchFrame, text="Current Match", font=('Helvetica', 13))
        currentMatchLabel.grid(row=0, column=2)

        team1Name = tk.Label(
            currentMatchFrame, text=f"{currentMatch.team1.name}", font=('Helvetica', 15))
        team1Name.grid(row=1, column=1)

        team1Score = tk.Label(
            currentMatchFrame, text=f"{currentMatch.team1Score}", font=('Helvetica', 15))
        team1Score.grid(row=2, column=1)

        team1GoalButton = tk.Button(
            currentMatchFrame, text="Give Goal", foreground='#FFFFFF', background='#1537E7', width=15)
        team1GoalButton.grid(row=3, column=1, ipady=2, padx=5)

        team2Name = tk.Label(
            currentMatchFrame, text=f"{currentMatch.team2.name}", font=('Helvetica', 15))
        team2Name.grid(row=1, column=4)

        team2Score = tk.Label(
            currentMatchFrame, text=f"{currentMatch.team2Score}", font=('Helvetica', 15))
        team2Score.grid(row=2, column=4)

        team2GoalButton = tk.Button(
            currentMatchFrame, text="Give Goal", foreground='#FFFFFF', background='#1537E7', width=15)
        team2GoalButton.grid(row=3, column=4, ipady=2, padx=5)

        stopMatchButton = tk.Button(
            currentMatchFrame, text="Stop Match", foreground='#FFFFFF', background='#1537E7', width=20)
        stopMatchButton.grid(row=4, column=2, ipady=2, pady=7)

# CURRENT MATCH SECTION ###

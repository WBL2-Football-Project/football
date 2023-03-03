import tkinter as tk
import tkinter.ttk as ttk
from api.Models.Tournament import Tournament
from .Widgets.PopUpModal import PopUpModal
import random


class CreateTournamentPopup(PopUpModal):
    def __init__(self, frame):
        super().__init__(frame, "Create Tournament")

        label = tk.Label(self, text="Create Tournament")
        label.grid(row=0, column=1, pady=10, ipady=3, sticky=tk.E)

        self.tournamentName = tk.Entry(self, width=30)
        self.tournamentName.grid(row=1, column=1, pady=10,
                                 ipady=5, sticky=tk.E)

    def confirmButton(self):
        tournament = Tournament(random.randint(0, 10000), self.tournamentName.get(
        ), self.frame.systemController.CURRENT_USER.username)

        self.frame.api.createTournament(tournament)
        self.frame.api.open_tournament(self.frame,  tournament)
        self.destroy()


class HomeScreen(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        # Root is reference to the GUI class that instantiated the window and system Controller object
        self.api = root.systemController.api
        self.systemController = root.systemController

        self.pack(fill="both", expand=True)

        headerFrame = tk.Frame(self)
        headerFrame.grid(row=0, pady=(10, 20))

        createNewTournamentButton = tk.Button(
            headerFrame, text="Create new Tournament", foreground='#FFFFFF', background='#1537E7', width=30, command=lambda: CreateTournamentPopup(self))
        createNewTournamentButton.grid(
            row=0, column=0, ipady=3, padx=20, sticky=tk.E)

        logoutButton = tk.Button(
            headerFrame, text="Logout", foreground='#FFFFFF', background='#E73B15', width=20, command=lambda: self.api.logout(self))
        logoutButton.grid(row=0, column=2, ipady=3, padx=20, sticky=tk.E)

        # label = tk.Label(
        #     self, text=f"{self.systemController.CURRENT_USER.username}")
        # label.grid(row=1, column=1, ipady=3, padx=20)

        # TODO: This will be replaced with get_tournaments()
        listOfTournaments = [Tournament(1, "Tournament 1", "RandomRef"), Tournament(
            2, "Tournament 2", "RandomRef"), Tournament(3, "Tournament 3", "RandomRef")]

        tournamentsFrame = tk.Frame(self)
        tournamentsFrame.grid(row=1)

        label = tk.Label(
            tournamentsFrame, text="Active Tournaments", font=('Helvetica', 13))
        label.grid(row=0, column=0, ipady=3, padx=20)

        for tournament in listOfTournaments:
            tournamnentButton = tk.Button(
                tournamentsFrame, text=f"{tournament.name}", command=lambda tournament=tournament: self.api.open_tournament(self, tournament), width=30)

            tournamnentButton.grid(column=2, ipady=3, padx=20, pady=10)

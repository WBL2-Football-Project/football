from .Models.User import User
import tkinter as tk
from .Models.Tournament import Tournament
from ui.pages.HomeScreen import HomeScreen
from ui.pages.LoginScreen import LoginScreen
from ui.pages.TournamentPageReferee import TournamentPageReferee
from .Models.Match import Match
from .Models.Team import Team


class API:
    def __init__(self):
        pass

    def setSystemController(self, systemController):
        self.systemController = systemController

    def change_page(self, currentPage, newPage):
        currentPage.destroy()
        newPage.pack()

    def login(self, page, user: User):
        """
        Login Method

        Get User from GUI
        Page parameter is used for the change_page() method where we will destory the login page if successful
        Check Username and Password against the database and either login if correct or throw error if not
        If logged in successfully load Homepage and create a neew User object then set ACTIVE_USER to the new user

        """
        self.systemController.CURRENT_USER = user
        self.change_page(page, HomeScreen(self.systemController.GUI_ROOT))

    def logout(self, page):
        self.systemController.CURRENT_USER = None
        self.change_page(page, LoginScreen(self.systemController.GUI_ROOT))

    def back(self, page, newPage):
        if newPage == 'Home':
            self.change_page(page, HomeScreen(self.systemController.GUI_ROOT))

    def open_tournament(self, page, tournament: Tournament):
        """
        Open Tournament Method

        Page parameter is used for the change_page() method where we will destory the home page once tournament page has been loaded
        This will use the change_page() method to open either Referee or User tournament page depending
        on if CURRENT_USER is the referee of the tournament object passed when the function is called
        method will then set CURRENT_TOURNAMENT once its opened the correct page

        """
        self.systemController.CURRENT_TOURNAMENT = tournament
        # TODO: Check if the CURRENT_USER is referee of the tournament and open the correct page
        self.change_page(page, TournamentPageReferee(
            self.systemController.GUI_ROOT))

    def createTournament(self, tournament: Tournament):
        """
        Create Tournament Method

        Get tournament from GUI
        Insert Tournament Object in Database
        If tournament created successfully load Tournament Referee page then set CURRENT_TOURNAMENT to the new tournament

        """
        pass

    def addTeam(self, team: Team):
        """
        Add Team Method

        Insert Team Object in Database
        If inserted successfully load updateTeamList()
        """
        pass

    def createMatch(self, match: Match):
        """
        Create Match Method

        Insert Match Object in Database
        If insert successfull call updateSchedule()
        """
        pass

    def startMatch(self, match: Match):
        """
        Start Match Method

        Update Database by setting the match object to started, use parameter match to compare with objects in database to find correct match
        Then set CURRENT_MATCH to the started match
        If update successful load TournamentPageReferee and started match should be displayed on screen
        """
        pass

    def updateSchedule(self):
        """
        Update Schedule Method

        This method will refresh the Schedule Page UI with the new Data
        """
        pass

    def updateTeamList(self):
        """
        Update Team List Method

        This method will refresh the Team UI with the new Data
        """
        pass

    def getTeamList(self, tournament: Tournament) -> list[Team]:
        """
        Get Team List Method

        This method will get all teams for a specific tournament and return a list of these teams
        """
        pass

    def getCurrentMatch(self, tournament: Tournament):
        """
        Get Current Match Method

        This method will get the current match for a specific tournament, this is the match where started is True
        """
        pass

    def getTournaments(self) -> list[Tournament]:
        """
        Get Tournament List Method

        This method will fetch all tournments from the database and return a list of them to be rendered onto the UI
        """
        pass

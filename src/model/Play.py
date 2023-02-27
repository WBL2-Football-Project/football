from typing import List
from Teams import *
from Schedule import *
from unittest import TestCase

class Play:
    """Manages sinle play between two teams statistic data object."""
    def __init__(self):
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
            virtualTeam1 (int) : indicates virtual ID indicating proper team1 ID at the revelant tournament stage
            virtualTeam2 (int) : indicates virtual ID indicating proper team2 ID at the revelant tournament stage
        """
        self.playID = None
        self.team1ID = None
        self.team2ID = None
        self.team1GoalsScored = None
        self.team2GoalsScored = None
        self.team1GoalsMissed = None
        self.team2GoalsMissed = None
        self.team1YellowCards = None
        self.team2YellowCards = None
        self.isPlayCompleted = None
        self.virtualTeam1 = None
        self.virtualTeam2 = None

    def generateRandomPlaySchedule(self):
        """Generates a random play schedule for entire tournament after is checked if expected amount of teams is defined.
        Method uses helpers: generateRandomTeamsList(), prepareGroupPhaseData(), preparePlayoffPhaseData().
        Call saveRelativeScheculeRecords() when the tournament schedule is calculated.
        Sets StateMachine.setIsScheduled() after full schedule is saved."""
        pass

    def generateRandomTeamsList(self):
        """Generates a randomly sorted list of all teams for further schedule computation."""
        pass

    def prepareGroupPhaseData(self,randomTeamsList:List[Teams]):
        """Generates a breakdown of the teams into 4 groups of 3 teams each.
        """
        pass

    def preparePlayoffPhaseData(self,randomTeamsList:List[Teams],groupsTeamsDistribution:List):
        """Generates a breakdown of the teams for quarter-final (4 plays of 2 teams each), semi-final (2 plays of 2 teams each), 3rdPlace-final (1 play of 2 teams) and final (1 play of 2 teams).
        """
        pass

    def saveRelativeScheduleRecords(self,randomTeamsList:List[Teams],groupsTeamsDistribution:List):
        """Creates full schedule calendar records for each required play of tournament for both group and playoff games.
        The coresponding to every scheduled game Play objects records are saved into the database as well."""
        pass

    def actualiseMatchData(self, playID, team1GoalsScored, team2GoalsScored, team1GoalsMissed, team2GoalsMissed, team1YellowCards, team2YellowCards, isPlayCompleted=False):
        """Actualise the current results of the game (during and after the play is completed)

        Args:
            playID (int): play record ID
            team1GoalsScored (int): team1 goals scored
            team2GoalsScored (int): team2 goals scored
            team1GoalsMissed (int): team1 goals missed
            team2GoalsMissed (int): team2 goals missed
            team1YellowCards (int): team1 yellow cards
            team2YellowCards (int): team2 yellow cards
            isPlayCompleted (bool, optional): is game finished
        """
        pass

    @staticmethod
    def getPlayListForListOfSchedules(listOfRecords:List[Schedule]):
        """Creates windows with view of games statistics for a given list of Schedule records (including Play records)

        Args:
            listOfRecords (List[Schedule]): list of Schedule records containing corresponding Play records
        """
        pass

class PlayTesting(TestCase):
    def test_surface(self):
        pass

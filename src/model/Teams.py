from Serialisable import Serialisable

class Teams(Serialisable):
    """Manages the teams data structure."""
    def __init__(self):
        """Fields

            teamID (int): (PM) The team ID
            name (str): The team name
            totalGoalsScored (int): (calculated) The total goals scored by the team during tournament
            totalGoalsMissed (int): (calculated) The total goals misses by the team during tournament
            totalYellowCards (int): (calculated) The total yellow cards played by the team during tournament
            totalPoints (int): (calculated) The total points played by the team during tournament
        """
        Serialisable.__init__(self,self.__class__,["teamID","name","totalGoalsScored","totalGoalsMissed","totalYellowCards","totalPoints"])
        self.teamID = None
        self.name = None
        self.totalGoalsScored = 0
        self.totalGoalsMissed = 0
        self.totalYellowCards = 0
        self.totalPoints = 0

    def checkData(self,name):
        """Check if the edited name of the team is correct and can be saved to the database.
        Returns True if data is correct and False otherwise.
        """
        pass

    @staticmethod
    def getNewTeamData():
        """Generate a new team creation data window then check the data by checkData and finally save the new record to the database.
        ( static method to call by Team.getNewTeamData() )
        """
        pass

    @staticmethod
    def addNewTeam(teamData):
        """Create the new Team record after checking the teamData and save the new object to the database using DbAbstractInterface."""
        pass

    @staticmethod
    def editTeamData():
        """Generate team edit data window for input basic data like team 'name'.
        Then data are checked by checkData() method and finally saved to the database.
        ( static method to call by Team.editTeamData() )
        """
        pass

    def actualiseCalculatedData(self, goalsScored, goalsMissed, yellowCards):
        """Actualise team calculated data, have to be called by Play.recordGamesData() implicitly.

        Args:
            goalsScored (int): goals scored in the game
            goalsMissed (int): goals missed in the game
            yellowCards (int): yellow cards in the game
        """
        pass

    @staticmethod
    def getTeamsCount():
        """Get the current number of teams record saved in the database"""
        pass

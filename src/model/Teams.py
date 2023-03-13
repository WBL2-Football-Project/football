from __future__ import annotations
from dataclasses import dataclass,field
from Serialisable import Serialisable

@dataclass(order=True)
class Teams(Serialisable):
    """Manages the teams data structure.
    
        Fields

            teamID (int): (PM) The team ID
            name (str): The team name
            totalGoalsScored (int): (calculated) The total goals scored by the team during tournament
            totalGoalsMissed (int): (calculated) The total goals misses by the team during tournament
            totalYellowCards (int): (calculated) The total yellow cards played by the team during tournament
            totalPoints (int): (calculated) The total points played by the team during tournament
    """

    teamID:int = field(default=0)
    name:str = field(default='')
    totalGoalsScored:int = field(default=0)
    totalGoalsMissed:int = field(default=0)
    totalYellowCards:int = field(default=0)
    totalPoints:int = field(default=0)

    def checkData(self,teamObj:Teams,forEdit:bool=False):
        """Check if the edited name of the team is correct and can be saved to the database.
        Returns True if data is correct and False otherwise.

        Args:
            teamObj (Teams): The team object with data
            forEdit (bool): True if checking for edit reasons, False otherwise
        """
        print('checkData teamObj',teamObj,'forEdit',forEdit)
        if not forEdit:
            if len(teamObj.name)==0 or teamObj.teamID==0:
                self.getSystemController().getApp().showErrorMessage('Team check failed','Team data is incorrect, some fields could be empty.')
                return False
            elif len(self.getSystemController().getDb().getListOfRecords(Teams,lambda x: x.teamID==teamObj.teamID or x.name==teamObj.name))>0:
                self.getSystemController().getApp().showErrorMessage('Team check failed','Team index or name duplicated.')
                return False
        else:
            if len(teamObj.name)==0:
                self.getSystemController().getApp().showErrorMessage('Team check failed','Team name cannot be empty.')
                return False
            elif len(self.getSystemController().getDb().getListOfRecords(Teams,lambda x: x.name==teamObj.name and x.teamID!=teamObj.teamID))>0:
                self.getSystemController().getApp().showErrorMessage('Team check failed','Team name duplicated, you have it in the database already.')
                return False
        return True

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

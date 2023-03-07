from typing import List,Optional
from Teams import *
from Schedule import *
from unittest import TestCase
from Serialisable import Serialisable
import inspect

class Play(Serialisable):
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
            revelantScheduleIDForTeam1 (int) : after the play is completed, the winner team1ID should be set in the coresponing future schedule ID object
            revelantScheduleIDForTeam2 (int) : after the play is completed, the winner team2ID should be set in the coresponing future schedule ID object
        """
        # Serialisable.__init__(self,self.__class__,["playID","team1ID","team2ID","team1GoalsScored","team2GoalsScored","team1GoalsMissed","team2GoalsMissed","team1YellowCards","team2YellowCards",
        #     "isPlayCompleted","relevantScheduleIDForTeam1","relevantScheduleIDForTeam2"])
        self.playID:int = 0
        self.team1ID:int = 0
        self.team2ID:int = 0
        self.team1GoalsScored:Optional[int] = None
        self.team2GoalsScored:Optional[int] = None
        self.team1GoalsMissed:Optional[int] = None
        self.team2GoalsMissed:Optional[int] = None
        self.team1YellowCards:Optional[int] = None
        self.team2YellowCards:Optional[int] = None
        self.isPlayCompleted:bool = False
        self.relevantScheduleIDForTeam1:Optional[int] = None
        self.relevantScheduleIDForTeam2:Optional[int] = None

    def generateRandomGroupPhasePlaySchedule(self):
        """Generates a random play schedule for entire tournament after is checked if expected amount of teams is defined.
        Method uses helpers: generateRandomTeamsList(), prepareGroupPhaseData(), preparePlayoffPhaseData().
        Call saveRelativeScheculeRecords() when the tournament schedule is calculated.
        Sets ApplicationState.setIsScheduled() after full schedule is saved."""
        pass

    def _generateRandomTeamsList(self):
        """Generates a randomly sorted list of all teams for further schedule computation."""
        pass

    def _prepareGroupPhaseData(self,randomTeamsList:List[Teams]):
        """Generates a breakdown of the teams into 4 groups of 3 teams each.
        """
        pass

    def _preparePlayoffPhaseData(self,randomTeamsList:List[Teams],groupsTeamsDistribution:List):
        """Generates a breakdown of the teams for quarter-final (4 plays of 2 teams each), semi-final (2 plays of 2 teams each), 3rdPlace-final (1 play of 2 teams) and final (1 play of 2 teams).
        """
        pass

    def saveRelativeScheduleRecords(self,randomTeamsList:List[Teams],groupsTeamsDistribution:List):
        """Creates full schedule calendar records for each required play of tournament for both group and playoff games.
        The coresponding to every scheduled game Play objects records are saved into the database as well."""
        pass

    def actualiseOneGameData(self, playID, team1GoalsScored, team2GoalsScored, team1GoalsMissed, team2GoalsMissed, team1YellowCards, team2YellowCards, isPlayCompleted=False):
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

    @staticmethod
    def generateplayoffphaseplayschedule():
        """Generates new list of the schedule objects for every games in the playoff phase after the group phase is completed.

        - get 2 best teams from every of group
        - get the max ID used currently in the database of Schedule table using DBAbstractInterface.getMaxIdFromTable()
        - prepare 4 schedule object (with unique schedule ID's) for quarter-final tree of games, match the winner from 
            one group always with the 2nd place team from the other random group
        - prepare 2 schedule object (with unique schedule ID's) for the semi-final tree of games, match the winner teams from quarter-final
        - prepare 2 schedule object (with unique schedule ID's) for the final tree of games, match the looser teams for the 3rd place final 
            and the winner teams for the 1st place final
        
        Importat notice: 
            Quarter-final and semi-final tree of games expect us to set the fields: revelantScheduleIDForTeam1 and revelantScheduleIDForTeam2,
            which indicate the scheduleID primary key fields in the next level of tree of games. We don't know at this moment who will be the
            winner in every play scheduled. That's why when the specific playoff game will be completed, the ID of the winner team should be
            set into the corresponding schedule object referenced by revelantScheduleIDForTeam1 and revelantScheduleIDForTeam2. After this
            setup, the next future schedule with be fullfiled by the actually team ID's wheres before those fields have to be setted up to None.

        Returns:
            List[Schedule] : list of Schedule objects
        """

class PlayTesting(TestCase):
    def test_surface(self):
        pass

if __name__ == "__main__":
    p=Play()
    # print('properties',[ k for k,v in Play().__dict__.items() if not k.startswith('_') ] )
    # print('tableNameList',p.tableNameList,'properties',[p for p in dir(Play) if isinstance(getattr(Play,p),property)])

    # starting database
    from DBPickleFile import DBPickleFile
    db=DBPickleFile(fileName='test_db.pck')

    # add some records
    db.startDatabase()
    db.addDataToDb(Play,p)
    p.playID=p.playID+1
    db.addDataToDb(Play,p)
    p.playID=p.playID+1
    db.addDataToDb(Play,p)

    # list all records
    print("after 3 records added",[ x.playID for x in db.getListOfRecords(Play) ]) # type: ignore

    # how much records we have
    print("amount of records",db.getCountOfRecordsInTable(Play))

    # modify record
    oldId=0
    p.playID=3
    db.updateDataInDb(Play,p,oldId)
    print("after change",oldId," into ",p.playID,[ x.playID for x in db.getListOfRecords(Play) ]) # type: ignore

    # delete one record
    db.deleteDataFromDb(Play,lambda x: x.playID==2) # type: ignore
    print("after deleting 2",[ x.playID for x in db.getListOfRecords(Play) ]) # type: ignore

    print("max ID",db.getMaxIdFromTable(Play))

    # truncate table
    db.truncateTable(Play)
    print("after truncate",[ x.playID for x in db.getListOfRecords(Play) ]) # type: ignore

from dataclasses import dataclass,field
import random
from datetime import *

from typing import Optional,List,Dict,Union
from Serialisable import Serialisable
from Schedule import Schedule
from Play import Play
from TimeOfDay import TimeOfDay

@dataclass(order=True)
class Group(Serialisable):
    """Class representing every single group in group phase of tournament
    
        Fields:
            groupID (int)=0 : the group ID
            groupName (str)="" : the group name
            team1PlayCounter (int)=0 : the amount of plays completed for team 1
            team2PlayCounter (int)=0 : the amount of plays completed for team 2
            team3PlayCounter (int)=0 : the amount of plays completed for team 3
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
    """

    groupID:int=field(default=0)
    groupName:str=field(default="")
    team1ID:int=field(default=0)
    team2ID:int=field(default=0)
    team3ID:int=field(default=0)
    team1Score:int=field(default=0)
    team2Score:int=field(default=0)
    team3Score:int=field(default=0)
    team1GoalsScored:int=field(default=0)
    team2GoalsScored:int=field(default=0)
    team3GoalsScored:int=field(default=0)
    team1GoalsMissed:int=field(default=0)
    team2GoalsMissed:int=field(default=0)
    team3GoalsMissed:int=field(default=0)
    team1YellowCards:int=field(default=0)
    team2YellowCards:int=field(default=0)
    team3YellowCards:int=field(default=0)

    def _betterTeam(self,c1,c2):
        """Return which index of team in group ( c1,c2 in [1,2,3] ) is better from two given team indexes: c1,c2

        Args:
            c1 (int): index of team in grup (1,2 or 3)
            c2 (int): index of team in grup (1,2 or 3)

        Returns:
            int: index of the team in group (1,2 or 3) which is better then the other from c1,c2
        """
        _team1=f'team{c1}'
        _team2=f'team{c2}'
        _score1=getattr(self,f'{_team1}Score')
        _goals1=getattr(self,f'{_team1}GoalsScored')
        _missed1=getattr(self,f'{_team1}GoalsMissed')
        _yellow1=getattr(self,f'{_team1}YellowCards')
        _score2=getattr(self,f'{_team2}Score')
        _goals2=getattr(self,f'{_team2}GoalsScored')
        _missed2=getattr(self,f'{_team2}GoalsMissed')
        _yellow2=getattr(self,f'{_team2}YellowCards')
        if _score1>_score1: return c1
        elif _score2>_score1: return c2
        elif _score1==_score2:
            if _goals1>_goals2: return c1
            elif _goals2>_goals1: return c2
            else:
                if _missed1<_missed2: return c1
                elif _missed2<_missed1: return c2
                else:
                    if _yellow1<_yellow2: return c1
                    elif _yellow2<_yellow1: return c2
                    else:
                        if random.randrange(1)==0: return c1
                        else: return c2

    def getGroupWinner(self) -> int:
        """Return teamID of the winner team for the group.

        Returns:
            int: teamID
        """
        _winnerCn=0
        if self._betterTeam(1,2) and self._betterTeam(1,3): _winnerCn=1
        elif self._betterTeam(2,1) and self._betterTeam(2,3): _winnerCn=2
        else: _winnerCn=3
        return getattr(self,f'team{_winnerCn}ID')

    def getGroupSecondPlace(self):
        """Return teamID of the second place winner team for the group.

        Returns:
            int: teamID
        """
        _2ndPlace=0
        if self._betterTeam(1,2) and not self._betterTeam(1,3): _2ndPlace=1
        elif self._betterTeam(2,1) and not self._betterTeam(2,3): _2ndPlace=2
        else: _2ndPlace=3
        return getattr(self,f'team{_2ndPlace}ID')

    @staticmethod
    def showMatchOrderGroupsStatus():
        """Show the current status of statistics for every 4 groups of group phase of tournament.
        Follow the 'show match order group status' sequence diagram.
        - get the groups data from database
        - get the schedules data from database and match to the groups data
        - call the UIAbstractInterface.displayStatisticsForGroupAndItsGamesSchedule() to show the statistics on the screen
        """
        pass

    def actualiseOneGroupStatistics(self,				 
                 team1AddGoalsScored:Optional[int]=None,
                 team1AddGoalsMissed:Optional[int]=None,
                 team1AddYellowCards:Optional[int]=None,
                 team2AddGoalsScored:Optional[int]=None,
                 team2AddGoalsMissed:Optional[int]=None,
                 team2AddYellowCards:Optional[int]=None,
                 team3AddGoalsScored:Optional[int]=None,
                 team3AddGoalsMissed:Optional[int]=None,
                 team3AddYellowCards:Optional[int]=None
                 ):
        """Actualise the current statistics for current group object (representing the particular record in the database)
        for goals and cards scores for evert of 3 teams in the group.
        - remove the parameters not given, check the rest if are about 2 teams from group
        - add statistics for this 2 teams in the group
        - increese the play counter for those teams
        - check if every team play counter is equal to 3 (every team is expected to play 3 games during the group phase)
        - if every team in group object had already 3 plays, set the isGroupCompleted flat to true
        - if isGroupCompleted is true, check every other group record in the database and if every groups are already completed,
            set the ApplicationState.setGroupPhaseCompleted()

        Args:
            team1AddGoalsScored (int,optional): team 1 amount of scored goals to add after next play is completed
            team1AddGoalsMissed (int,optional): team 1 amount of missed goals to add after next play is completed
            team1AddYellowCards (int,optional): team 1 amount of yellow cards to add after next play is completed
            team2AddGoalsScored (int,optional): team 2 amount of scored goals to add after next play is completed
            team2AddGoalsMissed (int,optional): team 2 amount of missed goals to add after next play is completed
            team2AddYellowCards (int,optional): team 2 amount of yellow cards to add after next play is completed
            team3AddGoalsScored (int,optional): team 3 amount of scored goals to add after next play is completed
            team3AddGoalsMissed (int,optional): team 3 amount of missed goals to add after next play is completed
            team3AddYellowCards (int,optional): team 3 amount of yellow cards to add after next play is completed
        """
        pass


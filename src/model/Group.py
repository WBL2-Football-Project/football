from typing import Optional


class Group:
    """Class representing every single group in group phase of tournament"""

    def __init__(self):
        """Fields:
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
        self.groupID: int = 0
        self.groupName: str = ""
        self.team1ID: int = 0
        self.team2ID: int = 0
        self.team3ID: int = 0
        self.team1Name: str = ""
        self.team2Name: str = ""
        self.team3Name: str = ""
        self.teams1PlayCounter: int = 0
        self.teams2PlayCounter: int = 0
        self.teams3PlayCounter: int = 0
        self.team1Score: int = 0
        self.team2Score: int = 0
        self.team3Score: int = 0
        self.team1GoalsScored: int = 0
        self.team2GoalsScored: int = 0
        self.team3GoalsScored: int = 0
        self.team1GoalsMissed: int = 0
        self.team2GoalsMissed: int = 0
        self.team3GoalsMissed: int = 0
        self.team1YellowCards: int = 0
        self.team2YellowCards: int = 0
        self.team3YellowCards: int = 0

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
                                    team1AddGoalsScored: Optional[int] = None,
                                    team1AddGoalsMissed: Optional[int] = None,
                                    team1AddYellowCards: Optional[int] = None,
                                    team2AddGoalsScored: Optional[int] = None,
                                    team2AddGoalsMissed: Optional[int] = None,
                                    team2AddYellowCards: Optional[int] = None,
                                    team3AddGoalsScored: Optional[int] = None,
                                    team3AddGoalsMissed: Optional[int] = None,
                                    team3AddYellowCards: Optional[int] = None
                                    ):
        """Actualise the current statistics for current group object (representing the particular record in the database)
        for goals and cards scores for evert of 3 teams in the group.
        - remove the parameters not given, check the rest if are about 2 teams from group
        - add statistics for this 2 teams in the group
        - increese the play counter for those teams
        - check if every team play counter is equal to 3 (every team is expected to play 3 games during the group phase)
        - if every team in group object had already 3 plays, set the isGroupCompleted flat to true
        - if isGroupCompleted is true, check every other group record in the database and if every groups are already completed,
                set the StateMachine.setGroupPhaseCompleted()

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

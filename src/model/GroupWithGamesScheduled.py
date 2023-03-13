from typing import List
from Group import *
from Schedule import *

class GroupWithGamesScheduled(Group):
	"""A group structure extended by list of related games scheduled objects including the play records for each schedule."""
	def __init__(self,group,schedulesList:List[Schedule]):
		"""
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
			scheduleList (List[Schedule]) : the schedule list containing the coresponding Play record data
		"""
		self.groupID:int=group.groupID
		self.groupName:str=group.groupName
		self.team1ID:int=group.team1ID
		self.team2ID:int=group.team2ID
		self.team3ID:int=group.team3ID
		self.teams1PlayCounter:int=group.teams1PlayCounter
		self.teams2PlayCounter:int=group.teams2PlayCounter
		self.teams3PlayCounter:int=group.teams3PlayCounter
		self.team1Score:int=group.team1Score
		self.team2Score:int=group.team2Score
		self.team3Score:int=group.team3Score
		self.team1GoalsScored:int=group.team1GoalsScored
		self.team2GoalsScored:int=group.team2GoalsScored
		self.team3GoalsScored:int=group.team3GoalsScored
		self.team1GoalsMissed:int=group.team1GoalsMissed
		self.team2GoalsMissed:int=group.team2GoalsMissed
		self.team3GoalsMissed:int=group.team3GoalsMissed
		self.team1YellowCards:int=group.team1YellowCards
		self.team2YellowCards:int=group.team2YellowCards
		self.team3YellowCards:int=group.team3YellowCards
		self.scheduleList=schedulesList

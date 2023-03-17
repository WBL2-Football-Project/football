from typing import Optional
from Schedule import *
from Play import *
from TimeOfDay import *

class SchedulesWithPlay(Schedule):
	"""Schedule object with additional corresponding play object data
	"""
	def __init__(self,schedule:Optional[Schedule]=None,play:Optional[Play]=None,team1:Optional[Teams]=None,team2:Optional[Teams]=None):
		"""Fields:
			scheduleID (int) : schedule ID
			playID (int) : corresponding play object ID
			play (int) : corresponding play object full data
			date (datetime) : scheduled date
			timeOfDay (TimeOfDay) : time of the day whene the game is scheduled
			isPlayCompleted (bool) : True means the game is completed, False - we don't have results yet
			isGroupPhase (bool) : True means this game is for group phase of tournament, False - playoff phase of tournament
			team1 (Teams) : team full data
			team2 (Teams) : team full data
		"""
		super()
		self.scheduleID = schedule.scheduleID
		self.playID = schedule.playID
		self.date = schedule.date
		self.timeOfDay = schedule.timeOfDay
		self.isPlayCompleted = schedule.isPlayCompleted
		self.isGroupPhase = schedule.isGroupPhase
		self.play = play
		self.team1 = team1
		self.team2 = team2

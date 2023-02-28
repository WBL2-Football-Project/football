from typing import Optional
from Schedule import *
from Play import *
from TimeOfDay import *

class SchedulesWithPlay(Schedule):
	"""Schedule object with additional corresponding play object data
	"""
	def __init__(self,schedule:Schedule,play:Optional[Play]):
		"""Fields:
			scheduleID (int) : schedule ID
			playID (int) : corresponding play object ID
			play (int) : corresponding play object full data
			date (datetime) : scheduled date
			timeOfDay (TimeOfDay) : time of the day whene the game is scheduled
			isPlayCompleted (bool) : True means the game is completed, False - we don't have results yet
			isGroupPhase (bool) : True means this game is for group phase of tournament, False - playoff phase of tournament
		"""
		self.scheduleID = schedule.scheduleID
		self.playID = schedule.playID
		self.date = schedule.date
		self.timeOfDay = schedule.timeOfDay
		self.isPlayCompleted = schedule.isPlayCompleted
		self.isGroupPhase = schedule.isGroupPhase
		self.play = play

from typing import List
from dataclasses import dataclass,field
from Group import Group
from Schedule import Schedule
from Play import Play
from Serialisable import Serialisable

@dataclass(order=True)
class PlayWithSchedule(Play,Serialisable):
	schedule:Schedule=field(default=Schedule())

@dataclass(order=True)
class GroupWithGamesScheduled(Group,Serialisable):
	"""A group structure extended by list of related games scheduled objects including the play records for each schedule."""
	play1:PlayWithSchedule=field(default=PlayWithSchedule())
	play2:PlayWithSchedule=field(default=PlayWithSchedule())
	play2:PlayWithSchedule=field(default=PlayWithSchedule())

from enum import Enum

class TimeOfDay(Enum):
    Morning='morning'
    Afternoon='Afternoon'

class Schedule:
    """Manages the schedule of the tournament plays."""
    def __init__(self):
        """Fields
            scheduleID (int): (PK) schedule record ID
            playID (int): (FK) corresponding play record ID
            date (datetime): date of play scheduled
            timeOfDay (TimeOfDay): time of day of play scheduled
            isPlayCompleted (bool): is play completed
            isGroupPhase (bool): is play in group phase
        """
        self.scheduleID = None
        self.playID = None
        self.date = None
        self.timeOfDay = None
        self.isPlayCompleted = None
        self.isGroupPhase = None

    def checkIfTournamentBegan(self):
        """Check if the tournament is started by calling @StateMachine.checkIsGroupScheduled() and return True.
        """
        pass

    def checkIfEqual16(self):
        """Check if there's a 16 teams registered.
        Returns True if yes otherwise False.
        """
        pass

    @staticmethod
    def recordGamesData():
        """Creates a window with list of unfinished games to choose from. Then create window with current play statistics to edit for referee. Then save statistics to database."""
        pass

    @staticmethod
    def showMatchOrderGroupsStatus():
        """Creates a window with list of current games statistics for tournament group stage."""
        pass

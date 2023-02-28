from TimeOfDay import *

# TODO:
# showmatchorderplayofftree
# #recordgamesdata
# calculateplayoffphaseschedule
# #calculategroupphaseschedule
# #checkifequal16
# #checkiftournamentbegan

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

    def calculateGroupPhaseSchedule(self):
        """Calculate group phase schedule. This method can be called only with referee rights account.
        To calculate group phase schedule use the 'Calculate Group Phase Schedule' sequence diagram.
        When done correctly, in database should be group records and every group phase games schedule saved.
        When done correctly, the proper StateMachine record should be updated by calling StateMachine.setIsGroupsScheduled().

        References: 
            Group
            Schedule
            StateMachine
            Schedule.calculateGroupPhaseSchedule()
        """
        pass

    def calculatePlayoffPhaseSchedule(self):
        """Calculate playoff phase schedule only if the group phase is already calculated. 
        This method can be called only with referee rights account.
        To calculate playoff phase schedule use the 'Calculate Playoff Phase Schedule' sequence diagram.
        When done correctly, in the database should be every playoff game scheduled with NULL team1/2 ID's 
        but with virtual team1/2 completed for future games with unknown yes compatitors.
        When done correctly, the proper StateMachine record should be updated by calling StateMachine.setIsPlayoffScheduled().

        References: 
            StateMachine
            Schedule
            Schedule.calculateGroupPhaseSchedule()
        """
        pass

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

    @staticmethod
    def calculateplayoffphaseschedule():
        """Manages of the generation of the schedule for entire playoff stage of the tournament.
        - check is playoff scheduled and show the error message if it is, then end the procedure
        - create a dialog yes no to let the user confirm the calculation have to be done
        - generate playoff phase play schedule (coresponding method from Play class)
        - use the list of schedules returned for sarialise it into the database (using add data to db from DBAbstractInterface class)
        - set is playoff scheduled (corresponding method from StateMachine class)
        - show confirmation message to use, everything's done (show info message from UIAbstractInterface class)
        """
        pass

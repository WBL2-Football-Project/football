from enum import Enum

# exception related to AccountRights class
class ExceptionStateMachine(Exception):
    def __init__(self, message='StateMachine Exception'):
        super().__init__(f"ERROR(StateMachine): {message}")

class AccountRights(Enum):
    """Enum defining the types of account rights"""
    NotLoggedIn='Not Logged In'
    UserRights='User Rights'
    RefereeRights='Referee Rights'

class StateMachine:
    """This class keep the current state of the application instance, e.g. holding instances for: is schedule generated or current user account rights."""

    def __init__(self):
        self.groupScheduleGenerated = False
        self.groupPhaseCompleted = False
        self.playoffScheduleGenerated = False
        self.accountRights:AccountRights = AccountRights.NotLoggedIn

    def checkIsGroupScheduled(self):
        """Returns True if the games group phase schedules is generated."""
        return self.scheduleGenerated
    
    def checkIsGroupPhaseCompleted(self):
        """Returns True if the games group phase schedules is completed."""
        return self.groupPhaseCompleted

    def setIsGroupScheduled(self,isGroupScheduled:bool):
        """Sets the isGroupScheduled flag of the application

        Args:
            isGroupScheduled (bool): the games group phase callendar is scheduled
        """
        self.scheduleGenerated = isGroupScheduled

    def checkIsPlayoffScheduled(self):
        """Returns True if the games playoff schedules is generated."""
        return self.scheduleGenerated

    def setIsPlayoffScheduled(self,isPlayoffScheduled:bool):
        """Sets the isPlayoffScheduled flag of the application

        Args:
            isPlayoffScheduled (bool): the games playoff phase callendar is scheduled

        Exceptions:

        """
        if not self.setIsGroupScheduled:
            raise ExceptionStateMachine("you don't have a group phase callendar yet, generate it first")
        self.scheduleGenerated = isPlayoffScheduled

    def setAccountRights(self, accountRights:AccountRights):
        """Sets the accountRights flag of the application, which usually should be set after a user is logged in.

        Args:
            accountRights (AccountRights): account rights deducted from the database user account data

        Raises:
            ExceptionStateMachine: exception state machine could be raised when improper account rights value was given
        """
        try:
            _rightName=AccountRights(accountRights)
            self.accountRights = accountRights
        except:
            raise ExceptionStateMachine('setAccountRights, accountRights must be AccountRights type')

    def isLoggedIn(self):
        """Return True if the user is logged in properly."""
        return self.accountRights!=AccountRights.NotLoggedIn

    def isUserRights(self):
        """Return True if the user is logged in and have 'user' account rights."""
        return self.accountRights==AccountRights.UserRights

    def isRefereeRights(self):
        """Return True if the user is logged in and have 'referee' account rights."""
        return self.accountRights==AccountRights.RefereeRights

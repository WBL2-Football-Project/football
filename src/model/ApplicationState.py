from AccountRights import *
from Serialisable import Serialisable

# exception related to AccountRights class
class ExceptionApplicationState(Exception):
    def __init__(self, message='ApplicationState Exception'):
        super().__init__(f"ERROR(ApplicationState): {message}")

class ApplicationState(Serialisable):
    """This class keep the current state of the application instance, e.g. holding instances for: is schedule generated or current user account rights."""

    def __init__(self):
        Serialisable.__init__(self,self.__class__,["groupScheduleGenerated","groupPhaseGenerated","playoffScheduleGenerated","accountRights"])
        self.ApplicationStateID=0
        self.groupScheduleGenerated = False
        self.groupPhaseCompleted = False
        self.playoffScheduleGenerated = False
        self.accountRights:AccountRights = AccountRights.NotLoggedIn

    def setGroupPhaseCompleted(self):
        """Set into database the groupPhaseCompleted to True, which means that tournament group phase is completed and the playoff phase is beginning."""
        pass

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
            raise ExceptionApplicationState("you don't have a group phase callendar yet, generate it first")
        self.scheduleGenerated = isPlayoffScheduled

    def setAccountRights(self, accountRights:AccountRights):
        """Sets the accountRights flag of the application, which usually should be set after a user is logged in.

        Args:
            accountRights (AccountRights): account rights deducted from the database user account data

        Raises:
            ExceptionApplicationState: exception state machine could be raised when improper account rights value was given
        """
        try:
            _rightName=AccountRights(accountRights)
            self.accountRights = accountRights
        except:
            raise ExceptionApplicationState('setAccountRights, accountRights must be AccountRights type')

    def isLoggedIn(self):
        """Return True if the user is logged in properly."""
        return self.accountRights!=AccountRights.NotLoggedIn

    def isUserRights(self):
        """Return True if the user is logged in and have 'user' account rights."""
        return self.accountRights==AccountRights.UserRights

    def isRefereeRights(self):
        """Return True if the user is logged in and have 'referee' account rights."""
        return self.accountRights==AccountRights.RefereeRights

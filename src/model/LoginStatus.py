from typing import Optional,Callable
from AccountRights import *

class LoginStatus:
    """Login status object to hold the login and rights information about the current logged in account."""
    def __init__(self,login:Optional[str]=None,rights:AccountRights=AccountRights.NotLoggedIn):
        """Fields:

            login (str, optional): The login identifier
            rights (AccountRights): The rights level to the application and database
            eventHandler (Callable[[str,AccountRights],None]): The rights changed event handler 
                (common event handler should leads to UI class implementation and is set automatically
                by the SystemController class)

            Arguments:
                login (str, optional): The login identifier
                rights (AccountRights): The rights level to the application and database
        """
        self.login = None
        self.rights:AccountRights = AccountRights.NotLoggedIn

    def setRightsChangedEventHandler(self,eventHandler:Callable[[str,AccountRights],None]):
        self.rightsChangesEventHandler = eventHandler

    def loginStatus(self,login:str,rights:AccountRights):
        """Registering the new login and rights status.

        Args:
            login (str): login identifier
            rights (AccountRights): rights level to the application and database
        """
        _oldRights=self.rights

        self.login=login
        self.rights=rights

        if not _oldRights == self.rights:
            self.rightsChangesEventHandler(self.login,self.rights)

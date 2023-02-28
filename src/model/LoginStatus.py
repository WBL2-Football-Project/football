from typing import Optional
from AccountRights import *

class LoginStatus:
    """Login status object to hold the login and rights information about the current logged in account."""
    def __init__(self,login:Optional[str]=None,rights:AccountRights=AccountRights.NotLoggedIn):
        """Fields:

            login (str, optional): The login identifier
            rights (AccountRights): The rights level to the application and database
        """
        self.login = None
        self.rights:AccountRights = AccountRights.NotLoggedIn

    def loginStatus(self,login:str,rights:AccountRights):
        """Registering the new login and rights status.

        Args:
            login (str): login identifier
            rights (AccountRights): rights level to the application and database
        """

        self.login=login
        self.rights=rights

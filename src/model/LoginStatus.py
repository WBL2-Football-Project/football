from StateMachine import *

class LoginStatus:
    """Login status object to hold the login and rights information about the current logged in account."""
    def __init__(self):
        """Fields:

            login (str): The login identifier
            rights (AccountRights): The rights
        """
        self.login = None
        self.rights:AccountRights = AccountRights.NotLoggedIn

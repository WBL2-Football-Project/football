"""PyDoc test
"""
from StateMachine import *
class Users:
    """Manages users accounts."""
    
    def __init__(self):
        """Fields
            login (str)              user login
            password (str)           user password
            rights (AccountRights)   user rights type   
        """
        self.login = None
        self.password = None
        self.rights = None

    def checkNewUserData(self, login, password):
        """Check if new account with user rights is possible (in relation to accounts existed in the current database).

        Args:
            login (str): user login
            password (str): user password

        Returns:
            True if login and password are valid (still are free to use), False otherwise
        """
        pass

    def checkNewUserDataReferee(self, login, password, rights:AccountRights):
        """Check if new account with user or referee rights is possible (in relation to accounts existed in the current database).

        Args:
            login (str): user login
            password (str): user password
            rights (AccountRights): account rights

        Returns:
            True if login and password are valid (still are free to use), False otherwise
        """
        pass

    def getNewAcountDataReferee(self):
        """Generates UI dialog window for input login, password and rights type.
        Then checks if the data provided is valid and new account is possible to create.
        Then creates the new account in the database.
        """
        pass

    def getNewAccountDataUser(self):
        """Generates UI dialog window for input login and password for user type rights only.
        Then checks if the data provided is valid and new account is possible to create.
        Then creates the new account in the database.
        """
        pass

    def checkRightChange(self, ID, login, password, rights):
        """Check if the change of new data provided by user for the account record ID is possible and could be accepted.
        (Descreesing the rights into the user type rights for last existing account is impossible, same for changing the login to equal to the other which also exists in the database)

        Args:
            ID (int): account record ID
            login (str): login string
            password (str): password string
            rights (AccountRights): account rights
        """
        pass


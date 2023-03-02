from AccountRights import *
from Serialisable import Serialisable

class Users(Serialisable):
    """Manages users accounts."""
    
    def __init__(self):
        """Fields
            login (str)              user login
            password (str)           user password
            rights (AccountRights)   user rights type   
        """
        self.login:str = ""
        self.password:str = ""
        self.rights:AccountRights = AccountRights.NotLoggedIn

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

    def checkRightsChange(self, ID, login, password, rights):
        """Check if the change of new data provided by user for the account record ID is possible and could be accepted.
        (Descreesing the rights into the user type rights for last existing account is impossible, same for changing the login to equal to the other which also exists in the database)

        Args:
            ID (int): account record ID
            login (str): login string
            password (str): password string
            rights (AccountRights): account rights
        """
        pass

    @staticmethod
    def changeUserRights():
        """Generates UI dialogs for changing user rights.

        - creates the new dialog windows for input user data: ID, login (search database filter, user can leave it blank to see all the records)
        - get list of records from database (refer to DBAbstractInterface get list of records), show error message if empty and finish the procedure
        - let the user choose from the list of records (refer to UIAbstractInterface - choose record from list)
        - for every record chosen to edit, create new dialog window for getting new 'rights'
        - check the new value of the rights (refer to Users check rights change) and show error message if it's forbidden then exit
        - save the new value of the rights to the database (refer to DBAbstractInterface update data in db)
        - show the confirmation message to user and go back to the list of users to let the user choose another one or exit
        """
        pass
    
    @staticmethod
    def logintoapp():
        """Generates UI dialogs for input the login and password data from the user to check the rights with the database.
        
        - create new dialog window for getting: login, password (refer to UIAbstractInterface create new dialog)
        - get rights from database (refer to DBAbstractInterface get rights from db) and show error message if access isn't granted then go back to login dialog
        - update the login status (refer to SystemController loginStatus)
        - start the application main screen with features access depending on the account rights
        """
        pass

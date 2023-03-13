from __future__ import annotations
from dataclasses import dataclass,field,fields
from typing import Optional,Dict,Any
from AccountRights import *
from Serialisable import Serialisable

@dataclass(order=True)
class Users(Serialisable):
    """Manages users accounts.
    
        Fields
            login (str)              user login
            password (str)           user password
            rights (AccountRights)   user rights type   
    """

    userID:int=field(default=0)
    login:str=field(default='')
    password:str=field(default='')
    rights:AccountRights=field(default=AccountRights.NotLoggedIn)

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
        print("checkNewUserDataReferee")
        _rec=self.getDb().getListOfRecords(Users,lambda x: x.login==login)
        if len(_rec)>0:
            self.getApp().showErrorMessage('checkNewUserDataReferee','There is a record found for login '+login+' you cannot save it')
            return False
        return True

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

    def checkRightsChange(self,userObj:Users):
        """Check if the edited name of the user is correct and can be saved to the database.
        Returns True if data is correct and False otherwise.
        Changed fields are:
            - rights (AccountRights)
            - password

        Args:
            teamObj (Users): The team object with data
            forEdit (bool): True if checking for edit reasons, False otherwise
        """
        print('checkData teamObj',userObj)
        if type(userObj.rights)!=AccountRights:
            self.getSystemController().getApp().showErrorMessage('User check failed','User rights cannot be empty.')
            return False
        elif userObj.rights==AccountRights.UserRights and len(self.getSystemController().getDb().getListOfRecords(Users,lambda x: x.rights==AccountRights.RefereeRights and x.userID!=userObj.userID))==0:
            self.getSystemController().getApp().showErrorMessage('User check failed','You cannot change rights into <user rights> for last existing <referee rights> user.')
            return False
        elif len(self.getSystemController().getDb().getListOfRecords(Users,lambda x: x.rights==AccountRights.RefereeRights and x.userID==userObj.userID and x.password==userObj.password))>0:
            self.getSystemController().getApp().showErrorMessage('User check failed','Saving not needed - look\'s like nothing changed.')
            return False
        elif len(userObj.password)==0:
            self.getSystemController().getApp().showErrorMessage('User check failed','You cannot set empty password.')
            return False
        return True

from typing import Dict,Optional,List,Type
import os,sys,pickle
from PickleSerialisation import PickleSerialisation
from DBAbstractInterface import *
from AccountRights import *
from unittest import TestCase
from Serialisable import Serialisable
from Users import Users

class DBPickleFile(PickleSerialisation,DBAbstractInterface):
    """Implements DBAbstractInterface"""

    def __init__(self,fileName='data.db'):
        """DBPickleFile constructor

        Args:
            fileName (str, optional): Pickle filename for holding the database. Defaults to 'data.db'.
        """
        PickleSerialisation.__init__(self,fileName)
        self.fileName = fileName

    def startDatabase(self,systemController):
        """Start database access
        e.g. possible to fill the database with default sample data"""
        self.scanSourcesForSerialised()
        Serialisable.setEnvironment(systemController)

    def getRightsFromDb(self, login, password) -> AccountRights:
        """Checks if login/password pair exists in the database and return the apropiete account rights which is one of values from AccountRights enum class.

        Reference:
            DBAbstractInterface.getRightsFromDb()
        """
        _fullDatabase=self.loadData(Users,lambda x: x.login==login and x.password==password) # type: ignore
        _rights=AccountRights.NotLoggedIn if len(_fullDatabase[Users])==0 else _fullDatabase[Users][0].rights # type: ignore
        return _rights
    
    def listDbContentToConsole(self):
        print("\ndatabase:")
        _fullData=self.loadData()
        for key,value in _fullData.items():
            print()
            print(f'{key.__name__} ({len(value)})')
            for rec in value:
                print("  ",rec)

if __name__=='__main__':
    from Play import Play
    p=Play()
    db=DBPickleFile()
    print(db.addDataToDb(p.__class__,p))

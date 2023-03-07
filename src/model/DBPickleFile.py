from typing import Dict,Optional,List,Type
import os,sys,pickle
from PickleSerialisation import PickleSerialisation
from DBAbstractInterface import *
from AccountRights import *
from unittest import TestCase

class DBPickleFile(PickleSerialisation,DBAbstractInterface):
    """Implements DBAbstractInterface"""

    def __init__(self,fileName='data.db'):
        """DBPickleFile constructor

        Args:
            fileName (str, optional): Pickle filename for holding the database. Defaults to 'data.db'.
        """
        PickleSerialisation.__init__(self,fileName)
        self.fileName = fileName

    def startDatabase(self):
        """Start database access
        e.g. possible to fill the database with default sample data"""
        self.scanSourcesForSerialised()

    def getRightsFromDb(self, login, password) -> AccountRights:
        """Checks if login/password pair exists in the database and return the apropiete account rights which is one of values from AccountRights enum class.

        Reference:
            DBAbstractInterface.getRightsFromDb()
        """
        pass # TODO: to implement
        return AccountRights.RefereeRights # TODO: temporary testing code only - implement it
        return AccountRights.NotLoggedIn

if __name__=='__main__':
    from Play import Play
    p=Play()
    db=DBPickleFile()
    print(db.addDataToDb(p.__class__,p))

from DBAbstractInterface import *
from AccountRights import *

class DBPickleFile(DBAbstractInterface):
    """Implements DBAbstractInterface"""
    def __init__(self,fileName='data.db'):
        self.fileName = fileName
        DBAbstractInterface.__init__(self, self)

    def addDataToDb(self, table, data): 
        """Add new object to the database.
        Reference:
            DBAbstractInterface.addDataToDb()
        """
        pass # TODO: to implement

    def updateDataInDb(self, table, data, ID): 
        """Update object in the database.
        Reference:
            DBAbstractInterface.updateDataInDb()
        """
        pass # TODO: to implement

    def resetAllDataInDb(self): 
        """Reset every data in database.
        Reference:
            DBAbstractInterface.resetAllDataInDb()
        """
        pass # TODO: to implement

    def getCountOfRecordsInTable(self, table): 
        """Return amount of records for chosen table in the database.

        Reference:
            DBAbstractInterface.getCountOfRecordsInTable()
        """
        pass # TODO: to implement

    def truncateTable(self, table): 
        """Zeroes out the specified table in the database.

        Reference:
            DBAbstractInterface.truncateTable()
        """
        pass # TODO: to implement

    def getRightsFromDb(self, login, password) -> AccountRights:
        """Checks if login/password pair exists in the database and return the apropiete account rights which is one of values from AccountRights enum class.

        Reference:
            DBAbstractInterface.getRightsFromDb()
        """
        pass # TODO: to implement
        return AccountRights.RefereeRights # TODO: temporary testing code only - implement it
        return AccountRights.NotLoggedIn

    def getListOfRecords(self, table, filterFunc: Callable[[List[Any]],List[Any]]) -> List[Any]: 
        """Returns list of objects from the table filtered by filter function if provided.

        Reference:
            DBAbstractInterface.getListOfRecords()
        """
        pass # TODO: to implement
        return []

    def getMaxIdFromTable(self, table:Serialisable):
        """Returns the maximum ID numer found in the specific table in the database.
        Reference:
            DBAbstractInterface.getMaxIdFromTable()
        """
        pass # TODO: to implement

from abc import abstractmethod
from AccountRights import *
from typing import Callable,Any,List
from Serialisable import *

# exception related to DBAbstractInterface class
class ExceptionDBAbstractInterface(Exception):
    def __init__(self, message='DBAbstractInterface Exception'):
        super().__init__(f"ERROR(DBAbstractInterface): {message}")

class DBAbstractInterface:
    """Interface class with abstract method. Need to be implemented by the actual DB writing class which defines all the abstract methods
    Raises:
        ExceptionDBAbstractInterface: no <method-name> method defined
    """

    def __init__(self, implementationClassObj):
        """Initialisation of the DBAbstractInterface.
        
        Fields:
            implementationClassObj (DBAbstractInterface) : implementation class object instance access
        
        Args:
            implementationClassObj (DBAbstractInterface): reference to to implementation class (dependency injection pattern)
        """
        self.implementationClassObj = implementationClassObj

    @abstractmethod
    def addDataToDb(self, table, data): 
        """Add new object to the database.

        Args:
            table (class type): class type definition
            data (class instance): class instance to serialise into database

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no addDataToDb method defined")

    @abstractmethod
    def updateDataInDb(self, table, data, ID): 
        """Update object in the database.

        Args:
            table (class type): class type definition
            data (class instance): class instance definition
            ID (int): unique identification of the object in the database

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no updateDataInDb method defined")

    @abstractmethod
    def resetAllDataInDb(self): 
        """Reset every data in database.

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no resetAllDataInDb method defined")

    @abstractmethod
    def getCountOfRecordsInTable(self, table): 
        """Return amount of records for chosen table in the database.

        Args:
            table (class type): class type definition

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no getCountOfRecordsInTable method defined")

    @abstractmethod
    def truncateTable(self, table): 
        """Zeroes out the specified table in the database.

        Args:
            table (class type): class type definition

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no truncateTable method defined")

    @abstractmethod
    def getRightsFromDb(self, login:str, password:str) -> AccountRights:
        """Checks if login/password pair exists in the database and return the apropiete account rights which is one of values from AccountRights enum class.

        Args:
            login (string): user login string
            password (string): user password string

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no getRightsFromDb method defined")

    @abstractmethod
    def getListOfRecords(self, table, filterFunc: Callable[[List[Any]],List[Any]]) -> List[Any]: 
        """Returns list of objects from the table filtered by filter function if provided.

        Args:
            table (class type): class type definition
            filterData (function): function to which the list of objects taken from the database is passed to, which have to return filtered list of objects

        Raises:
            ExceptionDBAbstractInterface: _description_
        """
        raise ExceptionDBAbstractInterface("no getListOfRecords method defined")

    @abstractmethod
    def getMaxIdFromTable(self, table:Serialisable):
        """Returns the maximum ID numer found in the specific table in the database.
        Returns:
            current maximum ID (int): current maximum ID from the specified table
        """
        raise ExceptionDBAbstractInterface("no getMaxIdFromTable method defined")

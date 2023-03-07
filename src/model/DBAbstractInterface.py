from abc import abstractmethod
from AccountRights import *
from typing import Callable,Any,List,Optional
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

    def setSystemController(self, systemControllerInstance):
        self.systemControllerInstance = systemControllerInstance

    def getSystemController(self):
        return self.systemControllerInstance
    
    @abstractmethod
    def startDatabase(self):
        """Start database"""
        raise ExceptionDBAbstractInterface("no startDatabase method defined")

    @abstractmethod
    def addDataToDb(self, table:Type[Serialisable], data:Serialisable) -> bool: 
        """Add new object to the database. If there's object with the same ID, it will be updated.
        Args:
            table (Type[Serialisable]): class type of the objects in the database
            data (Serialisable): class instance to be added/updated to the database

        Returns:
            bool: True if successful or False if not

        Reference:
            DBAbstractInterface.addDataToDb()
        """
        raise ExceptionDBAbstractInterface("no addDataToDb method defined")

    @abstractmethod
    def updateDataInDb(self, table:Type[Serialisable], data:Serialisable, ID) -> bool: 
        """Update the data in the database

        Args:
            table (Type[Serialisable]): class type of the objects in the database
            data (Serialisable): class instance to be added/updated to the database
            ID: object record ID value to find in the database

        Returns:
            bool: True if successful or False if not
        
        Reference:
            DBAbstractInterface.updateDataInDb()
        """
        raise ExceptionDBAbstractInterface("no updateDataInDb method defined")

    @abstractmethod
    def deleteDataFromDb(self, table:Optional[Type[Serialisable]]=None, filter_:Optional[Callable[[Serialisable],bool]]=None):
        """Delete the data from the DB - all or for the specific table optionally with condition.

        Args:
            table (Type[Serialisable]): _description_
            filter_ (Optional[Callable[[Serialisable],bool]], optional): _description_. Defaults to None.

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no deleteDataFromDb method defined")

    @abstractmethod
    def resetAllDataInDb(self): 
        """Reset every data in database.

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        raise ExceptionDBAbstractInterface("no resetAllDataInDb method defined")

    @abstractmethod
    def getCountOfRecordsInTable(self, table:Type[Serialisable]) -> int: 
        """Return amount of records for chosen table in the database.

        Args:
            table (Type[Serialisable]): serialisable class type

        Returns:
            int: amount of objects in the database for specified type of serialisable class

        Reference:
            DBAbstractInterface.getCountOfRecordsInTable()
        """
        raise ExceptionDBAbstractInterface("no getCountOfRecordsInTable method defined")

    @abstractmethod
    def truncateTable(self, table:Type[Serialisable]): 
        """Zeroes out the specified table in the database.

        Args:
            table (Type[Serialisable]): serialisable class type

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
    def getListOfRecords(self, table:Type[Serialisable], filterFunc: Optional[Callable[[Serialisable],bool]]=None) -> List[Serialisable]:
        """Returns list of objects from the table filtered by filter function if provided.

        Reference:
            DBAbstractInterface.getListOfRecords()

        Args:
            table (Type[Serialisable]): serialisable class type
            filterFunc (Callable[[Serialisable],bool],optional): function to filter list of objects. Default to all objects.

        Returns:
            List[Serialisable]: _description_
        """
        raise ExceptionDBAbstractInterface("no getListOfRecords method defined")

    @abstractmethod
    def getMaxIdFromTable(self, table:Type[Serialisable]) -> int:
        """Returns the maximum ID value found in the given table in the database.

        Reference:
            DBAbstractInterface.getMaxIdFromTable()

        Args:
            table (Type[Serialisable]): type of serialised class

        Returns:
            int: max value existed in the database for the table or 0 if there's no records yet
        """
        raise ExceptionDBAbstractInterface("no getMaxIdFromTable method defined")

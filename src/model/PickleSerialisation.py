from typing import Dict,Optional,List,Type,Callable,Any
from dataclasses import fields

import os,sys,pickle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from Serialisable import Serialisable

# class to manage serialisation of database
class PickleSerialisation:
    """PickleSerialisation class for serialise to the file instead of database
    """

    def __init__(self,fileName:str,defaultData:Optional[Dict[Type[Serialisable],List[Serialisable]]]=None):
        """Initialise the class

        Args:
            fileName (str): database file name to save every data to
            defaultData (Optional[Dict[Type[Serialisable],List[Serialisable]]],optional): Mandatory data which have to be saved into empty database at the beginning. Default to None.
        """
        self.fileName=fileName # pickle file name - static variable
        self.defaultData:Dict[Type[Serialisable],List[Serialisable]]={} if defaultData==None else defaultData # default content for the database        
        self._cachedData:Dict[Type[Serialisable],List[Serialisable]]={}
        self._cachedData=self.loadData()

    def listAllTables(self) -> Dict[Type[Serialisable],List[str]]:
        """List all tables defined in the application (classes inherited from Serialisable class)

        Returns:
            Dict[Type[Serialisable],List[str]]: currently recognized serialised classes with full properties names
        """

        # print(Serialisable.tableNameList)
        # return [cls.__name__ for cls in Serialisable.__subclasses__()]
        return Serialisable.tableNameList # type: ignore
       
    def scanSourcesForSerialised(self):
        """Scanning all loaded source code for serialised class types and register them all"""
        for s in [cls for cls in Serialisable.__subclasses__() if cls.__name__!='Serialisable']:
            _s:s.__class__=s() # type: ignore
            Serialisable.tableNameList[s]=[ f.name for f in fields(_s)]
            # Serialisable.tableNameList[s]=[ x for x in list(_s.__dict__.keys()) if x not in ['serialisationClass', 'tableName', 'fieldList'] ]
            # print(s.__name__,Serialisable.tableNameList[s])

    def loadData(self,table:Optional[Type[Serialisable]]=None,filter:Optional[Callable[[Serialisable],bool]]=None) -> Dict[Type[Serialisable],List[Serialisable]]:
        """Loading data from the database, optionally from chosen table with possible filtering records

        Args:
            table (Type[Serialisable],optional): Get only data for table / Serialisation class type. Default table to None.
            filter (Callable[[Serialisable],bool],optional): Filter all the objects if table was given. Defaults to None.

        Returns:
            Dict[Type[Serialisable],List[Serialisable]]: indexed by Type[Serialised] Dictionary, with list of Serialisable objects instances in value
        """
        _ret={}
        if not os.path.exists(self.fileName): 
            self._cachedData={}
            if len(self.defaultData.keys())>0: 
                self.saveData(self.defaultData)
        if len(self._cachedData.keys())!=0:
            _ret=self._cachedData
        try:
            _itemDb=pickle.load(open(self.fileName,"rb"))
            if not isinstance(_itemDb,dict) or len(_itemDb.keys())==0:
                _itemDb=self.defaultData
                self.saveData(_itemDb)
        except FileNotFoundError:
            self.saveData(self.defaultData)
            _itemDb=self.defaultData
        self._cachedData=_itemDb
        _ret=_itemDb

        # add not written tables
        for tableType,records in Serialisable.tableNameList.items():
            if tableType not in _ret:
                _ret[tableType]=[] # type: ignore

        if table!=None:
            if table in _ret.keys():
                if filter==None:
                    _ret={ k:v for k,v in _ret.items() if k==table }
                if filter!=None:
                    _ret[table]=[ x for x in _ret[table] if filter(x) ]
        return _ret

    def saveData(self,data:Dict[Type[Serialisable],List[Serialisable]]): # save data to pickle file
        data={ k: [ x for x in self._sortObjectList(v) ] for k,v in data.items() }
        pickle.dump(data,open(self.fileName,"wb"))
        self._cachedData=data

    def addDataToDb(self, table:Type[Serialisable], data:Serialisable) -> bool: 
        """Add new object to the database. ID field will be recounted before write.
        Args:
            table (Type[Serialisable]): class type of the objects in the database
            data (Serialisable): class instance to be added/updated to the database

        Returns:
            bool: True if successful or False if not

        Reference:
            DBAbstractInterface.addDataToDb()
        """
        if not self._checkTable(table):
            # table is not Serialisable
            return False
        _fulldatabase=self.loadData()
        _ID_fieldName=Serialisable.tableNameList[table][0] # main index field of object
        setattr(data,_ID_fieldName,self.getMaxIdFromTable(table)+1) # recount the ID of the object
        _tableRecords=[ x for x in _fulldatabase[table] if getattr(x,_ID_fieldName)!=getattr(data,_ID_fieldName) ] # get rid of the current object from the table with the same ID
        _tableRecords.append(data)
        _tableRecords=self._sortObjectList(_tableRecords) # sort the record by index
        _fulldatabase[table]=_tableRecords
        self.saveData(_fulldatabase)
        self._cachedData=_fulldatabase
        return True

    def setPrimaryKey(self, objInstance, value) -> Any:
        """Check defined primary key for given object implementation (inherited from Serialisable) and sets the primary key for given value.
        Args:
            objInstance (Serialisable): object instance
            value (Any): valu to set for primary key of given object instance
        """
        if not isinstance(objInstance, Serialisable):
            raise Exception('PIckleSerialisation.setPrimaryKey error: objInstance is not a Serialisable')
        _ID_pm_field_name=Serialisable.tableNameList[objInstance.__class__][0]
        setattr(objInstance,_ID_pm_field_name,value)
        return objInstance

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
        _fulldatabase=self.loadData()
        _recordsLen=len(_fulldatabase[table])
        _ID_fieldName=Serialisable.tableNameList[table][0] # main index field of object
        _tableRecords=[ x for x in _fulldatabase[table] if getattr(x,_ID_fieldName)!=ID ] # get rid of the current object from the table with the same ID
        if len(_tableRecords) == _recordsLen:
            return False # update impossible, the record to edit not found
        _tableRecords.append(data)
        _tableRecords=self._sortObjectList(_tableRecords) # sort the record by index
        _fulldatabase[table]=_tableRecords
        self.saveData(_fulldatabase)
        self._cachedData=_fulldatabase
        return True
    
    def deleteDataFromDb(self, table:Optional[Type[Serialisable]]=None, filterFunc:Optional[Callable[[Serialisable],bool]]=None):
        """Delete the data from the DB - all or for the specific table optionally with condition.

        Args:
            table (Type[Serialisable]): _description_
            filter_ (Optional[Callable[[Serialisable],bool]], optional): _description_. Defaults to None.

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        _fulldatabase:Dict[Type[Serialisable],List[Serialisable]]=self.loadData()
        if table!=None:
            if filterFunc==None:
                _fulldatabase[table]=[]
            else: # only objects matching the filter
                _fulldatabase[table]=list(filter(lambda x: not filterFunc(x),_fulldatabase[table]))
        else:
            _fulldatabase.clear()
        self.saveData(_fulldatabase)

    def resetAllDataInDb(self):
        """Reset every data in database.

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        self.deleteDataFromDb()

    def getCountOfRecordsInTable(self, table:Type[Serialisable]) -> int: 
        """Return amount of records for chosen table in the database.

        Args:
            table (Type[Serialisable]): serialisable class type

        Returns:
            int: amount of objects in the database for specified type of serialisable class

        Reference:
            DBAbstractInterface.getCountOfRecordsInTable()
        """
        _fulldatabase=self.loadData(table)
        return len(_fulldatabase[table])

    def truncateTable(self, table:Type[Serialisable]): 
        """Zeroes out the specified table in the database.

        Args:
            table (Type[Serialisable]): serialisable class type

        Raises:
            ExceptionDBAbstractInterface: exception when method has no implementation in final DB implementation class
        """
        self.deleteDataFromDb(table)

    def getOneRecord(self, table:Type[Serialisable], id:int) -> Any:
        """Find by given id and return one record from database

        Reference:
            DBAbstractInterface.getOneRecord()

        Args:
            table (Type[Serialisable]): serialisable class type
            id:int : record id to find

        Returns:
            Serialisable: one record data in form of Serialisable object
        """
        _ID_fieldName=Serialisable.tableNameList[table][0]
        _list=self.getListOfRecords(table,lambda x: getattr(x,_ID_fieldName)==id)
        if len(_list)==0:
            return None
        return _list[0]

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
        _fulldatabase=self.loadData(table)
        if not table in _fulldatabase:
            _fulldatabase[table]=[]
        elif filterFunc!=None:
            _fulldatabase[table]=list(filter(filterFunc,_fulldatabase[table]))
        return _fulldatabase[table]

    def getMaxIdFromTable(self, table:Type[Serialisable]) -> int:
        """Returns the maximum ID value found in the given table in the database.

        Reference:
            DBAbstractInterface.getMaxIdFromTable()

        Args:
            table (Type[Serialisable]): type of serialised class

        Returns:
            int: max value existed in the database for the table or 0 if there's no records yet
        """

        _fulldatabase=self.loadData(table)
        _maxId=0
        if table in _fulldatabase:
            if len(_fulldatabase[table])>0:
                _list=self._sortObjectList(_fulldatabase[table])
                _ID_fieldName=Serialisable.tableNameList[table][0] # main index field of object
                _maxId=getattr(_list[-1],_ID_fieldName)
        return _maxId

    def _sortObjectList(self,dataList:List[Serialisable]) -> List[Serialisable]:
        """Sort list of objects in the database table by first _ID field

        Args:
            dataList (List[Serialisable]): list of objects in the database table

        Returns:
            List[Serialisable]: sorted list of objects in the database table
        """
        if len(dataList) == 0: # no objects in list
            return dataList
        
        # there are some objects in the list to be sorted
        _type=dataList[0].__class__
        _ID_fieldName=Serialisable.tableNameList[_type][0]
        dataList=sorted(dataList,key=lambda x: getattr(x,_ID_fieldName))
        return dataList

    def _checkTable(self,table:Type[Serialisable]) -> bool:
        """Inner method to check existence of a table in the database table

        Args:
            table (Type[Serialisable]): serialisable class type

        Returns:
            bool: True if ok or False if class is not serialisable
        """
        if not Serialisable.__subclasscheck__(table):
            return False # table is not Serialisable
        if table not in self.loadData(table):
            self._cachedData[table]=[] # adding new class type to serialisable table list
            self.saveData(self._cachedData)
        return True # table is defined in serialisable table list
    
    def getPrimaryKeyFieldNamesList(self,table:Type[Serialisable]) -> List[str]:
        return [ Serialisable.tableNameList[table][0] ]

if __name__=="__main__":
    from __init__ import *
    p=PickleSerialisation('file.db')
    p.scanSourcesForSerialised()
    print('tableNameList',Serialisable.tableNameList)
    print('-------')
    print('List of all serialised classess defined in the source code with fields: ',p.listAllTables())
    print('-------')

from typing import Dict,List,Type,Optional,Any,Union,Callable
from abc import abstractmethod
from datetime import datetime
from enum import Enum
from SerialisableInterface import SerialisableInterface
from DBAbstractInterface import DBAbstractInterface
from AppControlInterface import AppControlInterface
from dataclasses import fields,asdict
from ColumnStyle import ColumnStyle,JustifyEnum

class ExceptionSerialisable(Exception):
    def __init__(self, message='Serialisable Exception'):
        super().__init__(f"ERROR(Serialisable): {message}")

class Serialisable(SerialisableInterface):
    """Inheritance class for the other classes which should be serialized into the database"""

    """static list of serialisable classes in the database
    object (Serialisable) : class to serialise
    List[str] : list of the field names to serialise from class
    """
    tableNameList:Dict[Type[SerialisableInterface], List[str]]={}

    @classmethod
    def setEnvironment(cls, systemController):
        cls.systemController:systemController.__class__=systemController
        cls.dbControl:DBAbstractInterface=systemController.getDb()
        cls.appControl:AppControlInterface=systemController.getApp()

    # def __init__(self,serialisationClass:Type[SerialisableInterface],fieldList:List[str]):
    # 	"""Initialize the serialisation with parameters

    # 	Args:
    # 		serialiseDestinationClass (Serialisable): serialisation class to serialise
    # 		fieldList (List[str]): _description_
    # 	"""
    # 	self.serialisationClass = serialisationClass
    # 	self.tableName = serialisationClass
    # 	self.fieldList = fieldList
    # 	# Serialisable.tableNameList[self.serialisationClass]=self.fieldList
    # 	# print('Serialisable:',[ k.__name__ for k,v in Serialisable.tableNameList.items() ])

    def _fromDictSetField(self,name,value,dataDict:Dict[str,Any]):
        setattr(self, name, value)
        dataDict[name]=value

    def fromDict(self, data:Dict[str,Any]):
        for f in fields(self.__class__): # type: ignore
            if f.name in data:
                print('f.name',f.name,'f.type',f.type,'type(data[f.name])',type(data[f.name]))
                if type(data[f.name])==type(f.default):
                    self._fromDictSetField(f.name, data[f.name],data)
                    # setattr(self, f.name, data[f.name])
                else:
                    if isinstance(f.default,Enum):
                        _enumType=type(f.default)
                        self._fromDictSetField(f.name,_enumType[data[f.name]],data)
                        # setattr(self,f.name,_enumType[data[f.name]])
                    elif f.type == 'str':
                        self._fromDictSetField(f.name, data[f.name] if type(data[f.name])==str else f'{data[f.name]}',data)
                        # setattr(self, f.name, data[f.name] if type(data[f.name])==str else f'{data[f.name]}')
                    elif f.type == 'int':
                        if type(data[f.name])==str:
                            if len(data[f.name])==0:
                                self._fromDictSetField(f.name,0,data)
                                # setattr(self,f.name,0)
                            else:
                                self._fromDictSetField(f.name,int(data[f.name]),data)
                                # setattr(self,f.name,int(data[f.name]))
                        elif data[f.name]==None:
                            self._fromDictSetField(f.name,0,data)
                            # setattr(self,f.name,0)
                        else:
                            raise ExceptionSerialisable(f'fromDict error: cannot convert value {data[f.name]} into type {f.type}')
                    elif f.type == 'float':
                        if type(data[f.name])==str or type(data[f.name])==int:
                            self._fromDictSetField(f.name, float(data[f.name]),data)
                            # setattr(self, f.name, float(data[f.name]))
                        else:
                            raise ExceptionSerialisable(f'fromDict error: cannot convert value {data[f.name]} into type {f.type}')
                    elif f.type == datetime:
                        raise ExceptionSerialisable(f'fromDict error: cannot convert value {data[f.name]} into type {f.type}')
                    elif f.type=='bool':
                        if type(data[f.name])==str:
                            if data[f.name].capitalize().startswith('Y') or data[f.name].startswith('1'):
                                self._fromDictSetField(f.name,True,data)
                                # setattr(self,f.name,True)
                            elif data[f.name].capitalize().startswith('N') or data[f.name].startswith('0'):
                                self._fromDictSetField(f.name,False,data)
                                # setattr(self,f.name,False)
                            else:
                                raise ExceptionSerialisable(f'fromDict error: cannot convert value {data[f.name]} into type {f.type}')
        return self

    def getValuesAsDict(self):
        return [ v for k,v in asdict(self) ] # type: ignore

    @abstractmethod
    def getHeadersForTreeview(self) -> List[ColumnStyle]:
        _headersForTreeview:List[ColumnStyle]=[]
        _pmArray=self.getDb().getPrimaryKeyFieldNamesList(self.__class__)
        for f in fields(self.__class__): # type: ignore
            if f.type in ['int','float']:
                _justify=JustifyEnum.RIGHT
            else:
                _justify=JustifyEnum.LEFT
            _headersForTreeview.append(ColumnStyle(self.getSystemController(),name=f.name,primaryKey=(f.name in _pmArray),justify=_justify))

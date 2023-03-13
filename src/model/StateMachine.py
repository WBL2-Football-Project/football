from __future__ import annotations
from abc import abstractmethod
from dataclasses import fields
from typing import List,Dict,Any,Optional,Union,Callable
from AccountRights import AccountRights
from StateMachineInterface import *
from SystemControllerAbstract import SystemControllerAbstract
from Serialisable import Serialisable

class StateMachine(StateMachineInterface):
    def __init__(self):
        self.states:Dict[str,State]={}
        self.flags:Dict[str,Flag]={}
        self.flagsIsSerialisable:bool=False
        # self.events:Dict[str,Event]={}

    def setSystemController(self,systemController:SystemControllerAbstract):
        self.systemController:systemController.__class__ = systemController

    def getSystemController(self) -> SystemControllerAbstract:
        if self.systemController==None:
            raise ExceptionStateMachine('getSystemController used before setSystemController was called')
        return self.systemController

    def initialiseFlags(self):
        _stateMachineObj=self._genFlagsDbRecord()
        _rec=self.systemController.dbControl.getOneRecord(self.__class__,1)
        if _rec==None:
            self.systemController.dbControl.addDataToDb(self.__class__,_stateMachineObj)
        else:
            _data={ x.name:getattr(_rec,x.name) for x in fields(_rec) if x.name in self.flags } # type: ignore
            for k,f in self.flags.items():
                if not f.isCallable:
                    if f.serialisable:
                        _value=_data[k] if k in _data and type(_data[k])==type(f.default) else f.default
                        self.setFlag(k,_value,False)
                else:
                    self.setFlag(k,f.call(),False)

            # for k,v in _data.items():
            #     print(f'setup data {k}={v} from database')
            #     self.setFlag(k,v,False)
            if self.flagsIsSerialisable:
                self.saveCurrentFlagsToDb()
            print('initialiseFlags',self.getFlag('teams_defined'))

    @abstractmethod
    def initialise(self):
        """Initialisation method to be implemented in the child class. Inside this method full state definition have to be implemented."""
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    def _getFlagsDbRecord(self) -> Optional[Dict[str,Any]]:
        _rec=self.systemController.dbControl.getOneRecord(self.__class__,1)
        if _rec!=None:
            return { x.name:getattr(_rec,x.name) for x in fields(_rec) if x.name in self.flags }
        return None

    def _genFlagsDbRecord(self):
        _stateMachineObj=self.__class__()
        for name,flag in self.flags.items():
            if flag.serialisable:
                setattr(_stateMachineObj,flag.name,flag.value)
        self.systemController.getDb().setPrimaryKey(_stateMachineObj,1)
        return _stateMachineObj

    def setFlag(self,name,value,save=True) -> bool:
        _isSerialisable=False
        if name in self.flags:
            self.flags[name].value=value
            _isSerialisable=self.flags[name].serialisable
            if save and _isSerialisable:
                self.getSystemController().getDb().updateDataInDb(self.__class__,self._genFlagsDbRecord(),1)
        else:
            raise ExceptionStateMachine(f'setFlag error: flag {name} not found')
        return _isSerialisable
        
    def setFlags(self,flags:Dict[str,Any],save=True):
        _isSerialisable=False
        for name,value in flags.items():
            _isSerialisable=max(_isSerialisable,self.setFlag(name,value,False))
        if _isSerialisable and save:
            self.getSystemController().getDb().updateDataInDb(self.__class__,self._genFlagsDbRecord(),1)

    def saveCurrentFlagsToDb(self):
        self.getSystemController().getDb().updateDataInDb(self.__class__,self._genFlagsDbRecord(),1)
        
    def getFlag(self,name:str,flagsDbRecord:Optional[Dict[str,Any]]=None) -> Any:
        if name in self.flags:
            _f=self.flags[name] if name in self.flags else None
            if _f==None:
                raise ExceptionStateMachine(f"getFlag error: no flag {name} found")
            if _f.isCallable:
                self.setFlag(name,_f.call(),False)
                return self.flags[name].value
            elif _f.serialisable:
                _data=self._getFlagsDbRecord() if flagsDbRecord is None else flagsDbRecord
                if _data==None:
                    return _f.default
                else:
                    _value=_data[name] if name in _data else None
                    if _value==None:
                        return _f.default
                    if _value!=_f.value:
                        # self.setFlag(name,_value,False)
                        self.flags[name].value=_value
                    return _value
            else:
                return self.flags[name].value
        else:
            raise ExceptionStateMachine(f'getFlag error: flag {name} not found')

    def getFlags(self) -> Dict[str,Any]:
        _ret={}
        _dbRecord=None
        if self.flagsIsSerialisable:
            _dbRecord=self._getFlagsDbRecord()
        for name,flag in self.flags.items():
            _ret[name]=self.getFlag(name,_dbRecord)
        return _ret

    def addFlag(self, flag:Flag):
        if not flag.name in self.flags:
            self.flags[flag.name]=flag
            self.flagsIsSerialisable=max(self.flagsIsSerialisable,flag.serialisable)
            self.flags[flag.name].setSM(self)
        return self.flags[flag.name]
            
    def addStatesByObjs(self, *stateArgs:State) -> List[State]:
        _retStateList:List[State]=[]
        if len(stateArgs)==0:
            raise ExceptionStateMachine('StateMachine.addStatesByObjs error: stateArgs is empty')
        else:
            for state in stateArgs:
                if not state.name in self.states:
                    _retStateList.append(state)
                    self.states[state.name]=state
                    state.setSM(self)
                else:
                    raise ExceptionStateMachine("StateMachine.addStatesByObjs error: '{state.name}' duplicated")
        return _retStateList

    def addState(self, state:State) -> State:
        if not state.name in self.states:
            self.states[state.name]=state
            state.setSM(self)
        else:
            raise ExceptionStateMachine("StateMachine.addState error: '{state.name}' duplicated")
        return self.states[state.name]
    
    def getState(self, name:str) -> State:
        if name in self.states:
            return self.states[name]
        raise ExceptionStateMachine("StateMachine.getState error: state '{name}' not found")

    def addFlagsByObjs(self, *flagsArgs:Flag) -> List[Flag]:
        _retFlagsList:List[Flag]=[]
        if len(flagsArgs)==0:
            raise ExceptionStateMachine('StateMachine.addFlagsByObjs error: flagsArgs is empty')
        else:
            for flag in flagsArgs:
                if not flag.name in self.flags:
                    _retFlagsList.append(flag)
                    self.flags[flag.name]=flag
                    self.flagsIsSerialisable=max(self.flagsIsSerialisable,flag.serialisable)
                    self.flags[flag.name].setSM(self)
        return _retFlagsList

    def getDefaultState(self) -> State:
        _startState:Optional[State]=None
        for name,state in self.states.items():
            if state.default:
                _startState=state
                break
        if _startState is None:
            raise ExceptionStateMachine('StateMachine.start error: not default State found')
        return _startState

    def start(self):
        _startState=self.getDefaultState()
        _startState.start()
        # _startState:Optional[State]=None
        # for name,state in self.states.items():
        #     if state.default:
        #         _startState=state
        #         break
        # if _startState is None:
        #     raise ExceptionStateMachine('StateMachine.start error: not default State found')
        
        # # start the default state:
        # _startState.start()

    def startState(self,stateName:str):
        if stateName not in self.states:
            raise ExceptionStateMachine(f'StateMachine.startState error: cannot find {stateName} state.')
        self.states[stateName].start()


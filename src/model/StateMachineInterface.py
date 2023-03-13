from __future__ import annotations
from typing import Dict,Optional,List,Union,Callable,Any
from abc import abstractmethod
# from SystemControllerAbstract import SystemControllerAbstract
# exception related to StateMachine class
class ExceptionStateMachine(Exception):
    def __init__(self, message='StateMachine Exception'):
        super().__init__(f"ERROR(StateMachine): {message}")

class Flag:
    def __init__(self, name:str, type_, default=None, call:Optional[Callable[[Any],Any]]=None, serialisable:bool=False):
        self.name=name
        self.default=default
        self.value:type_=default
        if callable(call):
            self.isCallable=True
            self.call_fun=call
        else:
            self.isCallable=False
        self.serialisable=serialisable

    def call(self):
        return self.call_fun(self.getSM().getSystemController())
    
    def setSM(self, sm):
        self.sm=sm

    def getSM(self):
        return self.sm
    
class Transition:
    def __init__(self,srcState:State,eventName:str,dstState:State,
                 beforeFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True,
                 beforeChange:Optional[Union[List[Callable[[State,StateMachineInterface],bool]],Callable[[State,StateMachineInterface],bool]]]=lambda st,sm:True,
                 transitionTo:Optional[State]=None,
                 afterFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True):

        self.srcState=srcState
        self.dstState=dstState
        self.eventName=eventName
        self.beforeFlags=beforeFlags if type(beforeFlags)==list else [beforeFlags]
        self.beforeChange=beforeChange if type(beforeChange)==list else [beforeChange]
        self.transitionTo=transitionTo
        self.afterFlags=afterFlags if type(afterFlags)==list else [afterFlags]
        self.cond:Callable[[Dict[str,Flag]],bool]=lambda _:True

    def getST(self):
        return self.srcState

    def condFlags(self, call:Callable[[Dict[str,Any]],bool]):
        self.cond=call

    def checkCondition(self):
        if callable(self.cond) and not self.cond(self.getST().getSM().getFlags()):
            return False
        return True

class State:
    def __init__(self, name:str='',fun:Callable=lambda __:print("State method started"),default:bool=False):
        self.name=name
        self.fun=fun
        self.dstState:Optional[State]=None
        self.transitions:List[Transition]=[]
        self.default=default
        self.data=None

    def setSM(self, sm):
        self.sm=sm

    def getSM(self):
        return self.sm

    def setTransition(self, *args, **kwargs):
        self.transitions.append(Transition(self,*args,**kwargs))
        return self.transitions[-1]
    
    def _genFun(self,state,transitionTo=None,previousState=None):
        _start=state.start
        # state.setPreviousState(previousState)
        if transitionTo==None:
            _fun=lambda *args,**kwargs:_start(*args,**kwargs,previousState=previousState)
        else:
            _fun=lambda *args,**kwargs:_start(*args,**kwargs,transitionTo=transitionTo,previousState=previousState)
        return _fun
    
    # def setPreviousState(self,previousState):
    #     self.previous=previousState

    def getActions(self):
        data=self.data
        embedded=True
        _actions:Dict[str,Callable]={}
        for t in self.transitions:
            _state=t.dstState if isinstance(t.dstState,State) else t.dstState() if callable(t.dstState) else None
            if _state==None:
                raise ExceptionStateMachine(f'getActions error: cannot set _state for action definition in {self.name}')
            if t.checkCondition():
                _actions=_actions|{t.eventName:self._genFun(_state,t.transitionTo,previousState=self)}
        return data,_actions,embedded

    def previous(self,*args,**kwargs) -> Any:
        if isinstance(self.previousState,State):
            return self.previousState
        else:
            return self.defaultState()

    def defaultState(self) -> Any:
        return self.getSM().getDefaultState()

    def start(self,data=None,previousState=None,*args,**kwargs):
        self.previousState=previousState if previousState!=None else self.defaultState
        print('state.start:',self.name)
        _data,_actions,_embedded=self.getActions()
        actions=kwargs.get('actions') if 'actions' in kwargs else _actions
        embedded=kwargs.get('embedded') if 'embedded' in kwargs else _embedded
        data=data if data!=None else _data
        transitionTo=kwargs.get('transitionTo') if 'transitionTo' in kwargs else None
        print('state.start params:',self.name,data,actions,embedded)
        returnFlags={'transitionTo':transitionTo,'data':None}
        _dataRet=self.fun(data,actions,embedded,returnFlags=returnFlags)
        _returnFlags_data=returnFlags['data'] if 'data' in returnFlags else None
        _returnFlags_transitionTo=self.getSM().states[returnFlags['transitionTo']] if ('transitionTo' in returnFlags and returnFlags['transitionTo'] in self.getSM().states) else None
        if (type(_dataRet)==bool and _dataRet) or ((type(_dataRet)==dict or type(_dataRet)==list or type(_dataRet)==str) and len(_dataRet)!=0) and _dataRet!=None:
            if _returnFlags_transitionTo!=None:
                _returnFlags_transitionTo.start(_returnFlags_data)
            elif transitionTo!=None:
                transitionTo.start(_dataRet)

class StateMachineInterface:

    @abstractmethod
    def setSystemController(self,systemController):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def getSystemController(self):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def initialiseFlags(self):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def initialise(self):
        """Initialisation method to be implemented in the child class. Inside this method full state definition have to be implemented."""
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def _getFlagsDbRecord(self):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore        

    @abstractmethod
    def setFlag(self,name,value,save=True) -> bool:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore
        
    @abstractmethod
    def setFlags(self,flags:Dict[str,Any],save=True):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod        
    def getFlag(self,name) -> Any:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def getFlags(self):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def addFlag(self, flag:Flag):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod            
    def addStatesByObjs(self, *stateArgs:State) -> List[State]:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def addState(self, state:State) -> State:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def getState(self, name:str) -> State:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod
    def addFlagsByObjs(self, *flagsArgs:Flag) -> List[Flag]:
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod    
    def start(self):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    @abstractmethod    
    def startState(self,stateName:str):
        raise ExceptionStateMachine(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

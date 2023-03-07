from __future__ import annotations
from abc import abstractmethod
from typing import List,Dict,Any,Optional,Union,Callable
from AccountRights import AccountRights

# exception related to StateMachine class
class ExceptionStateMachine(Exception):
    def __init__(self, message='StateMachine Exception'):
        super().__init__(f"ERROR(StateMachine): {message}")

class Flag:
    def __init__(self, name:str, type_, startingValue=None):
        self.name=name
        self.value:type_=startingValue

    def setSM(self, sm):
        self.sm=sm

    def getSM(self):
        return self.sm

class Event:
    def __init__(self, name:str):
        self.name=name

    def setSM(self, sm):
        self.sm=sm

    def getSM(self):
        return self.sm
    
class Transition:
    def __init__(self,dstState:State,event:Callable[[State,StateMachine],bool]=lambda st,sm:True,
                 beforeFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True,
                 beforeChange:Optional[Union[List[Callable[[State,StateMachine],bool]],Callable[[State,StateMachine],bool]]]=lambda st,sm:True,
                 afterChange:Optional[Union[List[Callable[[State,StateMachine],bool]],Callable[[State,StateMachine],bool]]]=lambda st,sm:True,
                 afterFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True):

        self.dstState=dstState
        self.beforeFlags=beforeFlags if type(beforeFlags)==list else [beforeFlags]
        self.beforeChange=beforeChange if type(beforeChange)==list else [beforeChange]
        self.afterChange=afterChange if type(afterChange)==list else [afterChange]
        self.afterFlags=afterFlags if type(afterFlags)==list else [afterFlags]

class State:
    def __init__(self, name:str='',fun:Callable[[*Any],Optional[bool]]=lambda __:print("State method started"),default:bool=False):
        self.name=name
        self.fun=fun
        self.dstState:Optional[State]=None
        self.transitions:Dict[str,Transition]={}
        self.default=default

    def setSM(self, sm):
        self.sm=sm

    def getSM(self):
        return self.sm
    
    def transition(self, dstState:State,
            event:Callable[[State,StateMachine],bool]=lambda st,sm:True,
            beforeFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True,
            beforeChange:Optional[Union[List[Callable[[State,StateMachine],bool]],Callable[[State,StateMachine],bool]]]=lambda st,sm:True,
            afterChange:Optional[Union[List[Callable[[State,StateMachine],bool]],Callable[[State,StateMachine],bool]]]=lambda st,sm:True,
            afterFlags:Optional[Union[List[Flag],Callable[[Dict[str,Flag]],bool]]]=lambda _:True):
        
        if dstState.name in self.transitions:
            raise Exception(f"State.transition error: '{dstState.name}' already defined")
        self.transitions[dstState.name]=Transition(dstState,event,beforeFlags,beforeChange,afterChange,afterFlags)

class StateMachine:
    def __init__(self,systemController=None):
        self.states:Dict[str,State]={}
        self.flags:Dict[str,Flag]={}
        # self.transitions:Dict[str,Dict[Transition]={}
        self.events:Dict[str,Event]={}
        self.systemController=systemController

    def addFlag(self, flag:Flag):
        if not flag.name in self.flags:
            self.flags[flag.name]=flag
        return self.flags[flag.name]

    # def addStatesByNames(self,*stateNamesArgs:str) -> List[State]:
    #     _retStateList:List[State]=[]
    #     if len(stateNamesArgs)==0:
    #         raise ExceptionStateMachine('StateMachine.addStatesByNames error: stateArgs is empty')
    #     else:
    #         for name in stateNamesArgs:
    #             state=State(name)
    #             if not state.name in self.states:
    #                 _retStateList.append(state)
    #                 self.states[state.name]=state
    #                 state.setSM(self)
    #             else:
    #                 raise ExceptionStateMachine(f"StateMachine.addStatesByNames error: '{name}' dupllicated")
    #     return _retStateList
            
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
    
    def addFlagsByObjs(self, *flagsArgs:Flag) -> List[Flag]:
        _retFlagsList:List[Flag]=[]
        if len(flagsArgs)==0:
            raise ExceptionStateMachine('StateMachine.addFlagsByObjs error: flagsArgs is empty')
        else:
            for flag in flagsArgs:
                if not flag.name in self.flags:
                    _retFlagsList.append(flag)
                    self.flags[flag.name]=flag
        return _retFlagsList
    
    def start(self):
        _startState:Optional[State]=None
        for name,state in self.states.items():
            if state.default:
                _startState=state
                break
        if _startState is None:
            raise ExceptionStateMachine('StateMachine.start error: not default State found')
        
        # start the default state:
        _startState.fun(_startState.default)

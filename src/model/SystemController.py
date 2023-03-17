import inspect
from typing import Optional
from dataclasses import fields,asdict
from DBAbstractInterface import *
from UIAbstractInterface import *
from ApplicationState import *
from LoginStatus import *
from AppControlInterface import *
from FootballStateMachine import *
from SystemControllerAbstract import *
from ExceptionSystemController import *
from Teams import *
from Group import *
from Play import *
from GroupWithGamesScheduled import GroupWithGamesScheduled,PlayWithSchedule
from SchedulesWithPlay import SchedulesWithPlay

class SystemController(SystemControllerAbstract):
    """Main system controller for the application definition. The application instance could start after this controller will be initiated.
    """

    def __init__(self, dbControl: DBAbstractInterface, appControl: AppControlInterface, stateMachine: StateMachineInterface):
        SystemControllerAbstract.__init__(
            self, dbControl, appControl, stateMachine)

    def userMenu(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs):
        """Generates the application menu for user rights

        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        _fun: Optional[Callable] = None
        if self.stateMachine.getFlag('rights') == AccountRights.UserRights:
            _fun = self.appControl.userMenu
        elif self.stateMachine.getFlag('rights') == AccountRights.RefereeRights:
            _fun = self.appControl.refereeMenu
        else:
            self.appControl.showErrorMessage(
                'Rights error', 'You don\'t have permission to access menus')
            # come back to login to app state
            self.stateMachine.getState('loginToApp').start()
            return False
        _parent = self.appControl.getMainCanvasFrame()
        self.getApp().clearMainCanvas()
        self.getApp().getMainFrame().after(50, lambda: _fun(
            data, actions, self.appControl.getMainCanvasFrame()))

    def checkLogin(self, user: Users) -> bool:
        rights = self.dbControl.getRightsFromDb(user.login, user.password)
        if rights == AccountRights.NotLoggedIn:
            user.login = ""
            user.password = ""
            return False
        else:
            user.rights = rights
            self.stateMachine.setFlag("rights", rights)
            # self.loginStatus.loginStatus(user.login,user.rights)
            return True

    def refereeMenu(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs):
        """Generates the application menu for referee rights

        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        # this=self
        self.appControl.clearMainCanvas()
        _mainCanvasFrame = self.appControl.getMainCanvasFrame()
        _fun = self.appControl.refereeMenu
        self.appControl.getMainFrame().after(50, _fun(data, actions, _mainCanvasFrame))
        # self.switchMainCanvasView(self.appControl.refereeMenu,data,actions) #,self.appControl.getMainCanvasFrame())

    def saveAccount(self, data, *args, **kwargs):
        print('saveAccount:', data)
        if not 'rights' in data:
            if self.stateMachine.getFlag('empty_database'):
                data['rights'] = AccountRights.RefereeRights
            else:
                data['rights'] = AccountRights.UserRights
        user = Users().fromDict(data)
        print(user)
        if user.checkNewUserDataReferee(**data):
            if self.getDb().addDataToDb(Users, user):
                self.appControl.showInfoMessage(
                    'Serialisation', f'Congratulations! New account for {user.login} added.')
                return True
            else:
                self.appControl.showErrorMessage(
                    'Serialisation', 'Error in saving the data!')
        return False

    def saveTeam(self,data,*args,returnFlags,**kwargs) -> bool:
        """Transfer State, check new Team record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveTeam:', data, 'returnFlags', returnFlags)
        team = Teams().fromDict(data)
        print(team)
        if team.checkData(team):
            if self.getDb().addDataToDb(Teams, team):
                if self.getDb().getCountOfRecordsInTable(Teams) >= 12:
                    self.stateMachine.setFlag("teams_defined", True)
                    self.appControl.showInfoMessage(
                        'Congratulations!', f'Expected 12 tournament teams defined\nYou can run groups calculation now!')
                    returnFlags['transitionTo'] = 'userMenu'
                    returnFlags['data'] = None
                else:
                    self.appControl.showInfoMessage(
                        'Serialisation', f'Congratulations! New team for {team.name} added.')
                return True
            else:
                self.appControl.showErrorMessage(
                    'Serialisation', 'Error in saving the data!')
        return False
    
    def saveGamesData(self,data,*args,returnFlags,**kwargs) -> bool:
        """Transfer State, check new Play data record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveGamesData:',data)
        play=Play().fromDict(data)
        print(play)
        if play.checkData(play,forEdit=True):
            if self.getDb().updateDataInDb(Play,play,play.playID):
                if play.isPlayCompleted:
                    if not self.stateMachine.getFlag('groups_completed'): # groups phase
                        # add statistics to groups - if the game is completed:
                        group:List[Group]=self.getDb().getListOfRecords(Group,lambda x: play.team1ID in [x.team1ID,x.team2ID] or play.team2ID in [x.team1ID,x.team2ID] )
                        if len(group)!=1:
                            self.appControl.showErrorMessage('saveGamesData error','Data inconsistency, cannot find one group for play teams!')
                            raise ExceptionSystemController('saveGamesData error: data inconsistency, cannot find one group for play teams')

                        # team1
                        group[0].team1GoalsScored+=play.team1GoalsScored
                        group[0].team1GoalsMissed+=play.team1GoalsMissed
                        group[0].team1YellowCards+=play.team1YellowCards
                        group[0].team1Score+=3 if play.team1GoalsScored>play.team2GoalsScored else 1 if play.team1GoalsScored==play.team2GoalsScored else 0

                        # team2
                        group[0].team2GoalsScored+=play.team2GoalsScored
                        group[0].team2GoalsMissed+=play.team2GoalsMissed
                        group[0].team2YellowCards+=play.team2YellowCards
                        group[0].team2Score+=3 if play.team2GoalsScored>play.team1GoalsScored else 1 if play.team1GoalsScored==play.team2GoalsScored else 0

                        # save
                        self.getDb().updateDataInDb(Group,group[0],group[0].groupID)
                    else: # play-off phase
                        # schedule next play-off phase play
                        if not play.isFinal:
                            if not play.isSemiFinal:
                                if not play.is3rdPlaceFinal and not play.isFinal:
                                    _p:List[Play]=self.getDb().getListOfRecords(Play,lambda x: 0 in [x.team1ID,x.team2ID] and play.playID in [x.relevantScheduleIDForTeam1,x.relevantScheduleIDForTeam2] )
                                    if len(_p)!=1:
                                        self.appControl.showErrorMessage('saveGamesData error',f'Data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                        raise ExceptionSystemController(f'saveGamesData error: data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                    _winnerTeamID=play.team1ID if play.team1GoalsScored>play.team2GoalsScored else play.team2ID
                                    if _p[0].team1ID==0:
                                        _p[0].team1ID=_winnerTeamID
                                    elif _p[0].team2ID==0:
                                        _p[0].team2ID=_winnerTeamID
                                    else:
                                        self.appControl.showErrorMessage('saveGamesData error',f"Data inconsistency, can't set teamID ({_winnerTeamID}) to the next level as it's fulfiled already!")
                                        raise ExceptionSystemController(f"saveGamesData error: Data inconsistency, can't set teamID ({_winnerTeamID}) to the next level as it's fulfiled already!")
                                    
                                    # save
                                    self.getDb().updateDataInDb(Play,_p[0],_p[0].playID)

                            else: # play.isSemiFinal
                                _winnerTeamID=play.team1ID if play.team1GoalsScored>play.team2GoalsScored else play.team2ID
                                _loserTeamID=play.team1ID if play.team1GoalsScored<play.team2GoalsScored else play.team2ID

                                # 3rd place final - _p[0]
                                _p:List[Play]=self.getDb().getListOfRecords(Play,lambda x: x.is3rdPlaceFinal and 0 in [x.team1ID,x.team2ID] and play.playID in [x.relevantScheduleIDForTeam1,x.relevantScheduleIDForTeam2] )
                                if len(_p)!=1:
                                    self.appControl.showErrorMessage('saveGamesData error',f'Data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                    raise ExceptionSystemController(f'saveGamesData error: data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                if _p[0].team1ID==0:
                                    _p[0].team1ID=_loserTeamID
                                elif _p[0].team2ID==0:
                                    _p[0].team2ID=_loserTeamID
                                else:
                                    self.appControl.showErrorMessage('saveGamesData error',f"Data inconsistency, can't set teamID ({_loserTeamID}) to the next level as it's fulfiled already!")
                                    raise ExceptionSystemController(f"saveGamesData error: Data inconsistency, can't set teamID ({_loserTeamID}) to the next level as it's fulfiled already!")

                                # save
                                self.getDb().updateDataInDb(Play,_p[0],_p[0].playID)

                                # final - _p[1]
                                _p:List[Play]=self.getDb().getListOfRecords(Play,lambda x: x.isFinal and  0 in [x.team1ID,x.team2ID] and play.playID in [x.relevantScheduleIDForTeam1,x.relevantScheduleIDForTeam2] )
                                if len(_p)!=1:
                                    self.appControl.showErrorMessage('saveGamesData error',f'Data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                    raise ExceptionSystemController(f'saveGamesData error: data inconsistency, cannot find one next relative to play ({play.playID}) game record!')
                                if _p[0].team1ID==0:
                                    _p[0].team1ID=_winnerTeamID
                                elif _p[0].team2ID==0:
                                    _p[0].team2ID=_winnerTeamID
                                else:
                                    self.appControl.showErrorMessage('saveGamesData error',f"Data inconsistency, can't set teamID ({_winnerTeamID}) to the next level as it's fulfiled already!")
                                    raise ExceptionSystemController(f"saveGamesData error: Data inconsistency, can't set teamID ({_winnerTeamID}) to the next level as it's fulfiled already!")
                                
                                # save
                                self.getDb().updateDataInDb(Play,_p[0],_p[0].playID)
                
                # check how many incompleted plays left
                _playsLeft=self.getDb().getListOfRecords(Play,lambda x: not x.isPlayCompleted)
                if len(_playsLeft)==0:
                    if not self.stateMachine.getFlag('playoff_scheduled'):
                        self.stateMachine.setFlag('groups_completed',True)
                    else:
                        self.stateMachine.setFlag('tournament_completed',True)
                self.appControl.showInfoMessage('Serialisation',f'Congratulations! Game record successfuly edited.')
                return True
            else:
                self.appControl.showErrorMessage('Serialisation','Error in saving the data!')

        return False # False - prevent to further change view - will stay on list of teams to choose to edit next one

    def saveEditedTeam(self,data,*args,**kwargs):
        """Transfer State, check edited Team record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveTeam:', data)
        team = Teams().fromDict(data)
        print(team)
        if team.checkData(team, forEdit=True):
            if self.getDb().updateDataInDb(Teams, team, team.teamID):
                self.appControl.showInfoMessage(
                    'Serialisation', f'Congratulations! Team record successfuly edited.')
                return True
            else:
                self.appControl.showErrorMessage(
                    'Serialisation', 'Error in saving the data!')
        return False  # False - prevent to further change view - will stay on list of teams to choose to edit next one

    def saveUserRightChanges(self, data, *args, **kwargs):
        """Transfer State, check edited User record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new User object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveUser:', data)
        user = Users().fromDict(data)
        print(user)
        if user.checkRightsChange(user):
            if self.getDb().updateDataInDb(Users, user, user.userID):
                self.appControl.showInfoMessage(
                    'Serialisation', f'Congratulations! User record successfuly edited.')
                return True
            else:
                self.appControl.showErrorMessage(
                    'Serialisation', 'Error in saving the data!')
        return False  # False - prevent to further change view - will stay on list of teams to choose to edit next one

    def registerAccount(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs):
        """User of referee register account. For empty database tables firstly created account is always with highest referee rights.

        """
        data = Users()
        self.appControl.clearMainCanvas()
        if self.stateMachine.getFlag('rights') == AccountRights.RefereeRights:
            def _fun(): return self.appControl.refereeDialogForNewUser(
                data, actions, self.appControl.getMainCanvasFrame())
        else:
            def _fun(): return self.appControl.dialogForNewUser(
                data, actions, self.appControl.getMainCanvasFrame())
        self.appControl.getMainFrame().after(50, _fun)
        return True

    def defineTeam(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs) -> bool:
        """Define team. This method can be called only with referee rights account."""
        team = Teams()
        team.teamID = self.getDb().getMaxIdFromTable(Teams)+1
        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.dialogForNewTeam(
            team, actions, self.appControl.getMainCanvasFrame()))
        return True

    def refereeEditTeamDataList(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs) -> bool:
        """Creates list of Team records on screen with option to edit it."""
        team = Teams()
        teamsListDict: List[Dict[str, Any]] = [
            asdict(x) for x in self.getDb().getListOfRecords(Teams)]
        _headers = [
            ColumnStyle(self,'teamID','id',JustifyEnum.RIGHT,True),
            ColumnStyle(self,'name','name',JustifyEnum.LEFT)
        ]
        #team.getHeadersForTreeview()

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(
            Teams.__name__, _headers, teamsListDict, actions, self.getApp().getMainCanvasFrame()))

        return True

    def changeUserRightsList(self, data, actions: Dict[str, Callable], embedded: bool = False, *args, **kwargs) -> bool:
        """Creates list of User records on screen with option to edit it."""
        user = Users()
        usersListDict: List[Dict[str, Any]] = [
            asdict(x) for x in self.getDb().getListOfRecords(Users)]
        _headers = [
            ColumnStyle(self,'userID','id',JustifyEnum.RIGHT,True),
            ColumnStyle(self,'login','login',JustifyEnum.LEFT),
            ColumnStyle(self,'rights','rigths',JustifyEnum.LEFT)
        ]
        # for ind,user in enumerate(usersListDict):
        #     usersListDict[ind]={ k:v if k!='rights' else v.value for k,v in user.items() }
        # user.getHeadersForTreeview()

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(Users.__name__, _headers, usersListDict, actions, self.getApp().getMainCanvasFrame()))

        return True

    def changeUserRights(self, data, actions: Dict[str, Callable], parentFrame: Any = None, *args, **kwargs) -> bool:
        """Change the rights for specific users. This call should be transferred to the User.changeUserRights method"""
        print('data',data)
        user = Users().fromDict(data)
        return self.getApp().modalDialog('User edit', self.appControl.refereeDialogForUserRights, data, actions, parentFrame, lambda data: user.fromDict(data).checkRightsChange(user))

    def refereeEditTeamData(self, data, actions: Dict[str, Callable], parentFrame: Any = None, *args, **kwargs) -> bool:
        """Edit team data. This method can be called only with referee rights account."""
        team = Teams().fromDict(data)
        return self.getApp().modalDialog('Team edit', self.appControl.dialogForEditTeam, data, actions, parentFrame, lambda data: team.fromDict(data).checkData(team, forEdit=True))

    def clearForSchedule(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs) -> bool:
        _db = self.getDb()
        _app = self.getApp()
        _sm = self.stateMachine
        if self.getApp().createDialogYesNo('Clear database', 'Are you sure to clear Group Play and Schedules?'):
            _db.truncateTable(Group)
            _db.truncateTable(Play)
            _db.truncateTable(Schedule)
            _sm.setFlag('groups_defined', False)
            _sm.setFlag('groups_scheduled', False)
        return True

    def calculateGroupPhaseSchedule(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs) -> bool:
        """Calculate group phase schedule. This method can be called only with referee rights account.
        To calculate group phase schedule use the 'Calculate Group Phase Schedule' sequence diagram.
        When done correctly, in the database should be group records and every group phase games schedule saved.
        Controller is transfering this call to @Schedule.calculateGroupPhaseSchedule()

        References: 
            Group
            Schedule
            Schedule.calculateGroupPhaseSchedule()
        """
        _db=self.getDb()
        _app=self.getApp()
        _sm=self.stateMachine
        if self.getApp().createDialogYesNo('Scheduling group phase','Are you sure, you want to let the app randomly \ngenerate games play for group phase?\n\n(warning: it\'s the one way decision)'):
            # checks
            _teamsCount = _db.getListOfRecords(Teams)
            if len(_teamsCount) != 12:
                _app.showErrorMessage(
                    'Calculate group phase error', f'You cannot calculate group phase without 12 teams defined (there\'s {len(_teamsCount)} right now)')
                return False
            if len(_db.getListOfRecords(Group)) != 0:
                _app.showErrorMessage(
                    'Calculate group phase error', f'There are some records in Group table in the database.\nOperation forbidden.')
                return False
            # save the groups to the database
            _groups: List[List[int]
                          ] = self.generateRandomGroupPhasePlaySchedule()
            _groupCn = 1
            for teamNrList in _groups:
                group = Group()
                group.groupID = _groupCn
                group.groupName = f'Group {_groupCn}'
                _cn = 1
                for _teamID in teamNrList:
                    _fieldName = f'team{_cn}ID'
                    setattr(group, _fieldName, _teamID)
                    _cn += 1
                _db.addDataToDb(Group, group)
                _groupCn += 1
            # set the flag for the application (serialisable flags will be automatically saved to the database)
            _sm.setFlag('groups_defined', True)
            # calculate the schedule for games planned in each group
            g = Group()
            _schedules = self.generateSchedulesForGroupDefinition()
            for play in _schedules['play']:
                _db.addDataToDb(Play, play)
            for schedule in _schedules['schedule']:
                _db.addDataToDb(Schedule, schedule)
            # set the flag for the application (serialisable flags will be automatically saved to the database)
            _sm.setFlag('groups_scheduled', True)
            _app.showInfoMessage(
                'Success!', 'Groups phase schedule fully generated.\nYou can now start recording scores for games.')
        return True

    def calculatePlayoffPhaseSchedule(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs) -> bool:
        """Calculate playoff phase schedule only if the group phase is already calculated. 
        This method can be called only with referee rights account.
        To calculate playoff phase schedule use the 'Calculate Playoff Phase Schedule' sequence diagram.
        When done correctly, in the database should be every playoff game scheduled with NULL team1/2 ID's 
        but with virtual team1/2 completed for future games with unknown yes compatitors.
        Controller is transfering this call to @Schedule.calculatePlayoffPhaseSchedule()

        References: 
            Schedule
            Schedule.calculatePlayoffPhaseSchedule()
        """
        _db=self.getDb()
        _app=self.getApp()
        _sm=self.stateMachine
        if not self.getApp().createDialogYesNo('Scheduling play-off phase','Are you sure, you want to let the app randomly \ngenerate games play for play-off phase?\n\n(warning: it\'s the one way decision)'):
            return False
        # checks
        _fl=self.stateMachine.getFlags()
        if not _fl['groups_completed'] or _fl['playoff_scheduled'] or _fl['tournament_completed']:
            _app.showErrorMessage('Calculate play-off phase error',f'Current state of flags in the application are incorrect\n(groups_completed,playoff_scheduled,tournament_completed).\nOperation forbidden.')
            return False

        # TODO: additional fields: isQuarterFinal:bool, isSemiFinal:bool, is3rdPlaceFinal:bool, isFinal:bool
        # generate quarter-final 4 games / 8 teams -> add isQuarterFinal=True field
        # generate semi-final 2 games / 4 teams -> add isSemiFinal=True field
        # generate 3rdPlaceFinal 1 game / 2 teams -> add is3rdPlaceFinal=True field
        # generate final 1 game / 2 teams -> add isFinal=True field
        groups=_db.getListOfRecords(Group)
        _quarterFinalGames:List[List[int]]=self._generateQuarterFinalSchedule(groups)

        # save it and add schedule records
        _playMaxID=_db.getMaxIdFromTable(Play)+1
        _scheduleMaxID=_db.getMaxIdFromTable(Schedule)+1
        _date=datetime.now()+timedelta(days=2)
        _semiFinalGames:Dict[int,List[int]]={0:[0,0],1:[0,0]}
        _cn=0
        # quarter final matches
        for (t1,t2) in _quarterFinalGames:
            p=Play(playID=_playMaxID,team1ID=t1,team2ID=t2,isQuarterFinal=True,relevantScheduleIDForTeam1=0,relevantScheduleIDForTeam2=0)
            s=Schedule(scheduleID=_scheduleMaxID,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Afternoon)
            _db.addDataToDb(Play,p)
            _db.addDataToDb(Schedule,s)
            _playMaxID+=1
            _scheduleMaxID+=1
            _date+=timedelta(days=1)
            _semiFinalGames[int(_cn/2)][_cn%2]=p.playID
            _cn+=1
        # semi final matches
        _date+=timedelta(days=2)
        _finalGames:List=[0,0]
        _cn=1
        for i,players in _semiFinalGames.items():
            p=Play(playID=_playMaxID,team1ID=0,team2ID=0,isSemiFinal=True,relevantScheduleIDForTeam1=players[0],relevantScheduleIDForTeam2=players[1])
            s=Schedule(scheduleID=_scheduleMaxID,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Afternoon)
            _db.addDataToDb(Play,p)
            _db.addDataToDb(Schedule,s)
            _playMaxID+=1
            _scheduleMaxID+=1
            _date+=timedelta(days=1)
            _finalGames[int(_cn/2)]=p.playID
            _cn+=1
        # 3rd place match
        _date+=timedelta(days=2)
        p=Play(playID=_playMaxID,team1ID=0,team2ID=0,is3rdPlaceFinal=True,relevantScheduleIDForTeam1=_finalGames[0],relevantScheduleIDForTeam2=_finalGames[1])
        s=Schedule(scheduleID=_scheduleMaxID,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Afternoon)
        _db.addDataToDb(Play,p)
        _db.addDataToDb(Schedule,s)
        _playMaxID+=1
        _scheduleMaxID+=1
        _date+=timedelta(days=1)
        # final match
        p=Play(playID=_playMaxID,team1ID=0,team2ID=0,isFinal=True,relevantScheduleIDForTeam1=_finalGames[0],relevantScheduleIDForTeam2=_finalGames[1])
        s=Schedule(scheduleID=_scheduleMaxID,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Afternoon)
        _db.addDataToDb(Play,p)
        _db.addDataToDb(Schedule,s)

        # set the flag for the application (serialisable flags will be automatically saved to the database)
        _sm.setFlag('playoff_scheduled',True)
        _app.showInfoMessage('Success!','Play-off phase schedule fully generated.\nYou can now start recording scores for games.')
        return True

    def recordGamesDataList(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,returnFlags,**kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        play=Play()
        playListDict:List[Play]=self.getDb().getListOfRecords(Play,lambda x: not x.isPlayCompleted)

        if len(playListDict)==0: # no more plays incomplete
            returnFlags['transitionTo']='userMenu' # go back to userMenu state
            returnFlags['data']=None
            return True

        _data:List[Dict[str,Any]]=[]
        _headers=[
            ColumnStyle(self,'playID','play',JustifyEnum.RIGHT,True),
            ColumnStyle(self,'date','date',JustifyEnum.LEFT),
            ColumnStyle(self,'team1ID','team 1',JustifyEnum.RIGHT),
            ColumnStyle(self,'team1_name','name',JustifyEnum.LEFT),
            ColumnStyle(self,'team1GoalsScored','goals',JustifyEnum.RIGHT),
            ColumnStyle(self,'team1YellowCards','yellow cards',JustifyEnum.RIGHT),
            ColumnStyle(self,'team2ID','team 2',JustifyEnum.RIGHT),
            ColumnStyle(self,'team2_name','name',JustifyEnum.LEFT),
            ColumnStyle(self,'team2GoalsScored','goals',JustifyEnum.RIGHT),
            ColumnStyle(self,'team2YellowCards','yellow cards',JustifyEnum.RIGHT)
            ]

        for i,play in enumerate(playListDict):
            # additional relationas objects added to record:
            _team1Obj=self.getDb().getListOfRecords(Teams,lambda x: x.teamID==play.team1ID)[0] if play.team1ID>0 else None # type: ignore
            _team2Obj=self.getDb().getListOfRecords(Teams,lambda x: x.teamID==play.team2ID)[0] if play.team2ID>0 else None # type: ignore
            _scheduleObj=self.getDb().getListOfRecords(Schedule,lambda x: x.playID==play.playID)[0] # type: ignore
            _data.append(asdict(play)|{
                'date':f"{_scheduleObj.date.strftime('%Y-%m-%d')} {_scheduleObj.timeOfDay.value}",
                'team1_name': _team1Obj.name if _team1Obj!=None else f"<play {play.relevantScheduleIDForTeam1}>",
                'team2_name': _team2Obj.name if _team2Obj!=None else f"<play {play.relevantScheduleIDForTeam2}>",
            }) #type: ignore

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(Play.__name__,_headers,_data,actions,self.getApp().getMainCanvasFrame())) # type: ignore
        return True

    def recordGamesData(self, data, actions: Dict[str, Callable], parentFrame: Any = None, *args, **kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        """Creates list of Team records on screen with option to edit it."""
        """Edit team data. This method can be called only with referee rights account."""
        print('play',data)
        play=Play().fromDict(data)
        if not (play.team1ID>0 and play.team2ID>0):
            self.getApp().showErrorMessage('Record game data error!','You cannot edit game data before both teams will be set.')
            return False
        return self.getApp().modalDialog('Play edit',self.appControl.dialogForEditPlay,data,actions,parentFrame,lambda data: play.fromDict(data).checkData(play,forEdit=True))

    def refereeResetApplicationData(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs) -> bool:
        """Reset application data. This method can be called only with referee rights account.
        After this operation is completed, the database is completely cleared and the application works again like during the first run.
        """
        if self.getApp().createDialogYesNo('Reset application data','Are you sure, you want to reset entire database of application?\n\n(warning: it\'s the one way decision)'):
            self.getDb().resetAllDataInDb(FootballStateMachine)
            self.stateMachine.setFlagsDefault()
        return True

    def loginToApp(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs):
        """Classic login/password authentication. After the data are taken, the application have to check with database if access should be granted.
        Additionally, the application keep the rights level for the account (user or referee rights account)

        - create new dialog window for getting: login, password (refer to UIAbstractInterface create new dialog)
        - get rights from database (refer to DBAbstractInterface get rights from db) and show error message if access isn't granted then go back to login dialog
        - update the login status (refer to SystemController loginStatus)
        - start the application main screen with features access depending on the account rights
        """

        print("loginToApp dialog here")
        # print("actions",actions)
        data = Users()
        if embedded:
            self.appControl.clearMainCanvas()
            self.appControl.getMainFrame().after(50,
                                                 lambda: self.appControl.dialogForAppLoginOrRegister(data, actions, self.appControl.getMainCanvasFrame()))  # type: ignore
        else:
            pass

        # self.appControl.dialogForAppLoginOrRegister(user,{"ok":lambda})
        # newUserFrame:tk.Frame = tk.Frame(parentFrame)
        # newUserFrame.grid()

        # _user=Users() # empty users instance for holding the data
        # if not embeded:
        #     if self.getApp().dialogForNewUser(_user,self.getApp().getMainFrame()):
        #         self.loginStatus.loginStatus(_user.login,self.getDb().getRightsFromDb(_user.login,_user.password))
        # else:
        #     self.getApp().dialogForNewUser(_user)
        return True

    def logoutFromAccount(self, data, actions: Dict[str, Callable], embedded: bool = True, *args, **kwargs):
        """Logout from the current account.
        """

        self.stateMachine.setFlag('rights', AccountRights.NotLoggedIn)
        return True

    def showMatchOrderGroupsStatus(self,data:List[GroupWithGamesScheduled],actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """User or referee both can watch the current groups status of teams.
            data: Group records list, extended by the field: 
                'plays' - list of plays for the group, which is extended by the field:
                    'schedule' - schedule record related to the current play record
        """
        data=[]
        _groups=self.getDb().getListOfRecords(Group)
        for g in _groups:
            _gs=GroupWithGamesScheduled().fromDict(asdict(g))
            data.append(_gs)
        for index,group in enumerate(data):
            _playList=self.getDb().getListOfRecords(Play,lambda x: x.team1ID in [group.team1ID,group.team2ID,group.team3ID])
            _cn=1
            for p in _playList:
                _ps=PlayWithSchedule().fromDict(asdict(p))
                _ps.schedule=self.getDb().getListOfRecords(Schedule,lambda x: x.playID==_ps.playID)[0]
                setattr(data[index],f'play{_cn}',_ps)
                _cn+=1
        print('showMatchOrderGroupsStatus DATA SENT:')
        print(data)
        print()
        self.getApp().clearMainCanvas()
        self.getApp().getMainFrame().after(50, lambda: self.getApp().displayStatisticsForGroupAndItsGamesScheduled(data,actions,self.appControl.getMainCanvasFrame()))
        return True

    def showMatchOrderPlayOffTree(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """User or referee both can watch the current play-off-tree status of teams."""

        data=[]
        _schedules=self.getDb().getListOfRecords(Schedule)
        for g in _schedules:
            _pl=self.getDb().getListOfRecords(Play,lambda x: x.playID==g.playID)[0]
            _t1=self.getDb().getOneRecord(Teams,_pl.team1ID)
            _t2=self.getDb().getOneRecord(Teams,_pl.team2ID)
            _gs=SchedulesWithPlay(g,_pl,_t1,_t2)
            data.append(_gs)
        print('showMatchOrderPlayOffTree DATA SENT:')
        print(data)
        print()
        self.getApp().clearMainCanvas()
        self.getApp().getMainFrame().after(50, lambda: self.getApp().displayStatisticsForPlayoffScheduledGames(data,actions,self.appControl.getMainCanvasFrame()))
        return True

    def teamsAmountLessThen16(self):
        """Return True if the saved number of teams in the database is less then 16"""
        raise ExceptionUIAbstractInterface(
            f"no {inspect.currentframe().f_code.co_name} method defined")  # type: ignore

    def getRightsFromDb(self, data, *args, **kwargs):
        login = data['login'] if 'login' in data else ''
        password = data['password'] if 'password' in data else ''
        rights = self.dbControl.getRightsFromDb(login, password)
        print('login', login, 'password', password, 'rights', rights)
        if rights == AccountRights.NotLoggedIn:
            self.appControl.showErrorMessage(
                'Login', f'Cannot find your account {login} for given login data.')
            return False
        self.stateMachine.setFlag('rights', rights)
        return True

    def _randomTeamFromList(self, teamList: List[int]) -> int:
        _ret = random.choice(teamList)
        teamList.remove(_ret)
        return _ret

    def generateRandomGroupPhasePlaySchedule(self) -> List[List[int]]:
        """Generates a random play schedule for entire tournament after is checked if expected amount of teams is defined.
        Method uses helpers: generateRandomTeamsList(), prepareGroupPhaseData(), preparePlayoffPhaseData().
        Call saveRelativeScheculeRecords() when the tournament schedule is calculated.
        Sets ApplicationState.setIsScheduled() after full schedule is saved."""
        _ret: List[List[int]] = []

        _db = self.getDb()
        _teamsNrs = [*range(1, 13)]
        for _groupCn in range(1, 5):
            _ret.append([self._randomTeamFromList(_teamsNrs), self._randomTeamFromList(
                _teamsNrs), self._randomTeamFromList(_teamsNrs)])
        return _ret

    def generateSchedulesForGroupDefinition(self) -> Dict[str, List[Union[Play, Schedule]]]:
        _ret: Dict[str, List[Union[Play, Schedule]]] = {
            "play": [], "schedule": []}
        _scheduleCn = 1
        _playCn = 1
        _groups: Dict[int, List[int]] = {}
        _groupRecs = self.getDb().getListOfRecords(Group)
        _date = datetime.now()
        for group in _groupRecs:
            # team1 - team2
            p=Play(playID=_playCn,team1ID=group.team1ID,team2ID=group.team2ID,isGroupPhase=True)
            _playCn+=1
            s=Schedule(scheduleID=_scheduleCn,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Morning,isGroupPhase=True)
            _scheduleCn+=1
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            # team1 - team3
            p=Play(playID=_playCn,team1ID=group.team1ID,team2ID=group.team3ID,isGroupPhase=True)
            _playCn+=1
            s=Schedule(scheduleID=_scheduleCn,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Noon,isGroupPhase=True)
            _scheduleCn+=1
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            # team2 - team3
            p=Play(playID=_playCn,team1ID=group.team2ID,team2ID=group.team3ID,isGroupPhase=True)
            _playCn+=1
            s=Schedule(scheduleID=_scheduleCn,playID=p.playID,date=_date,timeOfDay=TimeOfDay.Afternoon,isGroupPhase=True)
            _scheduleCn+=1
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            _date += timedelta(days=1)

        return _ret

    def _generateQuarterFinalSchedule(self,groups) -> List[List[int]]:
        """Generates schedule for 4 plays with pair of one winner of a group and one 2nd place winner of a group.

        Args:
            groups (Group): list of all groups obj from the database
        """
        _ret:List[List[int]]=[[0,0],[0,0],[0,0],[0,0]]

        _winners=[ g.getGroupWinner() for g in groups ]
        _secondPlaces=[ g.getGroupSecondPlace() for g in groups ]

        _ret[0][0]=self._randomTeamFromList(_winners)
        _ret[0][1]=self._randomTeamFromList(_secondPlaces)

        _ret[1][0]=self._randomTeamFromList(_winners)
        _ret[1][1]=self._randomTeamFromList(_secondPlaces)

        _ret[2][0]=self._randomTeamFromList(_winners)
        _ret[2][1]=self._randomTeamFromList(_secondPlaces)

        _ret[3][0]=self._randomTeamFromList(_winners)
        _ret[3][1]=self._randomTeamFromList(_secondPlaces)

        return _ret

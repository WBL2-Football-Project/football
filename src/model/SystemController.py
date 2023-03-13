import inspect
from typing import Optional
from dataclasses import asdict
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

class SystemController(SystemControllerAbstract):
    """Main system controller for the application definition. The application instance could start after this controller will be initiated.
    """

    def __init__(self, dbControl: DBAbstractInterface, appControl: AppControlInterface, stateMachine: StateMachineInterface):
        SystemControllerAbstract.__init__(self,dbControl,appControl,stateMachine)

    def userMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Generates the application menu for user rights

        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        _fun:Optional[Callable]=None
        if self.stateMachine.getFlag('rights')==AccountRights.UserRights:
            _fun=self.appControl.userMenu
        elif self.stateMachine.getFlag('rights')==AccountRights.RefereeRights:
            _fun=self.appControl.refereeMenu
        else:
            self.appControl.showErrorMessage('Rights error','You don\'t have permission to access menus')
            self.stateMachine.getState('loginToApp').start() # come back to login to app state
            return False
        _parent=self.appControl.getMainCanvasFrame()
        self.getApp().clearMainCanvas()
        self.getApp().getMainFrame().after(50, lambda: _fun(data,actions,self.appControl.getMainCanvasFrame()))

    def checkLogin(self,user:Users) -> bool:
        rights=self.dbControl.getRightsFromDb(user.login,user.password)
        if rights==AccountRights.NotLoggedIn:
            user.login=""
            user.password=""
            return False
        else:
            user.rights=rights
            self.stateMachine.setFlag("rights",rights)
            # self.loginStatus.loginStatus(user.login,user.rights)
            return True

    def refereeMenu(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """Generates the application menu for referee rights

        Args:
            embedded (bool, optional): True shows dialog in modal window. Defaults to False.
        """
        # this=self
        self.appControl.clearMainCanvas()
        _mainCanvasFrame=self.appControl.getMainCanvasFrame()
        _fun=self.appControl.refereeMenu
        self.appControl.getMainFrame().after(50,_fun(data,actions,_mainCanvasFrame))
        # self.switchMainCanvasView(self.appControl.refereeMenu,data,actions) #,self.appControl.getMainCanvasFrame())

    def saveAccount(self,data,*args,**kwargs):
        print('saveAccount:',data)
        if not 'rights' in data:
            if self.stateMachine.getFlag('empty_database'):
                data['rights'] = AccountRights.RefereeRights
            else:
                data['rights'] = AccountRights.UserRights
        user=Users().fromDict(data)
        print(user)
        if user.checkNewUserDataReferee(**data):
            if self.getDb().addDataToDb(Users,user):
                self.appControl.showInfoMessage('Serialisation',f'Congratulations! New account for {user.login} added.')
                return True
            else:
                self.appControl.showErrorMessage('Serialisation','Error in saving the data!')
        return False

    def saveTeam(self,data,*args,returnFlags,**kwargs):
        """Transfer State, check new Team record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveTeam:',data,'returnFlags',returnFlags)
        team=Teams().fromDict(data)
        print(team)
        if team.checkData(team):
            if self.getDb().addDataToDb(Teams,team):
                if self.getDb().getCountOfRecordsInTable(Teams)>=12:
                    self.stateMachine.setFlag("teams_defined",True)
                    self.appControl.showInfoMessage('Congratulations!',f'Expected 12 tournament teams defined\nYou can run groups calculation now!')
                    returnFlags['transitionTo']='userMenu'
                    returnFlags['data']=None
                else:
                    self.appControl.showInfoMessage('Serialisation',f'Congratulations! New team for {team.name} added.')
                return True
            else:
                self.appControl.showErrorMessage('Serialisation','Error in saving the data!')
        return False

    def saveEditedTeam(self,data,*args,**kwargs):
        """Transfer State, check edited Team record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new Team object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveTeam:',data)
        team=Teams().fromDict(data)
        print(team)
        if team.checkData(team,forEdit=True):
            if self.getDb().updateDataInDb(Teams,team,team.teamID):
                self.appControl.showInfoMessage('Serialisation',f'Congratulations! Team record successfuly edited.')
                return True
            else:
                self.appControl.showErrorMessage('Serialisation','Error in saving the data!')
        return False # False - prevent to further change view - will stay on list of teams to choose to edit next one

    def saveUserRightChanges(self,data,*args,**kwargs):
        """Transfer State, check edited User record and save it to the database

        Args:
            data (Dict[str,Any]): data dict for new User object

        Returns:
            bool: True if successful, False otherwise
        """
        print('saveUser:',data)
        user=Users().fromDict(data)
        print(user)
        if user.checkRightsChange(user):
            if self.getDb().updateDataInDb(Users,user,user.userID):
                self.appControl.showInfoMessage('Serialisation',f'Congratulations! User record successfuly edited.')
                return True
            else:
                self.appControl.showErrorMessage('Serialisation','Error in saving the data!')
        return False # False - prevent to further change view - will stay on list of teams to choose to edit next one
    
    def registerAccount(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs):
        """User of referee register account. For empty database tables firstly created account is always with highest referee rights.

        """
        data=Users()
        self.appControl.clearMainCanvas()
        if self.stateMachine.getFlag('rights') == AccountRights.RefereeRights:
            _fun=lambda: self.appControl.refereeDialogForNewUser(data,actions,self.appControl.getMainCanvasFrame())
        else:
            _fun=lambda: self.appControl.dialogForNewUser(data,actions,self.appControl.getMainCanvasFrame())
        self.appControl.getMainFrame().after(50, _fun)
        return True

    def defineTeam(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs) -> bool:
        """Define team. This method can be called only with referee rights account."""
        team=Teams()
        team.teamID=self.getDb().getMaxIdFromTable(Teams)+1
        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.dialogForNewTeam(team,actions,self.appControl.getMainCanvasFrame()))
        return True

    def refereeEditTeamDataList(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs) -> bool:
        """Creates list of Team records on screen with option to edit it."""
        team=Teams()
        teamsListDict:List[Dict[str,Any]]=[ asdict(x) for x in self.getDb().getListOfRecords(Teams) ]
        _headers=team.getHeadersForTreeview()

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(Teams.__name__,_headers,teamsListDict,actions,self.getApp().getMainCanvasFrame()))
        
        return True

    def changeUserRightsList(self,data,actions:Dict[str,Callable],embedded:bool=False,*args,**kwargs) -> bool:
        """Creates list of User records on screen with option to edit it."""
        user=Users()
        usersListDict:List[Dict[str,Any]]=[ asdict(x) for x in self.getDb().getListOfRecords(Users) ]
        _headers=user.getHeadersForTreeview()

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(Users.__name__,_headers,usersListDict,actions,self.getApp().getMainCanvasFrame()))
        
        return True

    def refereeEditTeamData(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Edit team data. This method can be called only with referee rights account."""
        team=Teams().fromDict(data)
        return self.getApp().modalDialog('Team edit',self.appControl.dialogForEditTeam,data,actions,parentFrame,lambda data: team.fromDict(data).checkData(team,forEdit=True))

    def clearForSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        _db=self.getDb()
        _app=self.getApp()
        _sm=self.stateMachine
        if self.getApp().createDialogYesNo('Clear database','Are you sure to clear Group Play and Schedules?'):
            _db.truncateTable(Group)
            _db.truncateTable(Play)
            _db.truncateTable(Schedule)
            _sm.setFlag('groups_defined',False)
            _sm.setFlag('groups_scheduled',False)
        return True

    def calculateGroupPhaseSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
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
        if self.getApp().createDialogYesNo('Clear database','Are you sure to clear Group Play and Schedules?'):
            _db.truncateTable(Group)
            _db.truncateTable(Play)
            _db.truncateTable(Schedule)
            _sm.setFlag('groups_defined',True)
            _sm.setFlag('groups_scheduled',True)
        if self.getApp().createDialogYesNo('Scheduling group phase','Are you sure, you want to let the app randomly \ngenerate games play for group phase?\n\n(warning: it\'s the one way decision)'):
            # checks
            _teamsCount=_db.getListOfRecords(Teams)
            if len(_teamsCount)!=12:
                _app.showErrorMessage('Calculate group phase error',f'You cannot calculate group phase without 12 teams defined (there\'s {len(_teamsCount)} right now)')
                return False
            if len(_db.getListOfRecords(Group))!=0:
                _app.showErrorMessage('Calculate group phase error',f'There are some records in Group table in the database.\nOperation forbidden.')
                return False
            # save the groups to the database
            _groups:List[List[int]]=self.generateRandomGroupPhasePlaySchedule()
            _groupCn=1
            for teamNrList in _groups:
                group=Group()
                group.groupID=_groupCn
                group.groupName=f'Group {_groupCn}'
                _cn=1
                for _teamID in teamNrList:
                    _fieldName=f'team{_cn}ID'
                    setattr(group,_fieldName,_teamID)
                    _cn+=1
                _db.addDataToDb(Group,group)
                _groupCn+=1
            # set the flag for the application (serialisable flags will be automatically saved to the database)
            _sm.setFlag('groups_defined',True)
            # calculate the schedule for games planned in each group
            g=Group()
            _schedules=self.generateSchedulesForGroupDefinition()
            for play in _schedules['play']:
                _db.addDataToDb(Play,play)
            for schedule in _schedules['schedule']:
                _db.addDataToDb(Schedule,schedule)
            # set the flag for the application (serialisable flags will be automatically saved to the database)
            _sm.setFlag('groups_scheduled',True)
            _app.showInfoMessage('Success!','Groups phase schedule fully generated.\nYou can now start recording scores for games.')
        return True

    def calculatePlayoffPhaseSchedule(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
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
        if self.getApp().createDialogYesNo('Scheduling play-off phase','Are you sure, you want to let the app randomly \ngenerate games play for play-off phase?\n\n(warning: it\'s the one way decision)'):
            pass
        return True

    def recordGamesDataList(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        play=Play()
        playListDict:List[Dict[str,Any]]=[ asdict(x) for x in self.getDb().getListOfRecords(Play) ]
        _headers=play.getHeadersForTreeview()

        self.appControl.clearMainCanvas()
        self.appControl.getMainFrame().after(50, lambda: self.appControl.chooseRecordFromList(Play.__name__,_headers,playListDict,actions,self.getApp().getMainCanvasFrame()))
        
        return True

    def recordGamesData(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Record games data. This method can be called only with referee rights account.
        Referee is updating the data of the game while there'are any changes like goals or yellow cards.
        Follow the 'Record games data' sequence diagram.
        """
        """Creates list of Team records on screen with option to edit it."""
        """Edit team data. This method can be called only with referee rights account."""
        play=Play().fromDict(data)
        return self.getApp().modalDialog('Play edit',self.appControl.dialogForEditPlay,data,actions,parentFrame,lambda data: play.fromDict(data).checkData(play,forEdit=True))

    def refereeResetApplicationData(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs) -> bool:
        """Reset application data. This method can be called only with referee rights account.
        After this operation is completed, the database is completely cleared and the application works again like during the first run.
        """
        if self.getApp().createDialogYesNo('Reset application data','Are you sure, you want to reset entire database of application?\n\n(warning: it\'s the one way decision)'):
            pass
        return True

    def loginToApp(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs):
        """Classic login/password authentication. After the data are taken, the application have to check with database if access should be granted.
        Additionally, the application keep the rights level for the account (user or referee rights account)

        - create new dialog window for getting: login, password (refer to UIAbstractInterface create new dialog)
        - get rights from database (refer to DBAbstractInterface get rights from db) and show error message if access isn't granted then go back to login dialog
        - update the login status (refer to SystemController loginStatus)
        - start the application main screen with features access depending on the account rights
        """
        
        print("loginToApp dialog here")
        # print("actions",actions)
        data=Users()
        if embedded:
            self.appControl.clearMainCanvas()
            self.appControl.getMainFrame().after(50, 
                lambda: self.appControl.dialogForAppLoginOrRegister(data,actions,self.appControl.getMainCanvasFrame())) # type: ignore            
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

    def logoutFromAccount(self,data,actions:Dict[str,Callable],embedded:bool=True,*args,**kwargs):
        """Logout from the current account.
        """

        self.stateMachine.setFlag('rights',AccountRights.NotLoggedIn)
        return True

    def showMatchOrderGroupsStatus(self):
        """User or referee both can watch the current groups status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    def showMatchOrderPlayOffTree(self):
        """User or referee both can watch the current play-off-tree status of teams."""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    def teamsAmountLessThen16(self):
        """Return True if the saved number of teams in the database is less then 16"""
        raise ExceptionUIAbstractInterface(f"no {inspect.currentframe().f_code.co_name} method defined") # type: ignore

    def changeUserRights(self,data,actions:Dict[str,Callable],parentFrame:Any=None,*args,**kwargs) -> bool:
        """Change the rights for specific users. This call should be transferred to the User.changeUserRights method"""
        user=Users().fromDict(data)
        return self.getApp().modalDialog('User edit',self.appControl.refereeDialogForUserRights,data,actions,parentFrame,lambda data: user.fromDict(data).checkRightsChange(user))

    def getRightsFromDb(self,data,*args,**kwargs):
        login=data['login'] if 'login' in data else ''
        password=data['password'] if 'password' in data else ''
        rights=self.dbControl.getRightsFromDb(login,password)
        print('login',login,'password',password,'rights',rights)
        if rights==AccountRights.NotLoggedIn:
            self.appControl.showErrorMessage('Login',f'Cannot find your account {login} for given login data.')
            return False
        self.stateMachine.setFlag('rights',rights)
        return True

    def _randomTeamFromList(self, teamList:List[int]) -> int:
        _ret=random.choice(teamList)
        teamList.remove(_ret)
        return _ret

    def generateRandomGroupPhasePlaySchedule(self) -> List[List[int]]:
        """Generates a random play schedule for entire tournament after is checked if expected amount of teams is defined.
        Method uses helpers: generateRandomTeamsList(), prepareGroupPhaseData(), preparePlayoffPhaseData().
        Call saveRelativeScheculeRecords() when the tournament schedule is calculated.
        Sets ApplicationState.setIsScheduled() after full schedule is saved."""
        _ret:List[List[int]] = []

        _db=self.getDb()
        _teamsNrs=[*range(1,13)]
        for _groupCn in range(1,5):
            _ret.append([self._randomTeamFromList(_teamsNrs),self._randomTeamFromList(_teamsNrs),self._randomTeamFromList(_teamsNrs)])
        return _ret

    def generateSchedulesForGroupDefinition(self) -> Dict[str,List[Union[Play,Schedule]]]:
        _ret:Dict[str,List[Union[Play,Schedule]]] = {"play":[],"schedule":[]}
        _scheduleCn=1
        _playCn=1
        _groups:Dict[int,List[int]]={}
        _groupRecs=self.getDb().getListOfRecords(Group)
        _date=datetime.now()
        for group in _groupRecs:
            # team1 - team2
            p=Play(playID=_playCn)
            _playCn+=1
            p.team1ID=group.team1ID
            p.team2ID=group.team2ID
            s=Schedule(scheduleID=_scheduleCn)
            _scheduleCn+=1
            s.playID=p.playID
            s.date=_date
            s.timeOfDay=TimeOfDay.Morning
            s.isGroupPhase=True
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            # team1 - team3
            p=Play(playID=_playCn)
            _playCn+=1
            p.team1ID=group.team1ID
            p.team2ID=group.team3ID
            s=Schedule(scheduleID=_scheduleCn)
            _scheduleCn+=1
            s.playID=p.playID
            s.date=_date
            s.timeOfDay=TimeOfDay.Noon
            s.isGroupPhase=True
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            # team2 - team3
            p=Play(playID=_playCn)
            _playCn+=1
            p.team1ID=group.team2ID
            p.team2ID=group.team3ID
            s=Schedule(scheduleID=_scheduleCn)
            _scheduleCn+=1
            s.playID=p.playID
            s.date=_date
            s.timeOfDay=TimeOfDay.Afternoon
            s.isGroupPhase=True
            _ret["play"].append(p)
            _ret["schedule"].append(s)

            _date+=timedelta(days=1)

        return _ret
    

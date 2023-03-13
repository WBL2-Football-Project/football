from dataclasses import dataclass,field
from StateMachine import *
from Users import Users
from Teams import Teams
from Serialisable import Serialisable

@dataclass(order=True)
class FootballStateMachine(StateMachine,Serialisable):

    footballStateMachineID:int=field(default=0)
    teams_defined:bool=field(default=False)
    groups_defines:bool=field(default=False)
    groups_scheduled:bool=field(default=False)
    groups_completed:bool=field(default=False)
    playoff_scheduled:bool=field(default=False)

    def __init__(self):
        StateMachine.__init__(self)

    def initialise(self):
        # register flags:
        (empty_database,login,rights,teams_defined,at_least_one_team_defined,groups_defined,groups_scheduled,groups_completed,teams_scheduled)=self.addFlagsByObjs(
            Flag("empty_database",bool,default=False,call=lambda sc: len(sc.getDb().getListOfRecords(Users))==0,serialisable=False),
            Flag("login",str,default="",serialisable=False),
            Flag("rights",AccountRights,default=AccountRights.NotLoggedIn,serialisable=False),
            Flag("teams_defined",bool,default=False,serialisable=True),
            Flag("at_least_one_team_defined",bool,default=False,call=lambda sc: len(sc.getDb().getListOfRecords(Teams))>0,serialisable=False),
            Flag("groups_defined",bool,default=False,serialisable=True),
            Flag("groups_scheduled",bool,default=False,serialisable=True),
            Flag("groups_completed",bool,default=False,serialisable=True),
            Flag("playoff_scheduled",bool,default=False,serialisable=True)
        )
        self.initialiseFlags()

        systemController=self.getSystemController()

        # register states:
        loginToApp=self.addState(State('loginToApp',systemController.loginToApp,default=True))
        logoutFromAccount=self.addState(State('logoutFromAccount',systemController.logoutFromAccount,default=True))
        registerAccount=self.addState(State('registerAccount',systemController.registerAccount))
        getRightsFromDb=self.addState(State('getRightsFromDb',systemController.getRightsFromDb))
        userMenu=self.addState(State('userMenu',systemController.userMenu))
        refereeMenu=self.addState(State('refereeMenu',systemController.refereeMenu))
        exitApp=self.addState(State('exitApp',systemController.exitApp))
        saveAccount=self.addState(State('saveAccount',systemController.saveAccount))
        showMatchOrderGroupsStatus=self.addState(State('showMatchOrderGroupsStatus',systemController.showMatchOrderGroupsStatus))
        showMatchOrderPlayOffTree=self.addState(State('showMatchOrderPlayOffTree',systemController.showMatchOrderPlayOffTree))
        defineTeam=self.addState(State('defineTeam',systemController.defineTeam))
        saveTeam=self.addState(State('saveTeam',systemController.saveTeam))
        saveEditedTeam=self.addState(State('saveEditedTeam',systemController.saveEditedTeam))
        refereeEditTeamDataList=self.addState(State('refereeEditTeamDataList',systemController.refereeEditTeamDataList))
        refereeEditTeamData=self.addState(State('refereeEditTeamData',systemController.refereeEditTeamData))
        changeUserRightsList=self.addState(State('changeUserRightsList',systemController.changeUserRightsList))
        changeUserRights=self.addState(State('changeUserRights',systemController.changeUserRights))
        saveUserRightChanges=self.addState(State('saveUserRightChanges',systemController.saveUserRightChanges))
        calculateGroupPhaseSchedule=self.addState(State('calculateGroupPhaseSchedule',systemController.calculateGroupPhaseSchedule))
        calculatePlayoffPhaseSchedule=self.addState(State('calculatePlayoffPhaseSchedule',systemController.calculatePlayoffPhaseSchedule))
        recordGamesDataList=self.addState(State('recordGamesDataList',systemController.recordGamesDataList))
        recordGamesData=self.addState(State('recordGamesData',systemController.recordGamesData))
        refereeResetApplicationData=self.addState(State('refereeResetApplicationData',systemController.refereeResetApplicationData))

        # tmp:
        clearForSchedule=self.addState(State('clearForSchedule',systemController.clearForSchedule))

        # transitions:
        loginToApp.setTransition("register",registerAccount)
        loginToApp.setTransition("cancel",exitApp)
        loginToApp.setTransition("ok",getRightsFromDb,transitionTo=userMenu)

        registerAccount.setTransition("cancel",registerAccount.previous)
        registerAccount.setTransition("ok",saveAccount,transitionTo=registerAccount)

        userMenu.setTransition("register_account",registerAccount).condFlags(lambda fl:fl['rights']==AccountRights.RefereeRights)
        userMenu.setTransition("show_match_order_groups_status",showMatchOrderGroupsStatus).condFlags(lambda fl:fl['groups_defined'])
        userMenu.setTransition("show_match_order_playoff_tree",showMatchOrderPlayOffTree).condFlags(lambda fl:fl['playoff_scheduled'])
        userMenu.setTransition("logout_from_account",logoutFromAccount,transitionTo=loginToApp)
        userMenu.setTransition("change_user_rights_list",changeUserRightsList).condFlags(lambda fl:fl['rights']==AccountRights.RefereeRights)
        userMenu.setTransition("edit_team_data_list",refereeEditTeamDataList).condFlags(lambda fl:not fl['groups_defined'] and fl['at_least_one_team_defined'])
        userMenu.setTransition("define_teams",defineTeam).condFlags(lambda fl:not fl['teams_defined'])
        userMenu.setTransition("record_games_data_list",recordGamesDataList).condFlags(lambda fl:fl['groups_scheduled'])
        userMenu.setTransition("reset_application_data",refereeResetApplicationData,transitionTo=self.getDefaultState())
        userMenu.setTransition("calculate_group_phase_schedule",calculateGroupPhaseSchedule,transitionTo=userMenu).condFlags(lambda fl:fl['teams_defined'] and not fl['groups_scheduled'])
        userMenu.setTransition("calculate_playoff_phase_schedule",calculatePlayoffPhaseSchedule,transitionTo=userMenu).condFlags(lambda fl:fl['groups_scheduled'] and not fl['playoff_scheduled'])

        # tmp:
        userMenu.setTransition("clear_for_schedule",clearForSchedule,transitionTo=userMenu).condFlags(lambda fl:fl['groups_scheduled'] and not fl['playoff_scheduled'])

        defineTeam.setTransition("ok",saveTeam,transitionTo=defineTeam)
        defineTeam.setTransition("cancel",userMenu)

        refereeEditTeamDataList.setTransition("chosen",refereeEditTeamData)
        refereeEditTeamDataList.setTransition("cancel",userMenu)

        recordGamesDataList.setTransition("chosen",recordGamesData)
        recordGamesDataList.setTransition("cancel",userMenu)
        
        refereeEditTeamData.setTransition("ok",saveEditedTeam,transitionTo=refereeEditTeamDataList) # TODO: add previous call for 'transitionTo'
        refereeEditTeamData.setTransition("cancel",refereeEditTeamDataList)

        changeUserRightsList.setTransition("chosen",changeUserRights)
        changeUserRightsList.setTransition("cancel",userMenu)

        changeUserRights.setTransition("ok",saveUserRightChanges,transitionTo=changeUserRightsList)
        changeUserRights.setTransition("cancel",changeUserRightsList)

        # recordGamesDataList.setTransition("choose",recordGamesData) # TODO: add style of Modal Dialog for recording data
        # recordGamesDataList.setTransition("cancel",recordGamesData.previous)
        
        # recordGamesData.setTransition("ok",saveGamesData,transitionTo=recordGamesData.previous)
        # recordGamesData.setTransition("cancel",recordGamesData.previous)


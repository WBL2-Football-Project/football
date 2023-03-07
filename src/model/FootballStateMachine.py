from StateMachine import *

class FootballStateMachine(StateMachine):
    def __init__(self,systemController=None):
        StateMachine.__init__(self,systemController)
        
        # register flags:
        (empty_database,rights,teams_defined,groups_defined,groups_scheduled,groups_completed,teams_scheduled)=self.addFlagsByObjs(
            Flag("empty_database",bool,False),
            Flag("rights",AccountRights,AccountRights.NotLoggedIn),
            Flag("teams_defined",bool,False),
            Flag("groups_defined",bool,False),
            Flag("groups_scheduled",bool,False),
            Flag("groups_completed",bool,False),
            Flag("teams_scheduled",bool,False)
        )

        # register states:
        (loginToApp,
            registerAccount,
            userMenu,
            refereeMenu,
            exitApp,
            autoLogin,
            showMatchOrderGroupsStatus,
            showMatchOrderPlayOffTree,
            defineTeam,
            refereeEditTeamData,
            changeUserRights,
            calculateGroupPhaseSchedule,
            calculatePlayoffPhaseSchedule,
            recordGamesData,
            refereeResetApplicationData)=self.addStatesByObjs(
                State('loginToApp',systemController.loginToApp,default=True),
                State('registerAccount',systemController.registerAccount),
                State('userMenu',systemController.userMenu),
                State('refereeMenu',systemController.refereeMenu),
                State('exitApp',systemController.exitApp),
                State('autoLogin',lambda st:systemController.autoLogin(st.data)),
                State('showMatchOrderGroupsStatus',systemController.showMatchOrderGroupsStatus),
                State('showMatchOrderPlayOffTree',systemController.showMatchOrderPlayOffTree),
                State('defineTeam',systemController.defineTeam),
                State('refereeEditTeamData',systemController.refereeEditTeamData),
                State('changeUserRights',systemController.changeUserRights),
                State('calculateGroupPhaseSchedule',systemController.calculateGroupPhaseSchedule),
                State('calculatePlayoffPhaseSchedule',systemController.calculatePlayoffPhaseSchedule),
                State('recordGamesData',systemController.recordGamesData),
                State('refereeResetApplicationData',systemController.refereeResetApplicationData),
        )

        # onClickRegister=lambda st,sm:True
        # setSuccessfulLogin=lambda fl:True
        
        # empty_database,rights,teams_defined,groups_defined,groups_scheduled,groups_completed,teams_scheduled

        # transitions:
        # show_login -> [event_show_login_register] -> register_user
        # show_login.transition(register_user,self.stateMachine.
        #                       beforeFlags=lambda fl:not fl['empty_database'] and fl['rights']==AccountRights.NotLoggedIn,)
        # show_login.transition(register_user,onClickRegister,
        #                       beforeFlags=lambda fl:not fl['empty_database'] and fl['rights']==AccountRights.NotLoggedIn,
        #                       beforeChange=None,
        #                       afterChange=
        #                       afterFlags=lambda fl: setSuccessfulLogin(fl))
        # show_login -> [event_show_login_ok(data)] -> show_user_menu
        # show_login -> referee_menu
        # show_login -> exit_app

        # exit_app -> exit_procedure
        # register_user -> autologin(login,password)
        # register_user -> show_login

        # autologin(login,password) -> show_user_menu
        # autologin(login,password) -> referee_user_menu
        # autologin(login,password) -> show_login

        # show_user_menu -> show_match_order_groups_status
        # show_user_menu -> show_match_order_playoff_status
        # show_user_menu -> show_login


        # referee_menu -> define_teams
        # referee_menu -> edit_team_data
        # referee_menu -> change_user_rights
        # referee_menu -> calculate_group_phase_schedule
        # referee_menu -> calculate_playoff_phase_schedule
        # referee_menu -> record_games_data
        # referee_menu -> show_match_order_groups_status
        # referee_menu -> show_match_order_playoff_status
        # referee_menu -> reset_application_data
        # show_user_menu -> show_login


        # define_teams -> define_teams
        # define_teams -> referee_menu
        # edit_team_data -> referee_menu
        # change_user_rights -> referee_menu
        # calculate_group_phase_schedule -> referee_menu
        # calculate_playoff_phase_schedule -> referee_menu
        # record_games_data -> record_games_data
        # record_games_data -> referee_menu
        # show_match_order_groups_status -> referee_menu
        # show_match_order_groups_status -> user_menu
        # show_match_order_playoff_status -> referee_menu
        # show_match_order_playoff_status -> user_menu
        # reset_application_data -> referee_menu
        # reset_application_data -> show_login

        # exit_procedur











        # flags:
        # :empty_database
        # :rights (not_logger_in,user_rights,referee_rights)
        # :teams_defined
        # :groups_scheduled
        # :playoffs_scheduled

        # states:
        # show_login -> [event_show_login_register] -> register_user
        # show_login -> [event_show_login_ok(data)] -> show_user_menu
        # show_login -> referee_menu
        # show_login -> exit_app

        # exit_app -> exit_procedure
        # register_user -> autologin(login,password)
        # register_user -> show_login

        # autologin(login,password) -> show_user_menu
        # autologin(login,password) -> referee_user_menu
        # autologin(login,password) -> show_login

        # show_user_menu -> show_match_order_groups_status
        # show_user_menu -> show_match_order_playoff_status
        # show_user_menu -> show_login

        # referee_menu -> define_teams
        # referee_menu -> edit_team_data
        # referee_menu -> change_user_rights
        # referee_menu -> calculate_group_phase_schedule
        # referee_menu -> calculate_playoff_phase_schedule
        # referee_menu -> record_games_data
        # referee_menu -> show_match_order_groups_status
        # referee_menu -> show_match_order_playoff_status
        # referee_menu -> reset_application_data
        # show_user_menu -> show_login

        # define_teams -> define_teams
        # define_teams -> referee_menu
        # edit_team_data -> referee_menu
        # change_user_rights -> referee_menu
        # calculate_group_phase_schedule -> referee_menu
        # calculate_playoff_phase_schedule -> referee_menu
        # record_games_data -> record_games_data
        # record_games_data -> referee_menu
        # show_match_order_groups_status -> referee_menu
        # show_match_order_groups_status -> user_menu
        # show_match_order_playoff_status -> referee_menu
        # show_match_order_playoff_status -> user_menu
        # reset_application_data -> referee_menu
        # reset_application_data -> show_login

        # exit_procedur

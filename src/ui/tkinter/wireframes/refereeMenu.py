from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
#from model import *
import tkinter as tk
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')))
tkVars = {}  # helper variable

# Exported dialog procedure:
def refereeMenu(data, actions:Dict[str,Callable], parentFrame=None):
    """Create dialog window with application menu with user rights:
		- change user rights
        - edit team data
        - define teams
        - record games data
        - reset application data
        - show match order groups status
        - show match order playoff tree
        - register account
    """

    # menu definition
    _a_show_match_order_groups_status=actions['show_match_order_groups_status'] if 'show_match_order_groups_status' in actions else None
    _a_show_match_order_playoff_tree=actions['show_match_order_playoff_tree'] if 'show_match_order_playoff_tree' in actions else None
    _a_register_account=actions['register_account'] if 'register_account' in actions else None
    _a_change_user_rights_list=actions['change_user_rights_list'] if 'change_user_rights_list' in actions else None
    _a_edit_team_data_list=actions['edit_team_data_list'] if 'edit_team_data_list' in actions else None
    _a_define_teams=actions['define_teams'] if 'define_teams' in actions else None
    _a_record_games_data_list=actions['record_games_data_list'] if 'record_games_data_list' in actions else None
    _a_reset_application_data=actions['reset_application_data'] if 'reset_application_data' in actions else None
    _a_logout_from_account=actions['logout_from_account'] if 'logout_from_account' in actions else None
    _a_calculate_group_phase_schedule=actions['calculate_group_phase_schedule'] if 'calculate_group_phase_schedule' in actions else None
    _a_calculate_playoff_phase_schedule=actions['calculate_playoff_phase_schedule'] if 'calculate_playoff_phase_schedule' in actions else None
    _a_clear_for_schedule=actions['clear_for_schedule'] if 'clear_for_schedule' in actions else None

    _refereeMenu=[]
    if _a_define_teams!=None: _refereeMenu.append({"name":"Define teams","action":lambda event:_a_define_teams()})
    if _a_calculate_group_phase_schedule!=None: _refereeMenu.append({"name":"Calculate group phase schedule","action":lambda event:_a_calculate_group_phase_schedule()})
    if _a_calculate_playoff_phase_schedule!=None: _refereeMenu.append({"name":"Calculate playoff phase schedule","action":lambda event:_a_calculate_playoff_phase_schedule()})
    if _a_edit_team_data_list!=None: _refereeMenu.append({"name":"Edit team data","action":lambda event:_a_edit_team_data_list()})
    if _a_record_games_data_list!=None: _refereeMenu.append({"name":"Record games data","action":lambda event:_a_record_games_data_list()})
    if _a_change_user_rights_list!=None: _refereeMenu.append({"name":"Change user rights","action":lambda event:_a_change_user_rights_list()})
    if _a_show_match_order_groups_status!=None: _refereeMenu.append({"name":"Show match order groups status","action":lambda event:_a_show_match_order_groups_status()})
    if _a_show_match_order_playoff_tree!=None: _refereeMenu.append({"name":"Show match order playodd tree","action":lambda event:_a_show_match_order_playoff_tree()})
    if _a_register_account!=None: _refereeMenu.append({"name":"Register user","action":lambda event:_a_register_account()})
    if _a_reset_application_data!=None: _refereeMenu.append({"name":"Reset application data","action":lambda event:_a_reset_application_data()})
    if _a_logout_from_account!=None: _refereeMenu.append({"name":"Logout from account","action":lambda event:_a_logout_from_account()})
    if _a_clear_for_schedule!=None: _refereeMenu.append({"name":"Clear for schedule (development)","action":lambda event:_a_clear_for_schedule()})

    print('referee menu...')
    # build simple button menu on screen
    _buttons={}
    _cn=1
    tk.Label(parentFrame, text="User menu:", font=('Helvetica', 10)).grid(row=0,column=0)
    for menu in _refereeMenu:
        if menu['action'] != None:
            _buttons[_cn]=tk.Button(parentFrame,text=menu['name'])
            _buttons[_cn].grid(row=_cn,column=0)
            if menu['action']!=None:
                _buttons[_cn].bind('<Button-1>',menu['action'])
            _cn+=1

if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.login = ""
            self.password = ""
            self.rights = ""
    fields = Fields()

    def onClickOk(*vars):
        print("Returned:", vars)

    refereeMenu(fields,{"ok":onClickOk},mainFrame)

    mainFrame.mainloop()

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

print(os.getcwd(),os.path.abspath(os.path.join(os.path.dirname(__file__), 'src', 'model')))

from StateMachine import State

tkVars = {}  # helper variable

# Exported dialog procedure:

def userMenu(data, actions:Dict[str,Callable], parentFrame=None):
    """Create dialog window with application menu with user rights:
        - show match order groups status
        - show match order playoff tree
        - register account
    """

    # menu definition
    _a_show_match_order_groups_status=actions['show_match_order_groups_status'] if 'show_match_order_groups_status' in actions else None
    _a_show_match_order_playoff_tree=actions['show_match_order_playoff_tree'] if 'show_match_order_playoff_tree' in actions else None
    _a_register_account=actions['register_account'] if 'register_account' in actions else None
    _a_logout_from_account=actions['logout_from_account'] if 'logout_from_account' in actions else None

    _userMenu=[]
    if _a_show_match_order_groups_status!=None: _userMenu.append({"name":"Show match order groups status","action":lambda event: _a_show_match_order_groups_status()})
    if _a_show_match_order_playoff_tree!=None: _userMenu.append({"name":"Show match order playodd tree","action":lambda event: _a_show_match_order_playoff_tree()})
    if _a_register_account!=None: _userMenu.append({"name":"Show match order playodd tree","action":lambda event: _a_register_account()})
    if _a_logout_from_account!=None: _userMenu.append({"name":"Logout","action":lambda event: _a_logout_from_account()})

    # build simple button menu on screen
    _buttons={}
    _cn=1
    tk.Label(parentFrame, text="User menu:", font=('Helvetica', 10)).grid(row=0,column=0)
    for menu in _userMenu:
        if menu['action']!=None:
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

    userMenu(fields,{"ok":onClickOk},mainFrame)

    mainFrame.mainloop()

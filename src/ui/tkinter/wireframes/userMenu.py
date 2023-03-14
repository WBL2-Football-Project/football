from StateMachine import State
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
#from model import *
from constants import *
import tkinter as tk
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src', 'model')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

print(os.getcwd(), os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'src', 'model')))


tkVars = {}  # helper variable

# Exported dialog procedure:


def userMenu(data, actions: Dict[str, Callable], parentFrame=None):
    """Create dialog window with application menu with user rights:
        - show match order groups status
        - show match order playoff tree
        - register account
    """

    # menu definition
    _a_show_match_order_groups_status = actions[
        'show_match_order_groups_status'] if 'show_match_order_groups_status' in actions else None
    _a_show_match_order_playoff_tree = actions[
        'show_match_order_playoff_tree'] if 'show_match_order_playoff_tree' in actions else None
    _a_register_account = actions['register_account'] if 'register_account' in actions else None
    _a_logout_from_account = actions['logout_from_account'] if 'logout_from_account' in actions else None

    _userMenu = []
    if _a_show_match_order_groups_status != None:
        _userMenu.append({"name": "View Groups",
                         "action": lambda event: _a_show_match_order_groups_status()})
    if _a_show_match_order_playoff_tree != None:
        _userMenu.append({"name": "View Schedule",
                         "action": lambda event: _a_show_match_order_playoff_tree()})
    if _a_register_account != None:
        _userMenu.append({"name": "Show match order playodd tree",
                         "action": lambda event: _a_register_account()})
    if _a_logout_from_account != None:
        _logoutAction = {"name": "Logout",
                         "action": lambda event: _a_logout_from_account()}

    userMenuFrame = tk.Frame(parentFrame)
    userMenuFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    userMenuFrame.grid(row=1)

    _buttons = {}
    _cn = 1

    row = 1
    column = 0

    logoutButton = tk.Button(parentFrame, text=_logoutAction['name'], background=SECONDARY_COLOUR,
                             foreground="#FFFFFF", font=(FONT, 10), width=20)
    logoutButton.grid(row=0, columnspan=5, ipady=2,
                      ipadx=2, padx=10, pady=15, sticky='e')
    logoutButton.bind('<Button-1>', _logoutAction['action'])

    for menu in _userMenu:
        if menu['action'] != None:
            _buttons[_cn] = tk.Button(
                userMenuFrame, text=menu['name'], font=(FONT, 10), background=PRIMARY_COLOUR, foreground="#FFFFFF")
            _buttons[_cn].grid(row=row, column=column,
                               ipady=2, ipadx=2, padx=10, pady=15)
            if menu['action'] != None:
                _buttons[_cn].bind('<Button-1>', menu['action'])

                column += 1
                if column > 2:
                    column = 0
                    row += 1

            _cn += 1


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

    userMenu(fields, {"ok": onClickOk}, mainFrame)

    mainFrame.mainloop()

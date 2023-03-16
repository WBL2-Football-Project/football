import sys
from typing import Optional, List, Any, Callable
from model import *

if __name__ == '__main__':
    # checking if TkInter is enable in environment
    try:
        import tkinter as tk
        from tkinter import ttk
        import tkinter.font as tkfont
        from tkinter import simpledialog
        from tkinter import messagebox
        Gui = True
    except ImportError:
        Gui = False
    """Testing PyDoc functionality 2.0
	"""

    # console start version
    Gui=False
    # checking start parameters - turning ON/OFF GUI

    # load proper AppControlInterface implementation
    from ui.console.AppConsole import AppConsole

    # starting the SystemController for the application ( dependency injection pattern ) - everything else is managed inside the SystemController object instance
    SystemController(DBPickleFile('football.pck'), AppConsole(), FootballStateMachine())

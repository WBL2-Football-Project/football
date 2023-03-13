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

    # analysing launch parameters (console mode run for auto tests)
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--console":
            Gui = False
        elif sys.argv[1] == "":
            if not Gui:
                print(
                    "There's not tkinter support in the environment, you need to start the program with -console parameter instead")
                exit(-1)
        elif sys.argv[1] == "--help":
            print("launch options:")
            print("  --console => start program in not GUI console mode")
            print("  --help => show help")
            exit(0)
    else:
        if not Gui:
            print("There's not tkinter support in the environment, you need to start the program with -console parameter instead")
            exit(-1)

    # checking start parameters - turning ON/OFF GUI
    if Gui:  # tkinter UI

        # load proper AppControlInterface implementation
        from ui.tkinter.AppGui import AppGui

        # starting the SystemController for the application ( dependency injection pattern ) - everything else is managed inside the SystemController object instance
        a=FootballStateMachine()
        SystemController(DBPickleFile('football.pck'), AppGui(), FootballStateMachine() )

    else:  # console UI

        # load proper AppControlInterface implementation
        from ui.console.AppConsole import AppConsole

        # starting the SystemController for the application ( dependency injection pattern ) - everything else is managed inside the SystemController object instance
        SystemController(DBPickleFile('football.pck'), AppConsole(), FootballStateMachine())

import os
import sys
from typing import Optional,List,Any,Callable,Dict
import inspect
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from model import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import simpledialog
from tkinter import messagebox

# Exported dialog procedure:
def createDialogYesNo(title:str,content:str,parentFrame):
        """Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
        User have to choose one option to close the window.

        Args:
            title (str): title of the window
            message (str): message text

        """
    
    # TODO: create the dialog

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    createDialogYesNo("title","content",mainFrame)

    mainFrame.mainloop()
    
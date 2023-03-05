from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
#from model import *
import os
import sys
from typing import Optional, List, Any, Callable, Dict
import inspect
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))


# Exported dialog procedure:
def createDialogYesNo(title: str, content: str, parentFrame):
    """Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
    User have to choose one option to close the window.

    Args:
        title (str): title of the window
        message (str): message text

    """

    dialogPopUp = tk.Toplevel(parentFrame)
    dialogPopUp.grid_columnconfigure(0, weight=1, uniform="equal")

    dialogPopUp.title(title)
    dialogPopUp.geometry("250x100")
    dialogPopUp.resizable(False,  False)

    dialogMessage = tk.Label(
        dialogPopUp, text=content, font=('Helvetica', 10))

    dialogMessage.grid(row=0)

    buttonsFrame = tk.Frame(dialogPopUp)
    buttonsFrame.grid(row=3, pady=(15, 0))
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    onNoButton = tk.Button(buttonsFrame, text='No', width=5)
    onNoButton.grid(row=0, column=0, padx=20)
    onNoButton.bind(
        "<Button-1>", lambda event: {"result": False})

    # Yes BUTTON
    onYesButton = tk.Button(buttonsFrame, text='Yes', width=5)
    onYesButton.grid(row=0, column=1, padx=20)
    onYesButton.bind(
        "<Button-1>", lambda event: {"result": True})


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    createDialogYesNo("title", "content", mainFrame)

    mainFrame.mainloop()

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
def showInfoMessage(title: str, content: str, parentFrame):
    """Showing new modal window on screen designed for information message.

    Args:
        title (str): title of the window
        message (str): message text

    """

    infoPopUp = tk.Toplevel(parentFrame)
    infoPopUp.grid_columnconfigure(0, weight=1, uniform="equal")

    infoPopUp.title(title)
    infoPopUp.geometry("250x100")
    infoPopUp.resizable(False,  False)

    infoMessage = tk.Label(
        infoPopUp, text=content, font=('Helvetica', 10))

    infoMessage.grid(row=0)

    buttonsFrame = tk.Frame(infoPopUp)
    buttonsFrame.grid(row=3, pady=(15, 0))
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

# OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='OK', width=5)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind(
        "<Button-1>", lambda event: infoPopUp.destroy())

# TODO: create the list for user to click one and return his tkID when user choose one record


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    showInfoMessage(
        "Information", "This is a piece of information!", mainFrame)

    mainFrame.mainloop()

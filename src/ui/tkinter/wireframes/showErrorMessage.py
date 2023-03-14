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
from ModalDialog import ModalDialog
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
#from model import *

# Exported dialog procedure:


def showErrorMessage(title: str, content: str, parentFrame):
    """Showing new modal window on screen designed for error message.

    Args:
        title (str): title of the window
        message (str): message text

    """

    # errorPopUp = tk.Toplevel(parentFrame)
    # errorPopUp.grid_columnconfigure(0, weight=1, uniform="equal")

    # errorPopUp.title(title)
    # errorPopUp.geometry("250x100")
    # # errorPopUp.resizable(False,  False)

    # errorMessage = tk.Label(
    #     errorPopUp, text=content, font=('Helvetica', 10))

    # errorMessage.grid(row=0)

    # buttonsFrame = tk.Frame(errorPopUp)
    # buttonsFrame.grid(row=3, pady=(15, 0))
    # buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # # OK BUTTON
    # onOKButton = tk.Button(buttonsFrame, text='OK', width=5)
    # onOKButton.grid(row=0, column=0)
    # onOKButton.bind(
    #     "<Button-1>", lambda event: errorPopUp.destroy())

    # open the modal dialog window for getting the values
    class _modalForExit(ModalDialog):
        def __init__(self, parent):
            super().__init__(parent, title, self.showResults, oneOkButton=True)

        def showResults(self, result):  # shows the results for every vehicle price offer
            return result

        def body(self, frame):  # designs the window widgets
            # exit question label
            tk.Label(frame, text=content).grid(
                row=0, column=0, ipadx=30, ipady=30, sticky='news')
            return frame

    _obj = _modalForExit(parentFrame)
    if _obj.getResult():
        return True
    return False

# TODO: create the message


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    showErrorMessage("Error Message", "This is an error message!", mainFrame)

    mainFrame.mainloop()

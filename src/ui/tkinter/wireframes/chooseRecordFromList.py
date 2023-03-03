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

tkID=Any # helper variable

# Exported dialog procedure:
def chooseRecordFromList(fieldsObj_list:List[Any],onClickOk,parentFrame):
    """Create a window with the list of records from chosen table and let the user select one of them."""
    
    global tkID
    tkID=tk.StringVar(parentFrame)

    # TODO: create the list for user to click one and return his tkID when user choose one record

if __name__=="__main__":

    # TEST CODE FOR DIALOG:

    mainFrame=tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.ID=""
            self.field1=""
            self.field2=""
            # as many field as the object will have for particular instance...
    fields_list=[Fields(),Fields(),Fields(),Fields(),Fields(),Fields()]
    def onClickOk(*vars):
        print("Returned:",vars)

    chooseRecordFromList(fields_list,onClickOk,mainFrame)
    onOKButton=tk.Button(mainFrame, text='OK', width=5)
    onOKButton.grid(row=20,column=0,columnspan=2,sticky='w')
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"chosen_record_ID":tkID.get()}))

    mainFrame.mainloop()
    

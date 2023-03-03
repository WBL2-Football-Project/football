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

tkVars={} # helper variable

def dialogForEditTeam(fieldsObj,onClickOk,parentFrame):
    """Create dialog window for input fields:
        - name
    """
    global tkVars
    tkVars["name"]=tk.StringVar(parentFrame,fieldsObj.name)

    tk.Label(parentFrame,text='Name:').grid(row=2,column=0,columnspan=2,sticky='w')
    tk.Entry(parentFrame,textvariable=tkVars["name"]).grid(row=3,column=0,columnspan=2,sticky='ew')

if __name__=="__main__":
    mainFrame=tk.Tk()
    mainFrame.title("Dialog")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self):
            self.name=""
    fields=Fields()

    def onClickOk(*name):
        print("name",name)

    dialogForEditTeam(fields,onClickOk,mainFrame)

    onOKButton=tk.Button(mainFrame, text='OK', width=5)
    onOKButton.grid(row=20,column=0,columnspan=2,sticky='w')
    onOKButton.bind("<Button-1>", lambda event: onClickOk({"name":tkVars["name"].get()}))

    mainFrame.mainloop()

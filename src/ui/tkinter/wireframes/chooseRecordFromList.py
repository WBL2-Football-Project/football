import os
import sys
from typing import Optional, List, Any, Callable, Dict, Type
from functools import reduce
import inspect
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '.')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../..')))

from ColumnStyle import ColumnStyle, JustifyEnum
from Serialisable import Serialisable
from tkinter import messagebox
from tkinter import simpledialog
from constants import *
import tkinter.font as tkfont
from tkinter import ttk
import tkinter as tk
#from model import *

# Exported dialog procedure:


# def chooseRecordFromList(tableType:Type[Serialisable], headers: Dict[str,ColumnStyle], fieldsObj_list: List[Serialisable], actions:Dict[str,Callable], parentFrame):
def chooseRecordFromList(title: str, headers: List[ColumnStyle], fieldsObj_list: List[Dict[str, Any]], actions: Dict[str, Callable], parentFrame):
    """Create a window with the list of records from chosen table and let the user select one of them."""

    tkID = Any  # helper variable
    tkID = tk.StringVar(parentFrame)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    parentFrame.grid_rowconfigure(0, weight=1)

    _columns = []
    for header in headers: #_cn in range(1, len(headers)):
        _columns.append(header.getName()) #f"c{_cn}")

    recordList = ttk.Treeview(parentFrame, columns=_columns, show='headings')

    def _r(a,b):
        return max(
            int(tkfont.Font().measure(a)),
            int(tkfont.Font().measure(b))
        )
    
    # headers
    for style in headers:
        _maxColValueWidth=0
        if len(fieldsObj_list)>=2:
            _maxColValueWidth=reduce(_r,[ x[style.getName()] for x in fieldsObj_list ])
        else:
            for fieldsObj in fieldsObj_list:
                _a:str=fieldsObj[style.getName()] # type: ignore - get the value for column 
                _maxColValueWidth=max(_maxColValueWidth,int(tkfont.Font().measure(_a)))
        recordList.heading(style.getName(), text=style.getVisualName()) #_colHash
        _maxColValueWidth=max(_maxColValueWidth,int(tkfont.Font().measure(style.getVisualName())))
        recordList.column(style.getName(), anchor=style.getJustifyForUI(), width=_maxColValueWidth) #_colHash

    recordList.grid(row=0,column=0,sticky='news')

    scrollbar = ttk.Scrollbar(parentFrame, orient='horizontal', command=recordList.xview)
    scrollbar.grid(row=1, sticky='ew')
    recordList.configure(xscrollcommand=scrollbar.set)

    def item_selected(event):
        for selected_item in recordList.selection():
            item = recordList.item(selected_item)
            record = item['values']
            tkID.set(item.get('text'))

    recordList.bind('<<TreeviewSelect>>', item_selected)

    # primary key names in array
    _ID_names_array = [v.getName() for v in headers if v.getPrimaryKey()]

    # values
    _cn = 0
    for iteamValuesDict in fieldsObj_list:
        _values=[ iteamValuesDict[h.getName()] if h.getName() in iteamValuesDict else "?" for h in headers ]
        recordList.insert('', 'end', values=_values, text=f'{_cn}')
        _cn += 1

    buttonsFrame = tk.Frame(parentFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='Choose',
                           width=20, font=(FONT, 10), background=PRIMARY_COLOUR, foreground='#FFFFFF')
    onOKButton.grid(row=0, column=0, ipadx=2, ipady=2)
    onOKButton.bind(
        "<Button-1>", lambda event: actions['chosen'](fieldsObj_list[int(tkID.get())]))

    # Cancel Button
    onCancelButton = tk.Button(
        buttonsFrame, text='Cancel', width=20, font=(FONT, 10), background=SECONDARY_COLOUR, foreground='#FFFFFF')
    onCancelButton.grid(row=0, column=1, padx=15, ipadx=2, ipady=2)
    onCancelButton.bind(
        "<Button-1>", lambda event: actions['cancel']())


if __name__ == "__main__":

    # TEST CODE FOR DIALOG:

    mainFrame = tk.Tk()
    mainFrame.title("Dialog for new team")
    mainFrame.geometry("800x600")

    # data fields
    class Fields:
        def __init__(self, ID, field1, field2):
            self.ID = ID
            self.field1 = field1
            self.field2 = field2

            # as many field as the object will have for particular instance...
    fields_list = [Fields(1, "Test1", "Test1"), Fields(2, "Test2", "Test2"),
                   Fields(3, "Test3", "Test3"), Fields(4, "Test4", "Test4"), Fields(5, "Test5", "Test5"), Fields(6, "Test6", "Test6")]

    def onClickOk(*vars):
        print("Returned:", vars)

    chooseRecordFromList(fields_list, onClickOk, mainFrame)
    mainFrame.mainloop()

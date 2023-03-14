import os
import sys
from typing import Optional, List, Any, Callable, Dict, Type
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

    _columns = ""
    for _cn in range(0, len(headers)-1):
        _columns += ', ' if len(_columns) > 0 else ''
        _columns += f"c{_cn}"
    recordList = ttk.Treeview(
        parentFrame, columns=_columns)

    # headers
    _cn = 0
    for style in headers:
        _colHash = f'#{_cn}'
        _cn += 1
        recordList.heading(_colHash, text=style.getName())
        recordList.column(_colHash, anchor=style.getJustifyForUI(), width=150)

    recordList.grid(row=0)

    scrollbar = tk.Scrollbar(
        parentFrame, orient='horizontal', command=recordList.xview)
    scrollbar.grid(row=1, sticky='ew')
    recordList.configure(xscrollcommand=scrollbar.set)

    # choose row handler
    def selectItem(item):
        item = recordList.focus()
        selected_item = recordList.item(item)
        tkID.set(selected_item.get('text'))

    recordList.bind('<ButtonRelease-1>', selectItem)

    # primary key names in array
    _ID_names_array = [v.getName() for v in headers if v.getPrimaryKey()]

    # values
    _cn = 0
    for iteamValuesDict in fieldsObj_list:
        # _text=f'{[ v for k,v in iteamValuesDict.items() if k in _ID_names_array ]}'
        _values = iteamValuesDict.items()
        # [ _values[v.getName()] for v in headers ]
        recordList.insert('', 'end', text=f'{_cn}', values=[
                          v for k, v in iteamValuesDict.items()])
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

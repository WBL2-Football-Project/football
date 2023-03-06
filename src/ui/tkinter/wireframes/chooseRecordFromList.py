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


tkID = Any  # helper variable

# Exported dialog procedure:


def chooseRecordFromList(fieldsObj_list: List[Any], onClickOk, parentFrame):
    """Create a window with the list of records from chosen table and let the user select one of them."""

    global tkID
    tkID = tk.StringVar(parentFrame)

    parentFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    chooseRecordFromListFrame = tk.Frame(parentFrame)
    chooseRecordFromListFrame.grid()

    recordList = ttk.Treeview(chooseRecordFromListFrame, columns="c1, c2")

    recordList.heading('#0', text='ID')
    recordList.heading('#1', text='Field 1')
    recordList.heading('#2', text='Field 2')
    recordList.column('#0', anchor=tk.CENTER)
    recordList.column('#1', anchor=tk.CENTER)
    recordList.column('#2', anchor=tk.CENTER)

    recordList.grid(row=0)

    def selectItem(item):
        item = recordList.focus()
        selected_item = recordList.item(item)
        tkID.set(selected_item.get('text'))

    recordList.bind('<ButtonRelease-1>', selectItem)

    for record in fieldsObj_list:
        recordList.insert('', 'end', text=record.ID,
                          values=(record.field1, record.field2))

    buttonsFrame = tk.Frame(chooseRecordFromListFrame)
    buttonsFrame.grid(row=5, pady=15)
    buttonsFrame.grid_columnconfigure(0, weight=1, uniform="equal")

    # OK BUTTON
    onOKButton = tk.Button(buttonsFrame, text='Choose', width=20)
    onOKButton.grid(row=0, column=0)
    onOKButton.bind(
        "<Button-1>", lambda event: onClickOk({"chosen_record_ID": tkID.get()}))

    # Cancel Button
    onCancelButton = tk.Button(buttonsFrame, text='Cancel', width=20)
    onCancelButton.grid(row=0, column=1, padx=15)
    onCancelButton.bind(
        "<Button-1>", lambda event: chooseRecordFromListFrame.destroy())


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

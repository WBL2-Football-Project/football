import tkinter as tk
import tkinter.ttk as ttk
from .pages.LoginScreen import LoginScreen
from .pages.HomeScreen import HomeScreen
from api.api import API
import os


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Football Tournament Tracker")
        self.geometry("800x600")

        self.resizable(False, False)

    def startApp(self):
        LoginScreen(self)

        self.mainloop()

    def setSystemController(self, systemController):
        self.systemController = systemController

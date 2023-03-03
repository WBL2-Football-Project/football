import tkinter as tk
import tkinter.ttk as ttk
from api.Models.User import User
import hashlib


class LoginScreen(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # Root is reference to the GUI class that instantiated the window and system Controller object
        self.api = root.systemController.api
        self.systemController = root.systemController

        self.pack(fill="both", expand=True)

        label = tk.Label(self, text="Login", font=('Helvetica', 20, 'bold'))
        label.grid(row=0, column=0, columnspan=2, ipady=10, sticky='w')
        label.pack()

        self.username = tk.Entry(self, width=30)
        self.username.pack(pady=10, ipady=5)

        self.password = tk.Entry(self, width=30)
        self.password.pack(pady=10, ipady=5)

        loginButton = tk.Button(
            self, text="Login", foreground='#FFFFFF', background='#1537E7', width=30, command=lambda: self.login())
        loginButton.pack(pady=10)

    def login(self):
        username = self.username.get()
        username = username.strip()
        username = username.lower()

        password = self.password.get()
        password = hashlib.sha256()

        if (username != "" and password != ""):
            user = User(username, password)
            self.api.login(self, user)

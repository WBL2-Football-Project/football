import tkinter as tk


class PopUpModal(tk.Toplevel):
    def __init__(self, frame, title):
        tk.Toplevel.__init__(self, frame)
        self.frame = frame
        self.title = title

        self.geometry("300x150")
        self.resizable(False, False)

        confirmButton = tk.Button(
            self, text="Confirm", command=lambda: self.confirmButton(), background='#1537E7', width=10, foreground='#FFFFFF')
        confirmButton.grid(row=2, column=1, ipady=2, padx=20, sticky=tk.E)

        cancelButton = tk.Button(
            self, text="Cancel", command=lambda: self.destroy(), background='#E73B15', width=10, foreground='#FFFFFF')
        cancelButton.grid(row=2, column=2, ipady=2, sticky=tk.E)

    def confirmButton(self):
        return self

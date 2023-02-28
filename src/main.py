import sys
from typing import Optional
from model import *

if __name__ == '__main__':
	# checking if TkInter is enable in environment
	try:
		import tkinter as tk
		from tkinter import ttk
		import tkinter.font as tkfont
		from tkinter import simpledialog
		from tkinter import messagebox
		Gui=True
	except ImportError:
		Gui=False
	"""Testing PyDoc functionality 2.0
	"""

	# analysing launch parameters (console mode run for auto tests)
	if len(sys.argv) >= 2:
		if sys.argv[1]=="--console":
			Gui=False
		elif sys.argv[1]=="":
			if not Gui:
				print("There's not tkinter support in the environment, you need to start the program with -console parameter instead")
				exit(-1)
		elif sys.argv[1]=="--help":
			print("launch options:")
			print("  --console => start program in not GUI console mode")
			print("  --help => show help")
			exit(0)
	else:
		if not Gui:
			print("There's not tkinter support in the environment, you need to start the program with -console parameter instead")
			exit(-1)

	# checking start parameters - turning ON/OFF GUI
	if Gui: # tkinter UI

		# starting tkinter helper class
		class TkHelper(UIHelperInterface,tk.Tk):
			def __init__(self):
				UIHelperInterface.__init__(self,self)
				tk.Tk.__init__(self) # initialisation of the Tk library

				self.systemController:Optional[SystemController]=None

				# e.g. root window title and dimension
				self.title("Football Tournament Tracker")

				# e.g. or - set geometry (width x height)
				self.geometry('800x600')

			def startApplicationLoop(self):
				# Execute Tkinter window
				self.mainloop()

			def setSystemController(self, systemController):
				self.systemController = systemController

		# starting the SystemController for the application ( dependency injection pattern ) - everything else is managed inside the SystemController object instance
		SystemController(DBPickleFile('football.db'),UITkinterGUI(TkHelper()))

	else: # console UI

		# starting console UI helper class
		class ConsoleHelper(UIHelperInterface):
			def __init__(self):
				UIHelperInterface.__init__(self,self)

				self.systemController:Optional[SystemController]=None
				self._exitApp=False # true if we want to exit from the main loop

				# e.g. root window title and dimension
				print("\nFootball Tournament Tracker")
				print("---------------------------")

			def startApplicationLoop(self):
				while not self._exitApp:
					print("** SAMPLE CODE ** Welcome, please enter your account details below (login,password).")
					print("LOGIN (hit ENTER on empty field = register new user account | Cmd/Ctrl+C = exit app):")
					login=input()
					if login=="":
						# registering new user account
						print("TODO: registering new user account")
					else:
						# continue working with the program
						print("TODO: input password and proceed with check login and rights")
						
			def setSystemController(self, systemController):
				self.systemController = systemController

		# starting the SystemController for the application ( dependency injection pattern ) - everything else is managed inside the SystemController object instance
		SystemController(DBPickleFile('football.db'),UIConsole(ConsoleHelper()))

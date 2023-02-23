"""
nested modules - Testing PyDoc 
"""
import sys
# import re
# import pickle
# import os

def testingpydoc(num1,num2):
	"""_summary_

	Args:
		num1 (_type_): _description_
		num2 (_type_): _description_
	"""
	print("Hello")

# if __name__ == '__main__':
# 	# checking if TkInter is enable in environment
# 	try:
# 		import tkinter as tk
# 		from tkinter import ttk
# 		import tkinter.font as tkfont
# 		from tkinter import simpledialog
# 		from tkinter import messagebox
# 		Gui=True
# 	except ImportError:
# 		Gui=False
# 	"""Testing PyDoc functionality 2.0
# 	"""

# 	# analysing launch parameters (console mode run for auto tests)
# 	if len(sys.argv) >= 2:
# 		if sys.argv[1]=="--console":
# 			Gui=False
# 		elif sys.argv[1]=="":
# 			if not Gui:
# 				print("There's not tkinter support in the environment, you need to start the program with -console parameter instead")
# 				exit(-1)
# 		elif sys.argv[1]=="--help":
# 			print("launch options:")
# 			print("  --console => start program in not GUI console mode")
# 			print("  --help => show help")
# 			exit(0)
# 	else:
# 		if not Gui:
# 			print("There's not tkinter support in the environment, you need to start the program with -console parameter instead")			
# 			exit(-1)


# 	# checking start parameters - turning ON/OFF GUI
# 	if Gui:
# 		root = tk.Tk()
		
# 		# root window title and dimension
# 		root.title("Welcome to football")
		
# 		# Set geometry (widthxheight)
# 		root.geometry('800x600')

# 		# Execute Tkinter
# 		root.mainloop()	
# 	else:
# 		print("Welcome to football\n")

print(testingpydoc.__doc__)

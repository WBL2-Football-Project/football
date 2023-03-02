import sys
from typing import Optional,List,Any,Callable
from model import *

# starting console UI helper class
class AppConsole(AppControlInterface):
	def __init__(self):
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

	# UIAbstractInterface implementation
	def createNewDialog(self, widgetDefinitionObj:WidgetDefinition):
		"""Prepare creation of a new dialog window on screen, saving widgetDefinitionObj.

		Args:
			widgetDefinitionObj (WidgetDefinition): _description_

		Raises:
			ExceptionUIAbstractInterface: no createNewDialog method defined
		"""
		pass
	
	def createDialogWithNeededWidgets(self):
		"""Setup widgets in new dialog window and activate it on screen for to interact with user."""
		pass

	def chooseRecordFromList(self, table:Serialisable, filterFunc:Optional[Callable[[Any],List[Any]]]=None):
		"""Create a window with the list of records from chosen table and let the user select one of them.

		Args:
			table (Serialisable): the class object inherited from the Serialisable class, representing the data in the table in the application database
			filterFunc (Callable[[Any],List[Any]],Optional): _description_

		Raises:
			ExceptionUIAbstractInterface: _description_
		"""
		pass

	def inputDataFromUser(self):
		"""Hand out the control of window UI and all created widgets to user for waiting for they answer.
		"""
		pass

	def showInfoMessage(self, title, message):
		"""Showing new modal window on screen designed for information message.

		Args:
			title (str): title of the window
			message (str): message text

		"""
		pass

	def showErrorMessage(self, title, message):
		"""Showing new modal window on screen designed for error message.

		Args:
			title (str): title of the window
			message (str): message text

		"""
		pass

	def createDialogYesNo(self, title, question): 
		"""Showing new modal window on screen designed for asking the user for one of the answers: Yes or No.
		User have to choose one option to close the window.

		Args:
			title (str): title of the window
			message (str): message text

		"""
		pass

	def displayStatisticsForGroupAndItsGamesScheduled(self,dataStruct:List[GroupWithGamesScheduled]):
		pass

	def displayStatisticsForPlayoffScheduledGames(self,dataStruct:List[SchedulesWithPlay]):
		pass

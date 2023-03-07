from typing import Dict,List,Type
from SerialisableInterface import SerialisableInterface

class Serialisable(SerialisableInterface):
	"""Inheritance class for the other classes which should be serialized into the database"""

	"""static list of serialisable classes in the database
	object (Serialisable) : class to serialise
	List[str] : list of the field names to serialise from class
	"""
	tableNameList:Dict[Type[SerialisableInterface], List[str]]={}

	def __init__(self,serialisationClass:Type[SerialisableInterface],fieldList:List[str]):
		"""Initialize the serialisation with parameters

		Args:
			serialiseDestinationClass (Serialisable): serialisation class to serialise
			fieldList (List[str]): _description_
		"""
		self.serialisationClass = serialisationClass
		self.tableName = serialisationClass
		self.fieldList = fieldList
		# Serialisable.tableNameList[self.serialisationClass]=self.fieldList
		# print('Serialisable:',[ k.__name__ for k,v in Serialisable.tableNameList.items() ])


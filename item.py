"""Item Module

This module contains Item class.
"""

class Item(object):
	"""Item class
	Stores an id, and a name.

	Attributes:
	* id (int) - id of item
	* name (string) - name of item
	"""
<<<<<<< HEAD
	def __init__(self, id, name, t = 'None'):
=======
	def __init__(self, id, name, t = None):
>>>>>>> refs/remotes/Whatsit/master
		#Item constructor
		self.id = id
		self.name = name
		self.itemType = t
		self.effects = {}

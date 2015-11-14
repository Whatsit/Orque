"""Item Module

This module contains Item class.
<<<<<<< HEAD
"""
=======
Item class
Stores an id, and a name.
>>>>>>> refs/remotes/Whatsit/master

class Item(object):
	"""Item class
	Stores an id, and a name.

	Attributes:
	* id (int) - id of item
	* name (string) - name of item
	"""
    def __init__(self, id, name):
		#Item constructor
        self.id = id
        self.name = name

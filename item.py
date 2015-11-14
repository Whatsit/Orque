"""Item Module

This module contains Item class.
Item class
Stores an id, and a name.

Attributes:
* id (int) - id of item
* name (string) - name of item
"""
class Item(object):

    def __init__(self, id, name):
		#Item constructor
        self.id = id
        self.name = name

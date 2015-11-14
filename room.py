""" Room Module

roomType is temporary for now
0 => default room
1 => puzzle room

adjacencyList signifies the type of connection between rooms
index of list corresponds to direction(clockwise)
0 => north
1 => east
2 => south
3 => west
value in list corresponds to connector type
0 => wall
1 => corridor
2 => door
3 => uninitialized
"""
from item import Item

class Room:
	""" Room Class
	
	Attributes:
	roomType (int) - type of room. 0 by default
	itemList (list [item]) - list of items in the room
	playerList (list [player]) - list of players in the room
	adjacencyList (list [int]) - adjacency list for the room
	"""
	def __init__(self, type = 0):
		""" Default Constructor 
		
		Parameters:
		type (int) - room type. 0 by default.
		"""
		self.roomType = type
		self.itemList = []
		self.playerList = []
		self.adjacencyList = [3,3,3,3]

	def describe(self):
		""" describe
		
		Print description of the room.
		The description will vary depending on the type of room.
		"""
		if self.roomType == 1:
			print("There's a puzzle in this room")
		else:
			print("This is a normal room")
	
	def checkDoor(self):
		""" checkDoor
		
		check the adjacency list of the room to see if a door is locked.
		If the door is locked, return the direction of the door.
		If multiple doors are locked, return all directions.
		
		Return: result (list) - list of locked door directions.
		"""
		result = []
		for x in range(0, 4):
			if self.adjacencyList[x] == 2:
				result.append(x)
		return result
		
	def hasItemByName(self, itemName):
		""" hasItemByName
		
		checks if the room has a specific item. returns true if the item is in the room.
		otherwise false.
		
		Parameters:
		itemName (string) - name of the item to search
		
		Return: boolean - result
		"""
		for x in range(0, len(self.itemList)):
			item = self.itemList[x]
			if item.name == itemName:
				return True
		return False

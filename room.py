'''
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
'''
from item import Item

class Room:
	def __init__(self, type = 0):
		self.roomType = type
		self.itemList = []
		self.playerList = []
		self.adjacencyList = [3,3,3,3]

	def describe(self):
		if self.roomType == 1:
			print("There's a puzzle in this room")
		else:
			print("This is a normal room")
	
	def checkDoor(self):
		for x in self.adjacencyList:
			if x is 2:	# if we find a locked door, return direction of door.
				return self.adjacencyList.index(x)
			else:
				return None
	def hasItemByName(self, itemName):
		for x in range(0, len(self.itemList)):
			item = self.itemList[x]
			if item.name == itemName:
				return True
		return False

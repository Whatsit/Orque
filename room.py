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
'''

class Room:
	def __init__(self, type = 0):
		self.roomType = type
		self.itemList = []
		self.playerList = []
		self.adjacencyList = [1,1,1,1]

	def describe(self):
		if self.roomType == 1:
			print("There's a puzzle in this room")
		else:
			print("This is a normal room")

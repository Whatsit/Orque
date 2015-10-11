class Room:
	def __init__(self):
		self.itemList = []
		self.playerList = []
		self.adjacencyList = [0,0,0,0]
	def checkDoor (self):
	''' Returns the adjacent room’s direction if there is a locked door (i.e. a puzzle room) adjacent to this room, or None if no such connection exists.'''
        for x in self.adjacencyList:
            if x is 2:    # if we find a locked door, return direction of door.
                return self.adjacencyList.index(x)
            else
                return None

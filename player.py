from gameMap import *
class Player:
	def __init__(self, id, loc):
		self.playerId = id
		self.name = "Default"
		self.health = 1
		self.inventory = []
		self.location = loc
		self.command = ""

	def addItem(self, item):
		inventory.append(item)

	def removeItem(self, item):
		inventory.remove(item)

	def updateCom(self, string):
		command = string

	def useItem(self):
		if not inventory:
			print('No item')
		else:
			check = Room.checkDoor()
			if check == None:
				print('No door you idiot')
			else:
				move(check, True)

	# dir holds the direction to move incoded as 0-3 (north, east, south, west).
	# flag lets move now if the player has a key to unlock a potential door.
	def move(self, dir, flag):
		location = self.location
		newLoc = location
		curRoom = Map.layout[location[0]][location[1]]
		if dir == 0:	# north
			check = curRoom.adjacencyList[0]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]+1]
				curRoom.playerList.remove(self)
				newRoom = Map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				location = newLoc
			elif check == 2 and flag == false:
				print('The door is locked')
			else:
				print('You hit a wall...')
		elif dir == 1:	# east
			check = curRoom.adjacencyList[1]
			if check == 1 or flag == True:
				newLoc = [location[0]+1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = Map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				location = newLoc
				print("I moved bitches")
			elif check == 2 and flag == false:
				print('The door is locked')
			else:
				print('You hit a wall...')
		elif dir == 3:	# west
			check = curRoom.adjacencyList[3]
			if check == 1 or flag == True:
				newLoc = [location[0]-1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = Map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				location = newLoc
			elif check == 2 and flag == false:
				print('The door is locked')
			else:
				print('You hit a wall...')
		elif dir == 2:	# south
			check = curRoom.adjacencyList[2]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]-1]
				curRoom.playerList.remove(self)
				newRoom = Map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				location = newLoc
			elif check == 2 and flag == false:
				print('The door is locked')
			else:
				print('You hit a wall...')

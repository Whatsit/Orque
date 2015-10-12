import settings
#------------------------------------------------------------------------------------------
#Player class
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

	def move(self, dir, flag):
		location = self.location
		newLoc = location
		curRoom = settings.mapContainer[0].layout[location[0]][location[1]]
		if dir == 0:	#north
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
		elif dir == 1:	#east
			check = curRoom.adjacencyList[1]
			if check == 1 or flag == True:
				newLoc = [location[0]+1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = settings.mapContainer[0].layout[newLoc[0]][newLoc[1]]
				#newRoom.playerList.append(self)
				location = newLoc
				print("I moved bitches")
			elif check == 2 and flag == false:
				print('The door is locked')
			else:
				print('You hit a wall...')
		elif dir == 3:	#west
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
		elif dir == 2:	#south
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

#------------------------------------------------------------------------------------------
#Map class
MAPSIZE = 3 

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(MAPSIZE)] for x in range(MAPSIZE)]

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom
#------------------------------------------------------------------------------------------
#Room class
class Room:
	def __init__(self):
		self.itemList = []
		self.playerList = []
		self.adjacencyList = [0,0,0,0]

#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------

import config
from room import Room

class Player:
	def __init__(self, id, loc):
		self.playerId = id
		self.name = "Default"
		self.health = 1
		self.inventory = []
		self.location = loc
		self.command = ""

	def addItem(self, item):
		self.inventory.append(item)

	def removeItem(self, item):
		self.inventory.remove(item)

	def updateCom(self, string):
		self.command = string

	def useItem(self):
		if not inventory:
			print('No item')
		else:
			check = Room.checkDoor()
			if check == None:
				print('No door you idiot')
			else:
				move(check, True)

	def search(self):
		items = ""
		for i in config.map.layout[self.location[0]][self.location[1]].itemList:
			items += i.name
		
		if items == "":
			print("There are no items in the room")
		else:
			print("The follwing items are in the room: %s" % items)

	def parseCommand(self):
		cmd = self.command.split(" ")
		if cmd[0] == "move":
			if cmd[1] == "north":
				self.move(0,False)
			elif cmd[1] == "east":
				self.move(1,False)
			elif cmd[1] == "south":
				self.move(2,False)
			elif cmd[1] == "west":
				self.move(3,False)
			else:
				print("Please input valid direction")
		elif cmd[0] == "search":
			self.search()
		elif cmd[0] == "inventory":
			self.printInventory()
		elif cmd[0] == "get":
			self.getItem()
		else:
			print("Please input valid command")

	#Picks up key from room(temporary)
	def getItem(self):
		curRoom = config.map.layout[self.location[0]][self.location[1]]
		if not curRoom.itemList:
			print("There is no item to gotet from this room")
		else:
			self.inventory.append(curRoom.itemList[0])
			curRoom.itemList.pop()
			print("You got some items")
			self.printInventory()

	def printInventory(self):
		items = ""
		for i in self.inventory:
			items += i.name
		
		if items == "":
			print("There are no items in your inventory")
		else:
			print("The follwing items are in your inventory: %s" % items)

	def move(self, dir, flag):
		location = self.location
		newLoc = self.location
		curRoom = config.map.layout[location[0]][location[1]]
		print(curRoom.adjacencyList)
		if dir == 0:	#north
			check = curRoom.adjacencyList[0]
			if check == 1 or flag == True:
				newLoc = [location[0]-1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				print("You moved north")
			elif check == 2 and flag == False:
				print('The door is locked')
			else:
				print('You hit a wall...')
			print(self.location)
		elif dir == 1:	#east
			check = curRoom.adjacencyList[1]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]+1]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				print("You moved east")
			elif check == 2 and flag == False:
				print('The door is locked')
			else:
				print('You hit a wall...')
			print(self.location)
		elif dir == 2:	#south
			check = curRoom.adjacencyList[2]
			if check == 1 or flag == True:
				newLoc = [location[0]+1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				print("You moved south")
			elif check == 2 and flag == False:
				print('The door is locked')
			else:
				print('You hit a wall...')
			print(self.location)
		elif dir == 3:	#west
			check = curRoom.adjacencyList[3]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]-1]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				print("You moved west")
			elif check == 2 and flag == False:
				print('The door is locked')
			else:
				print('You hit a wall...')
			print(self.location)

		config.map.layout[self.location[0]][self.location[1]].describe()
		if check == 1:
			print(newRoom.adjacencyList)
		else:
			print(curRoom.adjacencyList)
		

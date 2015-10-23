import config
import itertools
from map import Map
from room import Room

class Player:
	def __init__(self, id, loc):
		self.playerId = id
		self.name = "Default"
		self.health = 1
		self.inventory = []
		self.location = loc
		self.command = ""
		self.playerPath = [loc]


	def addItem(self, item):
		self.inventory.append(item)

	def removeItem(self, item):
		self.inventory.remove(item)

	def updateCom(self, string):
		self.command = string

	def hasItemByName(self, itemName):
		for x in range(0, len(self.inventory)):
			item = self.inventory[x]
			if item.name == itemName:
				return True
		return False
		
	def useItem(self, itemName):
		if not self.inventory:
			print('Inventory is empty')
		else:
			if not self.hasItemByName(itemName):
				print('There is no item called ', itemName, ' in inventory')
			else:
				curRoom = config.map.layout[self.location[0]][self.location[1]]
				check = curRoom.checkDoor()
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
			if len(cmd) > 1:
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
			else:
				print("Please include a valid direction")
		elif cmd[0] == "search":
			self.search()
		elif cmd[0] == "inventory":
			self.printInventory()
		elif cmd[0] == "get":
			if len(cmd) > 1:
				self.getItem(cmd[1])
			else:
				print("Please include an item name")
		elif cmd[0] == "use":
			if len(cmd) > 1:
				self.useItem(cmd[1])
			else:
				print("Please include an item name")
		else:
			print("Please input valid command")

	#Picks up key from room(temporary)
	def getItem(self, itemName):
		curRoom = config.map.layout[self.location[0]][self.location[1]]
		
		if not curRoom.hasItemByName(itemName):
			print("There is no item named ", itemName ," to get from this room")
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
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
				print("You moved north")
				print(self.playerPath)
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
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
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
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
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
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
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
		config.map.printMap()

import config
import itertools
from map import Map
from room import Room

DIRECTIONS = {"north" : 0, "east" : 1, "south" : 2, "west" : 3}

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
		
	def useItem(self, itemName, dir):
		if not self.inventory:
			print('Inventory is empty')
		else:
			if not self.hasItemByName(itemName):
				print('There is no item called ', itemName, ' in inventory')
			else:
				curRoom = config.map.layout[self.location[0]][self.location[1]]
				check = curRoom.checkDoor()
				print(check)
				if not check:
					print('There are no locked doors')
				else:
					if dir == None:
						self.move(DIRECTIONS[check[0]], True)
					else:
						if dir in DIRECTIONS.keys():
							if dir in check :
								self.move(DIRECTIONS[dir], True)
							else:
								print("You hit a wall")
						else:
							print("Invalid direction parameter")

	def search(self):
		items = ""
		for i in config.map.layout[self.location[0]][self.location[1]].itemList:
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			print("There are no items in the room")
		else:
			print("The following items are in the room: %s" % items)

	def parseCommand(self):
		cmd = self.command.split(" ")
		if cmd[0] == "move":
			if len(cmd) > 1:
				if cmd[1] in DIRECTIONS.keys():
					self.move(DIRECTIONS[cmd[1]],False)
				else:
					print("Invalid direction parameter")
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
				if len(cmd) > 2:
					self.useItem(cmd[1], cmd[2])
				else:
					self.useItem(cmd[1], None)
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
			print("You picked up an item: %s" % itemName)
			self.printInventory()

	def printInventory(self):
		items = ""
		for i in self.inventory:
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			print("There are no items in your inventory")
		else:
			print("The following items are in your inventory: %s" % items)
		
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

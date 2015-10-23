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

<<<<<<< HEAD
	def hasItemByName(self, itemName):
		for x in range(0, len(self.inventory)):
			item = self.inventory[x]
			if item.name == itemName:
				return True
		return False
		
	def useItem(self, itemName, dir):
		if not self.inventory:
			print('Inventory is empty')
=======
	def useItem(self):
		if not inventory:
			print('No item')
>>>>>>> refs/remotes/Whatsit/master
		else:
			check = Room.checkDoor()
			if check == None:
				print('No door you idiot')
			else:
<<<<<<< HEAD
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
=======
				move(check, True)
>>>>>>> refs/remotes/Whatsit/master

	def search(self):
		items = ""
		for i in config.map.layout[self.location[0]][self.location[1]].itemList:
<<<<<<< HEAD
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			print("There are no items in the room")
		else:
			print("The following items are in the room: %s" % items)
=======
			items += i.name
		
		if items == "":
			print("There are no items in the room")
		else:
			print("The follwing items are in the room: %s" % items)
			
>>>>>>> refs/remotes/Whatsit/master

	def parseCommand(self):
		#FUCKING TOTAL FREEDOM BITCH TEMPLATE 
		
		'''
		Example inputss:
			I want to move right
			I want to move left
			I want to move west
			I want to move up
			Down is the direction I want to move
			right
			up
			grab							( will get key)
			backpack						( display inventory)
			down search move left 			(this input moves you down, more restrictions?)
			up dasioda dwjdnad adonad		(this moves you up, more restrictions?)
			and a whole bunch of other shit  
			
			But is it too much freedom? 
		'''
		
		PossibleMoves = ['down','south','bottom','bot','top','up','north','left','west','right','east']
		MoveIndicate = ['move', 'run', 'walk']
		Down = ['down','south','bottom','bot']
		Up = ['top','up','north']
		Left = ['left','west']
		Right = ['right','east']
		PossibleSearches = ['search','find','explore','examine']
		PossibleInventories = ['inventory','backpack','items','found']
		PossibleGet = ['get','take','steal','grab']
		cmd = self.command.split(" ")
<<<<<<< HEAD
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
=======
		for i in range(0, len(cmd)):
			s = cmd[i]
			if s in MoveIndicate:						#if move is found first, then check next input for direction
				if i != len(cmd)-1:						#if there is anything after move command
					if cmd[i+1] in Up:
						self.move(0,False)
					elif cmd[i+1] in Right:
						self.move(1,False)
					elif cmd[i+1] in Down:
						self.move(2,False)
					elif cmd[i+1] in Left:
						self.move(3,False)
					else:
						print("Please type in a valid direction to move")
					break
				else:
					print("Please type in a direction to move")
					break
			elif s in PossibleMoves:				#if direction is indicated without move 
				if cmd[i] in Up:
					self.move(0,False)
				if cmd[i] in Right:
					self.move(1,False)
				if cmd[i] in Down:
					self.move(2,False)
				if cmd[i] in Left:
					self.move(3,False)
				break
			elif s in PossibleSearches:
				self.search()
				i = len(cmd)
				break
			elif s in PossibleInventories:
				self.printInventory()
				i = len(cmd)
				break
			elif s in PossibleGet:
				self.getItem()
				i = len(cmd)	
				break	
			elif i == len(cmd)-1:				#no valid commands were found
				print("Please input valid command")
				
				
			

			
>>>>>>> refs/remotes/Whatsit/master

	#Picks up key from room(temporary)
	def getItem(self):
		curRoom = config.map.layout[self.location[0]][self.location[1]]
		if not curRoom.itemList:
			print("There is no item to gotet from this room")
		else:
			self.inventory.append(curRoom.itemList[0])
			curRoom.itemList.pop()
			print("You picked up an item: %s" % itemName)
			self.printInventory()

	def printInventory(self):
		items = ""
		for i in self.inventory:
<<<<<<< HEAD
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			print("There are no items in your inventory")
		else:
			print("The following items are in your inventory: %s" % items)
		
=======
			items += i.name
		
		if items == "":
			print("There are no items in your inventory")
		else:
			print("The follwing items are in your inventory: %s" % items)
>>>>>>> refs/remotes/Whatsit/master
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
		

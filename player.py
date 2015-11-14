"""Player Module

Handles player movements and possible actions.
Parses player input and exectues action.
Possible actions are: move, search, get, use, and check inventory.
"""
import config
import itertools
from map import Map
from room import Room
from random import randint

"""Dictionaries for movement directions:
"""
DIRECTIONS = {'0' : ['top','up','north'], '1' : ['right','east'], '2' : ['down','south','bottom','bot'], '3' : ['left','west']}

PossibleMoves = ['down','south','bottom','bot','top','up','north','left','west','right','east']
MoveIndicate = ['move', 'run', 'walk']
Down = ['down','south','bottom','bot']
Up = ['top','up','north']
Left = ['left','west']
Right = ['right','east']
PossibleSearches = ['search','find','explore','examine']
PossibleInventories = ['inventory','backpack','items','found']
PossibleGet = ['get','take','steal','grab']
PossibleUse = ['use']

class Player:
	"""Player class
<<<<<<< HEAD
	
	Attributes:
	playerID (int) - id
	name (string) - player name. defaults to "default"
	health (int) - health. defaults to 1
	inventory (list [item]) - player inventory
	command (string) - requested action/command
	playerPath (list) - list of player locations visited
=======
>>>>>>> refs/remotes/Whatsit/master
	"""
	def __init__(self, id):
		""" Default Constructor
		
		Parameters: 
		id (int) - player id
		"""
		self.playerId = id
		self.name = "Default"
		self.health = 1
		self.inventory = []
		self.location = randomCoord()
		self.command = ""
		self.playerPath = [self.location]
		config.map.layout[self.location[0]][self.location[1]].playerList.append(self)

	def addItem(self, item):
<<<<<<< HEAD
		"""addItem() 
		adds item to player inventory list.
		
		Parameters: 
		item (item) - item to add
=======
		"""addItem() Peramiters: item
		adds item to player inventroy list.
>>>>>>> refs/remotes/Whatsit/master
		"""
		self.inventory.append(item)

	def removeItem(self, item):
<<<<<<< HEAD
		""" removeItem() 
		
		removes item to inventory list
		
		Peramiters:
		
		item (item) - item to remove
=======
		"""removeItem() Peramiters: item
		removes item to inventory list
>>>>>>> refs/remotes/Whatsit/master
		"""
		self.inventory.remove(item)

	def updateCom(self, string):
<<<<<<< HEAD
		""" updateItem() 
		
		sets player command as string.
		
		Parameters:
		string (string) - command
		"""
		self.command = string

	#working on better way to handle associating directional keyword with num
	def getKeyByValue(self, value):
		""" getKeyByValue
		
		get directional value given a value from DIRECTIONS
		
		Parameters:
		
		value (string) - value to search
=======
		"""updateItem() Peramiters: string
		sets player command as string.
		"""
		self.command = string


	def getKeyByValue(self, value):
		"""working on better way to handle associating directional keyword with num
>>>>>>> refs/remotes/Whatsit/master
		"""
		key = ""
		print(DIRECTIONS.values())
		for x in range(0, 4):
			valueList = list(DIRECTIONS.values())[x]
			if value in valueList:
				key = list(DIRECTIONS.keys())[x]
		print("key is", key)

	def hasItemByName(self, itemName):
<<<<<<< HEAD
		""" hasItemByName()
		
		returns true or false if player has itemName in inventory.
		
		Parameters:
		itemName (string) - item name to search
=======
		"""hasItemByName() Peramiters: itemName
		returns true or false if player has itemName in inventory.
>>>>>>> refs/remotes/Whatsit/master
		"""
		for x in range(0, len(self.inventory)):
			item = self.inventory[x]
			if item.name == itemName:
				return True
		return False
<<<<<<< HEAD
	
	def useItem(self, itemName, dir):
		"""useItem() 
		
		determines if player can use item on door
		if so moves player through door.
		
		Parameters:
		itemName (string) - item to use
		dir (int) - direction to move
=======

	def useItem(self, itemName, dir):
		"""useItem() Peramiters: itemName, dir
		determins if player can use item on door
		then if so moves player through door.
>>>>>>> refs/remotes/Whatsit/master
		"""
		if not self.inventory:
			return 'Inventory is empty'
		else:
			if self.hasItemByName(itemName):
				curRoom = config.map.layout[self.location[0]][self.location[1]]
				check = curRoom.checkDoor()
				print(check)
				if not check:
					return 'There are no locked doors'
				else:
					if dir == None:
						self.move(check[0], True)
					else:
						if dir in Up and 0 in check:
							self.move(0, True)
						elif dir in Right and 1 in check:
							self.move(1, True)
						elif dir in Down and 2 in check:
							self.move(2, True)
						elif dir in Left and 3 in check:
							self.move(3, True)
						else:
							return "Invalid direction parameter"
			else:
				return "There is no item called %s in your inventory" % itemName
<<<<<<< HEAD
	
	def search(self):
		"""search()
		
=======

	def search(self):
		"""search() Peramiters: None
>>>>>>> refs/remotes/Whatsit/master
		seaches current room for items that can be picked up.
		"""
		items = ""
		for i in config.map.layout[self.location[0]][self.location[1]].itemList:
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			return "There are no items in the room"
		else:
			return "The following items are in the room: %s" % items

	def parseCommand(self):
<<<<<<< HEAD
		"""parseCommand()
		
		parses command and calls corresponding action function.
		
		Example inputs:
=======
		"""parseCommand() Peramiters: None
		parses command and calls corisponding action function.
		"""

		'''
		Example inputss:
>>>>>>> refs/remotes/Whatsit/master
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
		"""


		cmd = self.command.split(" ")

		for i in range(0, len(cmd)):
			s = cmd[i]
			#if move is found first, then check next input for direction
			if s in MoveIndicate:
				#if there is anything after move command
				if i != len(cmd)-1:
					if cmd[i+1] in Up:
						return self.move(0,False)
					elif cmd[i+1] in Right:
						return self.move(1,False)
					elif cmd[i+1] in Down:
						return self.move(2,False)
					elif cmd[i+1] in Left:
						return self.move(3,False)
					else:
						return "Please type in a valid direction to move"
					break
				else:
					return "Please type in a direction to move"
					break
			#if direction is indicated without move
			elif s in PossibleMoves:
				if cmd[i] in Up:
					return self.move(0,False)
				if cmd[i] in Right:
					return self.move(1,False)
				if cmd[i] in Down:
					return self.move(2,False)
				if cmd[i] in Left:
					return self.move(3,False)
				break
			elif s in PossibleSearches:
				return self.search()
				i = len(cmd)
				break
			elif s in PossibleInventories:
				return self.printInventory()
				i = len(cmd)
				break
			elif s in PossibleGet:
				return self.getItem(cmd[i+1])
				i = len(cmd)
				break
			elif s in PossibleUse:
				if len(cmd) > 2:
					return self.useItem(cmd[i+1], cmd[i+2])
				elif len(cmd) > 1:
					return self.useItem(cmd[i+1], None)
				i = len(cmd)
				break
			#no valid commands were found
			elif i == len(cmd)-1:
				return "Please input valid command"

	def getItem(self, itemName):
<<<<<<< HEAD
		"""getItem() 
		
		Picks up key from room(temporary)
		"""
=======
		"""getItem() Picks up key from room(temporary)"""
>>>>>>> refs/remotes/Whatsit/master
		curRoom = config.map.layout[self.location[0]][self.location[1]]
		if not curRoom.itemList:
			return "There is no item to get from this room"
		else:
			if curRoom.hasItemByName(itemName):
				self.inventory.append(curRoom.itemList[0])
				curRoom.itemList.pop()
				return "You picked up an item: %s" % itemName
				self.printInventory()
			else:
				return "There is no item called %s to get from this room" % itemName
<<<<<<< HEAD
	
	def printInventory(self):
		"""printInventory() 
		
=======

	def printInventory(self):
		"""printInventory() Peramiters: None
>>>>>>> refs/remotes/Whatsit/master
		prints items in inventory.
		"""
		items = ""
		for i in self.inventory:
			items += i.name + ", "
		items = items[:-2]

		if items == "":
			return "There are no items in your inventory"
		else:
			return "The following items are in your inventory: %s" % items
<<<<<<< HEAD
	
	def move(self, dir, flag):
		"""move() 
		
		handles move action. if calling functions has determined that player can move,
		moves player to room in given direction.
		
		Parameters:
		dir () - direction to move
		flag () - flag var
=======

	def move(self, dir, flag):
		"""move() Peramiters: dir, flag
		dir = direction to move
		flag = if calling functions has determinded that player can move
		moves player to room in givien direction.
>>>>>>> refs/remotes/Whatsit/master
		"""
		output = ''
		location = self.location
		newLoc = self.location
		curRoom = config.map.layout[location[0]][location[1]]
		print(curRoom.adjacencyList)
		config.map.printMap(self.playerId)
		#move north
		if dir == 0:
			check = curRoom.adjacencyList[0]
			if check == 1 or flag == True:
				newLoc = [location[0]-1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				#Append to playerPath and insure no duplicates
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
				output = "You moved north"
			elif check == 2 and flag == False:
				output = 'The door is locked'
			else:
				output = 'You hit a wall...'
			print(self.location)
		#move east
		elif dir == 1:
			check = curRoom.adjacencyList[1]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]+1]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				#Append to playerPath and insure no duplicates
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
				output = "You moved east"
			elif check == 2 and flag == False:
				output = 'The door is locked'
			else:
				output = 'You hit a wall...'
			print(self.location)
		#move south
		elif dir == 2:
			check = curRoom.adjacencyList[2]
			if check == 1 or flag == True:
				newLoc = [location[0]+1, location[1]]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				#Append to playerPath and insure no duplicates
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
				output = "You moved south"
			elif check == 2 and flag == False:
				output = 'The door is locked'
			else:
				output = 'You hit a wall...'
			print(self.location)
		#move west
		elif dir == 3:
			check = curRoom.adjacencyList[3]
			if check == 1 or flag == True:
				newLoc = [location[0], location[1]-1]
				curRoom.playerList.remove(self)
				newRoom = config.map.layout[newLoc[0]][newLoc[1]]
				newRoom.playerList.append(self)
				self.location = newLoc
				#Append to playerPath and insure no duplicates
				self.playerPath.append(newLoc)
				self.playerPath.sort()
				self.playerPath = list(k for k,_ in itertools.groupby(self.playerPath))
				output = "You moved west"
			elif check == 2 and flag == False:
				output = 'The door is locked'
			else:
				output = 'You hit a wall...'
			print(self.location)

		config.map.layout[self.location[0]][self.location[1]].describe()
		if check == 1:
			print(newRoom.adjacencyList)
		else:
			print(curRoom.adjacencyList)
		config.map.printMap(self.playerId)
		return output

def randomCoord():
<<<<<<< HEAD
	"""randomCoord 
	returns random coordinate on map.
	
	Return: (list[int][int]) - coordinates
=======
	"""randomCoord Peramiters: None
	returns random coordinite on map.
>>>>>>> refs/remotes/Whatsit/master
	"""
	return [randint(0,config.ROWS-1), randint(0,config.COLS-1)]

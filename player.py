"""Player class
"""
import config
import itertools
import sys
from threading import Timer, Thread
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
	"""
	def __init__(self, id):
		self.playerId = id
		self.name = "Default"
		self.health = 1
		self.inventory = []
		self.location = randomCoord()
		self.command = ""
		self.playerPath = [self.location]
		config.map.layout[self.location[0]][self.location[1]].playerList.append(self)

	def addItem(self, item):
		"""addItem() Peramiters: item
		adds item to player inventroy list.
		"""
		self.inventory.append(item)

	def removeItem(self, item):
		"""removeItem() Peramiters: item
		removes item to inventory list
		"""
		self.inventory.remove(item)

	def updateCom(self, string):
		"""updateItem() Peramiters: string
		sets player command as string.
		"""
		self.command = string


	def getKeyByValue(self, value):
		"""working on better way to handle associating directional keyword with num
		"""
		key = ""
		print(DIRECTIONS.values())
		for x in range(0, 4):
			valueList = list(DIRECTIONS.values())[x]
			if value in valueList:
				key = list(DIRECTIONS.keys())[x]
		print("key is", key)

	def hasItemByName(self, itemName):
		"""hasItemByName() Peramiters: itemName
		returns true or false if player has itemName in inventory.
		"""
		for x in range(0, len(self.inventory)):
			item = self.inventory[x]
			if item.name == itemName:
				return True
		return False

	def useItem(self, itemName, dir):
		"""useItem() Peramiters: itemName, dir
		determins if player can use item on door
		then if so moves player through door.
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
				if config.map.layout[self.location[0]][self.location[1]].roomType == 1:
					attemptPuzzle()
			else:
				return "There is no item called %s in your inventory" % itemName

	def search(self):
		"""search() Peramiters: None
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
		"""parseCommand() Peramiters: None
		parses command and calls corisponding action function.
		"""

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
		"""getItem() Picks up key from room(temporary)"""
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

	def printInventory(self):
		"""printInventory() Peramiters: None
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

	def move(self, dir, flag):
		"""move() Peramiters: dir, flag
		dir = direction to move
		flag = if calling functions has determinded that player can move
		moves player to room in givien direction.
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
		#config.map.printMap(self.playerId)
		return output

def randomCoord():
	"""randomCoord Peramiters: None
	returns random coordinite on map.
	"""
	return [randint(0,config.ROWS-1), randint(0,config.COLS-1)]

def attemptPuzzle():
	global timeOut 
	global playerAnswer
	timeOut = False
	playerAnswer = None
	puzzleThread = Thread(target=startPuzzle)
	puzzleThread.daemon = True
	puzzleThread.start()
	puzzleThread.join(1)
	if playerAnswer is None:
		print("\nToo slow my friend, you're dead!\nPress enter to continue")
		timeOut = True

playerAnswer = None
timeOut = False
def startPuzzle():
	global playerAnswer
	global timeOut
	question = "1+1= "
	realAnswer = 2
	playerAnswer = input(question)
	if timeOut == False:
		if playerAnswer == str(realAnswer):
			print("How clever, you're correct!")
		else:
			print("Were you dropped as a baby? Welp, doesnt matter now, you're dead!")

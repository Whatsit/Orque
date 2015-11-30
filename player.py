"""Player Module

Handles player movements and possible actions.
Parses player input and exectues action.
Possible actions are: move, search, get, use, and check inventory.
"""
import config
import itertools
import sys
from threading import Timer, Thread
from map import Map
from room import Room
from item import Item
from Attack import attack
from random import randint, choice, seed

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
PossibleAttack = ['attack','fight','charge','hit','punch','kick']
PossibleEquip = ['equip']

class Player:
	"""Player class

	Attributes:
	playerID (int) - id
	name (string) - player name. defaults to "default"
	health (int) - health. defaults to 1
	inventory (list [item]) - player inventory
	command (string) - requested action/command
	playerPath (list) - list of player locations visited
	"""
	def __init__(self, id):
		""" Default Constructor
		Parameters:
		id (int) - player id
		"""
		self.playerId = id
		self.name = "Default"
		self.health = 10
		self.attackRange = [0,3]
		self.protection = 0
		self.attackBonus = 0
		self.inventory = []
		self.outfit = "None"
		self.weapon = "None"
		self.location = randomCoord()
		self.command = ""
		self.playerPath = [self.location]
		config.map.layout[self.location[0]][self.location[1]].playerList.append(self)

	def playerAttack(self):
		if(len(config.map.layout[self.location[0]][self.location[1]].playerList) == 1):
			return "You flail at the air violently... ( -1 PRIDE )"
		elif(len(config.map.layout[self.location[0]][self.location[1]].playerList) == 2):
			return "You Attack the person before you ( attack not done )"
			for p in config.map.layout[self.location[0]][self.location[1]].playerList:
				if(p != self):
					print("Winner :: " + str(attack(self, self, p)))
		else:
			self.health = self.health - 1
			return "Due to the packed confines, you trip over the other people in the room... ( -1 HEALTH )"
			

	def equipItem(self, itemName):
		if self.hasItemByName(itemName):
			item = None
			for i in self.inventory:
				if i.name == itemName:
					item = i
					break
			if item.itemType == "armor":
				self.outfit = item.name
				self.protection = item.effects["armor"]
				return "Armor Equipped :: ProtectionBonus: " + str(self.protection)
			elif item.itemType == "weapon":
				self.weapon = item.name
				self.attackBonus = item.effects["weapon"]
				return "Weapon Equipped :: AttackBonus: " + str(self.attackBonus)
			else:
				return "Can't equip this type"
		else:
			return "No such equipment in inventory"

	def addItem(self, item):
		"""addItem()
		adds item to player inventory list.

		Parameters:
		item (item) - item to add
		"""
		self.inventory.append(item)

	def removeItem(self, item):
		""" removeItem()

		removes item to inventory list

		Peramiters:

		item (item) - item to remove
		"""
		self.inventory.remove(item)

	def updateCom(self, string):
		""" updateItem()

		sets player command as string.

		Parameters:
		string (string) - command
		"""
		self.command = string

	#working on better way to handle associating directional keyword with num
	def getKeyByValue(self, value):
		""" getKeyByValue """
		key = ""
		print(DIRECTIONS.values())
		for x in range(0, 4):
			valueList = list(DIRECTIONS.values())[x]
			if value in valueList:
				key = list(DIRECTIONS.keys())[x]
		print("key is", key)

	def hasItemByName(self, itemName):
		""" hasItemByName()

		returns true or false if player has itemName in inventory.

		Parameters:
		itemName (string) - item name to search
		"""
		for x in range(0, len(self.inventory)):
			item = self.inventory[x]
			if item.name == itemName:
				return True
		return False

	def useItem(self, itemName, dir):
		""" useItem()

		determines if player can use item on door
		if so moves player through door.

		Parameters:
		itemName (string) - item to use
		dir (int) - direction to move
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
					self.attemptPuzzle()
			else:
				return "There is no item called %s in your inventory" % itemName

	def search(self):
		""" search()

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
		""" parseCommand()

		parses command and calls corresponding action function.

		Example inputs:
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
			attack							(will attack other player in room)
		"""


		cmd = self.command.split(" ", maxsplit = 1)

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
				if len(cmd) == 1:
					print('Please input item name')
				else:
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
			elif s in PossibleAttack:
				return self.playerAttack()
				i = len(cmd)
				break
			elif s in PossibleEquip:
				if len(cmd) > 1:
					return self.equipItem(cmd[i+1])
				i = len(cmd)
				break
			#no valid commands were found
			elif i == len(cmd)-1:
				return "Please input valid command"

	def getItem(self, itemName):
		"""getItem()

		Picks up key from room(temporary)
		"""
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
		"""printInventory()
		prints items in inventory.
		"""
		items = ""
		for i in self.inventory:
			items += " | " + i.itemType + " : " + i.name + "@"
		items = items[:-1]

		if items == "":
			return "There are no items in your inventory"
		else:
			return "The following items are in your inventory:@%s" % items

	def move(self, dir, flag):
		""" move()

		handles move action. if calling functions has determined that player can move,
		moves player to room in given direction.

		Parameters:
		dir () - direction to move
		flag () - flag var
		"""
		output = ''
		location = self.location
		newLoc = self.location
		curRoom = config.map.layout[location[0]][location[1]]
		print(curRoom.adjacencyList)
		config.map.printMap(self)
		
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


	playerAnswer = None
	timeOut = False

	def attemptPuzzle(self):
		global timeOut
		global playerAnswer
		timeOut = False
		playerAnswer = None
		puzzleThread = Thread(target=self.startPuzzle)
		puzzleThread.daemon = True
		puzzleThread.start()
		puzzleThread.join(10)
		if playerAnswer is None:
			print("\nToo slow my friend, you're dead!\nPress enter to continue")
			timeOut = True

	def startPuzzle(self):
		global playerAnswer
		global timeOut
		question, realAnswer = generateQuestions()
		playerAnswer = input(question)
		if timeOut == False:
			if playerAnswer == str(realAnswer):
				print("How clever, you're correct!")
				self.puzzleReward()
			else:
				print("Were you dropped as a baby? Welp, doesnt matter now, you're dead!")
				#ToDo: Kill the player, temp: Randomly teleport player
				config.map.layout[self.location[0]][self.location[1]].playerList.remove(self)
				self.location = randomCoord()
				while config.map.layout[self.location[0]][self.location[1]].roomType == 1:
					self.location = randomCoord()
				self.playerPath.append(self.location)
				config.map.layout[self.location[0]][self.location[1]].playerList.append(self)
				config.map.printMap(self)

	def puzzleReward(self):
		reward = Item(11,'reward')  #ToDo: A real reward
		print("You have won a %s." % reward.name)
		self.addItem(reward)

def generateQuestions():
	ops = ['+', '-', '*', '/', '%']
	# Generate ints for lhs and rhs of question and operator
	seed()
	lhs = randint(2,16)
	rhs = randint(2,16)
	cOps = choice(ops)
	# Choose an operator and generate answer
	if cOps == '+':
		lhs = lhs * randint(2,4)
		rhs = rhs * randint(1,5)
		answer = lhs + rhs
	elif cOps == '-':
		lhs = lhs * randint(2,4)
		rhs = rhs * randint(1,5)
		answer = lhs - rhs
	elif cOps == '/':
		lhs = lhs * randint(2,10)
		answer = int(lhs / rhs)
	elif cOps == '%':
		lhs = lhs * randint(2,10)
		answer = lhs % rhs
	else:
		answer = lhs * rhs
	# Convert lhs, ops, rhs into a question string
	questionString = str(lhs) + cOps + str(rhs) + '= '
	return questionString, str(answer)

def randomCoord():
	"""randomCoord
	returns random coordinate on map.

	Return: (list[int][int]) - coordinates
	"""
	seed()
	return [randint(0,config.ROWS-1), randint(0,config.COLS-1)]



import config
import itertools
from map import Map
from room import Room

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

	#working on better way to handle associating directional keyword with num
	def getKeyByValue(self, value):
		key = ""
		print(DIRECTIONS.values())
		for x in range(0, 4):
			valueList = list(DIRECTIONS.values())[x]
			if value in valueList:
				key = list(DIRECTIONS.keys())[x]
		print("key is", key)
		
	
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
			if self.hasItemByName(itemName):
				curRoom = config.map.layout[self.location[0]][self.location[1]]
				check = curRoom.checkDoor()
				print(check)
				if not check:
					print('There are no locked doors')
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
							print("Invalid direction parameter")
			else:
				print("There is no item called %s in your inventory" % itemName)

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
		
		
		cmd = self.command.split(" ")

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
				self.getItem(cmd[i+1])
				i = len(cmd)	
				break	
			elif s in PossibleUse:
				if len(cmd) > 2:
					self.useItem(cmd[i+1], cmd[i+2])
				elif len(cmd) > 1:
					self.useItem(cmd[i+1], None)
				i = len(cmd)
				break
			elif i == len(cmd)-1:				#no valid commands were found
				print("Please input valid command")

	#Picks up key from room(temporary)
	def getItem(self, itemName):
		curRoom = config.map.layout[self.location[0]][self.location[1]]
		if not curRoom.itemList:
			print("There is no item to get from this room")
		else:
			if curRoom.hasItemByName(itemName):
				self.inventory.append(curRoom.itemList[0])
				curRoom.itemList.pop()
				print("You picked up an item: %s" % itemName)
				self.printInventory()
			else:
				print("There is no item called %s to get from this room" % itemName)

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
		

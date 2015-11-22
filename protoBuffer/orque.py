""" Orque Module

Main module to run orque.

IMPORTANT NOTE:
	- For config.map.layout[x][y] 
		* Something went wrong and (x,y) does signify a Cartesian (x,y) coord,
		  instead x is the row and y is the column
		* Therefore config.map.layout[x][y] is equivalent to Cartesian (y,x) coord
"""

import time
import config
import sys
import os
from player import Player
from room import Room
from map import Map
from item import Item
# from ui import UI
from gpb_pb2 import *

timer = 0


""" Initialize map and rooms """
config.map = Map()
config.map.randomConnectedMap()

""" Initialize and spawn players """
for p in range(0,2):
	tmpPlayer = Player(p)
	config.pL.append(tmpPlayer)
#config.map.layout[0][0].playerList.append(config.pL[0])

""" Spawn key """
key = Item(1,"key")
config.map.layout[config.pL[0].location[0]][config.pL[0].location[1]].itemList.append(key)
#print(config.map.layout[1][0].itemList[0].name)

""" Initial map """
config.map.printMap(0,1)

#UI test
#ui = UI()

def saveGame():

	savefile = raw_input("Please enter a name for the save file: ")
	
	if os.path.exists(savefile):
		response = raw_input("This file already exists. Are you sure you want to overwrite? [Y/n]: ")
		if response is not 'Y':
			print("Game not saved.")
			return
		
	savegame = GameMessage()

	for p in range(len(config.pL)):
		player = savegame.playerList.player.add()
		player.playerId = config.pL[p].playerId
		player.name = config.pL[p].name
		player.health = config.pL[p].health

		for i in config.pL[p].inventory:
			item = player.inventory.item.add()
			item.itemName = i.name
		
		player.location.x = config.pL[p].location[0]
		player.location.y = config.pL[p].location[1]

		for p in config.pL[p].playerPath:
			pathCoord = player.path.location.add()
			pathCoord.x = p[0]
			pathCoord.y = p[1]

	for x in range(len(config.map.layout)):
		for y in range(len(config.map.layout[0])):
			currentRoom = config.map.layout[x][y]
			room = savegame.map.room.add()
			room.location.x = x
			room.location.y = y
			room.adjacencyList.north = currentRoom.adjacencyList[0]
			room.adjacencyList.east = currentRoom.adjacencyList[1]
			room.adjacencyList.south = currentRoom.adjacencyList[2]
			room.adjacencyList.west = currentRoom.adjacencyList[3]
			
			for i in config.map.layout[x][y].itemList:
				item = room.inventory.item.add()
				item.itemName = i.name

			room.type = currentRoom.roomType
			
	f = open(savefile, "wb")
	f.write(savegame.SerializeToString())
	f.close

	print("Game has been saved to: " + savefile)

def loadGame():
	
	savefile = raw_input("Please enter the name of the save file to load: ")

	savegame = GameMessage()
	
	f = open(savefile, "rb")
	savegame.ParseFromString(f.read())
	f.close()

	config.pL = []
	config.map = Map()
	
	for r in savegame.map.room:
		room = Room()

		if r.type is 1:
			room = Room(1)

		for i in r.inventory.item:
			item = Item(0, i.itemName)
			room.itemList.append(item)

		room.adjacencyList[0] = r.adjacencyList.north
		room.adjacencyList[1] = r.adjacencyList.east
		room.adjacencyList[2] = r.adjacencyList.south
		room.adjacencyList[3] = r.adjacencyList.west

		config.map.addRoom(r.location.x, r.location.y, room)

	for p in savegame.playerList.player:
		player = Player(p.playerId)
		player.name = p.name
		player.health = p.health
		
		for i in p.inventory.item:
			item = Item(0, i.itemName)
			player.inventory.append(item)

		player.location[0] = p.location.x
		player.location[1] = p.location.y

		config.map.layout[p.location.x][p.location.y].playerList.append(player)

		for loc in p.path.location:
			player.playerPath.append([loc.x, loc.y])

		config.pL.append(player)

	print("Game has been loaded from: " + savefile)

while True:
	for p in range(len(config.pL)):
		print("Player {0}".format(p))
		config.map.printMap(config.pL[p].playerId)
		command = raw_input("Input command: ").strip()
		if command == "exit":
			sys.exit()
		elif command == "save":
			saveGame()
		elif command == "load":
			loadGame()
			config.map.printMap(0,1)
			break
		else:
			config.pL[p].command = command
			print(config.pL[p].parseCommand())
		#config.pL[p].command = input("Press enter to continue: ")
		#os.system('cls' if os.name == 'nt' else 'clear')

#Timer logic code (To be implemented later)
'''
	if timer < 1:
		timer += 1
		time.sleep(1)
	else:
		for p in range(len(playerList)):
			cmd = playerList[p].command.split(" ")
			print(cmd)
		break
'''

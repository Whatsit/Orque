'''
IMPORTANT NOTE:
	- For config.map.layout[x][y] 
		* Something went wrong and (x,y) does signify a Cartesian (x,y) coord,
		  instead x is the row and y is the column
		* Therefore config.map.layout[x][y] is equivalent to Cartesian (y,x) coord
'''

import time
import config
from player import Player
from room import Room
from map import Map
from item import Item
from ui import UI

timer = 0

#Initialize map and rooms
config.map = Map()
config.map.randomConnectedMap()

#Initialize and spawn players
config.pL = [Player(1,[0,0])]
config.map.layout[0][0].playerList.append(config.pL[0])

#Spawn key
key = Item(1,"key")
config.map.layout[0][1].itemList.append(key)
#print(config.map.layout[1][0].itemList[0].name)

#Initial map
config.map.printMap(1)

#UI test
#ui = UI()


while True:
	config.pL[0].command = input("Input command: ")
	if config.pL[0].command == "exit":
		break
	else:
		config.pL[0].parseCommand()

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

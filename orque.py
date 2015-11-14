'''
IMPORTANT NOTE:
	- For config.map.layout[x][y] 
		* Something went wrong and (x,y) does signify a Cartesian (x,y) coord,
		  instead x is the row and y is the column
		* Therefore config.map.layout[x][y] is equivalent to Cartesian (y,x) coord
'''

import time
import config
import sys
import os
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
for p in range(0,1):
	tmpPlayer = Player(p)
	config.pL.append(tmpPlayer)
#config.map.layout[0][0].playerList.append(config.pL[0])

#Spawn key
key = Item(1,"key")
config.map.layout[config.pL[0].location[0]][config.pL[0].location[1]].itemList.append(key)
#print(config.map.layout[1][0].itemList[0].name)

#Initial map
config.map.printMap(0,1)

#UI test
#ui = UI()


while True:
	for p in range(len(config.pL)):
		print("Player ", p)
		config.map.printMap(config.pL[p].playerId)
		config.pL[p].command = input("Input command: ")
		if config.pL[p].command == "exit":
			sys.exit()
		else:
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

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
from ui import UI
from random import randint, seed, choice

timer = 0


""" Initialize map and rooms """
config.map = Map()
config.map.randomConnectedMap()

""" Initialize and spawn players """
for p in range(0,2):
	tmpPlayer = Player(p)
	config.pL.append(tmpPlayer)

"""	Give players weapen and armor """
for p in config.pL:
	weapon = Item(2,"Rusty_Knife","weapon")
	weapon.effects["weapon"] = 2
	armor = Item(3,"Old_Hardhat","armor")
	armor.effects["armor"] = 2
	potion = Item(4,"Green_Liquid_In_A_Jar","potion")
	potion.effects["health"] = 10
	p.inventory.append(weapon)
	p.inventory.append(armor)
	p.inventory.append(potion)


#config.map.layout[0][0].playerList.append(config.pL[0])

""" Spawn items """
itemContainer = [['Rusty_Knife','weapon'], ['Old_Hardhat','armor'], 
				 ['Green_Liquid_In_A_Jar', 'potion'], ['key', 'key']]

for i in range(0,10):
	seed()
	cItem = choice(itemContainer)
	item = Item(i,cItem[0],cItem[1])
	xPos = randint(0,config.ROWS-1)
	yPos = randint(0,config.COLS-1)
	# Make sure items do not spawn in puzzle room
	while config.map.layout[xPos][yPos].roomType == 1:
		xPos = randint(0,config.ROWS-1)
		yPos = randint(0,config.COLS-1)
	config.map.layout[xPos][yPos].itemList.append(item)
	print(item.name, xPos, yPos)

key = Item(11,"key")
config.map.layout[config.pL[0].location[0]][config.pL[0].location[1]].itemList.append(key)
#print(config.map.layout[1][0].itemList[0].name)

""" Initial map """
config.map.printMap(0,1)

#UI test
#ui = UI()


while True:
	for p in range(len(config.pL)):
		print("Player ", p)
		print(config.map.printMap(config.pL[p].playerId))
		if(len(config.map.layout[config.pL[p].location[0]][config.pL[p].location[1]].playerList) > 1):
			print("WARNING :: There is another player in the room!!!")

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

import time
import config
from player import Player
from room import Room
from map import Map
from item import Item

timer = 0

#Initialize map and rooms
config.map = Map()
config.map.simpleSquareMap()
'''
for i in range(0,3):
	for j in range(0,2):
		config.map.addRoom(i,j,Room())
		config.map.layout[i][j].adjacencyList = [1,1,1,1]

config.map.addRoom(0,0,Room())
config.map.addRoom(1,0,Room())
'''



#Initialize and spawn players
playerList = [Player(1,[0,0])]
config.map.layout[0][0].playerList.append(playerList[0])
'''
playerL = [Player(1,[0,0]), Player(2,[1,0])]
playerL[0].command = "move right"
playerL[1].command = "attack"
#config.map.layout[1][0].playerList.append(playerL[1])
'''

'''
#Modify adjacency list
config.map.layout[0][0].adjacencyList[1] = 1
config.map.layout[1][0].adjacencyList[1] = 1
'''

#Spawn key
key = Item(1,"key")
config.map.layout[1][0].itemList.append(key)
print(config.map.layout[1][0].itemList[0].name)

while True:
	playerList[0].command = input("Input command: ")
	if playerList[0].command == "exit":
		break
	else:
		playerList[0].parseCommand()















	'''
	playerL[0].move(1, False)
	playerL[0].search()
	'''
	

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

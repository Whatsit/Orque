import time
from clusterFck import Player
from clusterFck import Room
from clusterFck import Map

timer = 0

#Initialize map and rooms
Map = Map()
Map.addRoom(0,0,Room())
Map.addRoom(0,1,Room())

#Initialize players
playerL = [Player(1,[0,0]), Player(2,[0,1])]
playerL[0].command = "move right"
playerL[1].command = "attack"


#Spawn players into room
Map.layout[0][0].playerList.append(playerL[0])
Map.layout[0][1].playerList.append(playerL[1])

#Modify adjacency list
Map.layout[0][0].adjacencyList[1] = 1
Map.layout[0][1].adjacencyList[1] = 1


while True:
	playerL[0].move(1, False, Map)
	break
	

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

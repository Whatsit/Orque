import time
import settings
from clusterFck import Player
from clusterFck import Room
from clusterFck import Map

timer = 0

#Initialzie global
settings.init()

#Initialize map and rooms
settings.mapContainer.append(Map())
settings.mapContainer[0].addRoom(0,0,Room())
settings.mapContainer[0].addRoom(0,1,Room())

#Initialize players
playerL = [Player(1,[0,0]), Player(2,[0,1])]
playerL[0].command = "move right"
playerL[1].command = "attack"


#Spawn players into room
settings.mapContainer[0].layout[0][0].playerList.append(playerL[0])
settings.mapContainer[0].layout[0][1].playerList.append(playerL[1])

#Modify adjacency list
settings.mapContainer[0].layout[0][0].adjacencyList[1] = 1
settings.mapContainer[0].layout[0][1].adjacencyList[1] = 1


while True:
	playerL[0].move(1, False)
	break
	


	if timer < 1:
		timer += 1
		time.sleep(1)
	else:
		for p in range(len(playerList)):
			cmd = playerList[p].command.split(" ")
			print(cmd)
		break


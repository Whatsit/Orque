import socket
import time
import config
import sys
import os
from player import Player
from room import Room
from map import Map
from item import Item
from threading import Thread

def handler(connect, player):
	while True:
		#recv client command
		response = connect.recv(1024).decode()
		
		if(response):
			if not response:
				break;
			else:
				print ("Player ", player, " : ",response)
				if(response == 'exit'):
					print ("Player ", player, 'has rage quit')
					break;
				else:
					#process commands
					config.pL[int(player)].command = response
					res = config.pL[int(player)].parseCommand()
					connect.send(res.encode())
	connect.close()
	
if __name__ == '__main__':
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((config.host, int(config.port)))

	serverIP = socket.gethostbyname(socket.gethostname())
	print ('server started on ', serverIP, ':', config.port)
	server.listen(5)

	playerCount = 0
	timer = 0

	""" Initialize map and rooms """
	config.map = Map()
	config.map.randomConnectedMap()

	""" Initialize and spawn players """
	for p in range(0,1):
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

	""" Spawn key """
	key = Item(1,"key","key")
	config.map.layout[config.pL[0].location[0]][config.pL[0].location[1]].itemList.append(key)
	#key = Item(2,"key")
	#config.map.layout[config.pL[1].location[0]][config.pL[1].location[1]].itemList.append(key)
	#print(config.map.layout[1][0].itemList[0].name)
	
	while True:
		connect, address = server.accept()
		print('New Connection', address)
		print(address, "is Player ", playerCount)
		
		#send hello
		msg = 'welcome to orque'
		connect.send(msg.encode())
		
		tmpPlayer = Player(playerCount)
		config.pL.append(tmpPlayer)
		config.map.printMap(0,1)
		
		thread = Thread(target=handler, args=(connect, playerCount))
		thread.start()
		
		playerCount += 1
	server.close()


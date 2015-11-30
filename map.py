""" Map Module

This module contains the layout for the map. It has a function to
randomly generate a map. The Map class also handles printing the map.

"""

import config
from room import Room
from random import randint
from lib.termcolor import colored
from lib.colorama import init
init()

ROWS = config.ROWS
COLS = config.COLS

class Map:
	""" Map Class

	Attributes:
	* layout (list [int][int]) - A 2d array of integer for room coordinates
	"""
	def __init__(self):
		""" Default constructor

		Initializes layout.
		"""
		self.layout = [[0 for x in range(COLS)] for x in range(ROWS)]
		print(self.layout)

	def addRoom(self,x,y,pRoom):
		""" addRoom

		Parameters:
		* x (int) - x coordinate
		* y (int) - y coordinate
		* pRoom (room) - instance of room to add
		"""
		self.layout[x][y] = pRoom

	def randomConnectedMap(self):
		""" randomConnectedMap

		Randomly generated connected map with dimensions ROWSxCOLS
		"""
		print("Generating random connected map")

		tmpPuzzleRoomCoord = []
		onHold = 0

		for i in range(ROWS):
			for j in range(COLS):
				boolBreakConstraint = False

				if onHold > 0:
					x = 90
				else:
					x = randint(1,100)  # Decide on room type

				if x >= 90:
					# Checks if room to be added is within 1 space of a puzzle room
					for pRC in tmpPuzzleRoomCoord:
						if manhattanDist([i,j],pRC) <= 2:
							self.addRoom(i,j,Room())
							boolBreakConstraint = True
							onHold += 1
							break
					if boolBreakConstraint == False:
						self.addRoom(i,j,Room(1))  # Initialize puzzle room
						tmpPuzzleRoomCoord.append([i,j])  # Temporarily store puzzle room coord in puzzle list ""
						onHold = 0
				else:
					self.addRoom(i,j,Room())  # Initialize normal room

				# Randomly initialize room adjacencies

				#	0 - North adjacency
				#	1 - East adjacency
				#	2 - South adjacency
				#	3 - Weset adjacency

				if i == 0:
					self.layout[i][j].adjacencyList[0] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[0] = 2
					self.layout[i-1][j].adjacencyList[2] = 2
				else:
					self.layout[i][j].adjacencyList[0] = self.layout[i-1][j].adjacencyList[2]
				if j == COLS-1:
					self.layout[i][j].adjacencyList[1] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[1] = 2
				else:
					self.layout[i][j].adjacencyList[1] = randint(0,1)
				if i == ROWS-1:
					self.layout[i][j].adjacencyList[2] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[2] = 2
				else:
					self.layout[i][j].adjacencyList[2] = randint(0,1)
				if j == 0:
					self.layout[i][j].adjacencyList[3] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[3] = 2
					self.layout[i][j-1].adjacencyList[1] = 2
				else:
					self.layout[i][j].adjacencyList[3] = self.layout[i][j-1].adjacencyList[1]
				#""" there must be at least 1 corridor """
				if self.layout[i][j].adjacencyList[1] == 0 and self.layout[i][j].adjacencyList[2] == 0 and i != ROWS-1 and j != COLS-1:
					self.layout[i][j].adjacencyList[randint(1,2)] = 1
		"""
		#Debug
		for i in range(ROWS):
			for j in range(COLS):
				print(self.layout[i][j].adjacencyList, end = '')
			print()
		for i in range(len(tmpPuzzleRoomCoord)):
			print(tmpPuzzleRoomCoord[i])
		"""

		return tmpPuzzleRoomCoord

	def printMap(self,p,type=0):
		""" printMap

		Prints the map. Red lines denote a locked door. Blue lines denote the player.
		As the player explores, more lines on the map appear corresponding to the places
		that the player has been at.
		"""
		for i in range(ROWS):
			topLine = ""
			midLine = ""
			botLine = ""
			for j in range(COLS):
				if type == 1 or [i,j] in p.playerPath:
					#""" Top line North """
					if self.layout[i][j].adjacencyList[0] == 1:
						topLine += " | "
					elif self.layout[i][j].adjacencyList[0] == 2:
						topLine += colored(" | ", "blue")
					else:
						topLine += "   "
					#""" Mid line West """
					if self.layout[i][j].adjacencyList[3] == 1:
						midLine += "-"
					elif self.layout[i][j].adjacencyList[3] == 2:
						midLine += colored("-", "blue")
					else:
						midLine += " "
					#""" Mid line Room """
					if self.layout[i][j].roomType == 0:
						if not self.layout[i][j].playerList:
							midLine += "N"
						else:
							midLine += colored("N", "red")
					else:
						if not self.layout[i][j].playerList:
							midLine += colored("P", "blue")
						else:
							midLine += colored("P", "white")
					#""" Mid line East """
					if self.layout[i][j].adjacencyList[1] == 1:
						midLine += "-"
					elif self.layout[i][j].adjacencyList[1] == 2:
						midLine += colored("-", "blue")
					else:
						midLine += " "
					#""" Bot line South """
					if self.layout[i][j].adjacencyList[2] == 1:
						botLine += " | "
					elif self.layout[i][j].adjacencyList[2] == 2:
						botLine += colored(" | ", "blue")
					else:
						botLine += "   "
				#""" if player has not visited location leave it blank """
				else:
					topLine += '   '
					midLine += '   '
					botLine += '   '
			print(topLine)
			print(midLine)
			print(botLine)

	def validateGenRanMap(self,trials):
		check = None
		for i in range(0,trials):
			check = map.randomConnectedMap()
			print(check)
			for j in range(len(check)):
				for k in range(len(check)):
					if j == k:
						continue
					elif manhattanDist(check[j],check[k]) <= 2:
						print("GenRanMap violated constraint")
						return
		print("GenRanMap satisfied constraint")

def manhattanDist(p1,p2):
	dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
	#print(dist)
	return dist


if __name__ == "__main__":
    map = Map()
    map.validateGenRanMap(10)

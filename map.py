import config
from room import Room
from random import randint
from lib.termcolor import colored
from lib.colorama import init
init()

ROWS = 5
COLS = 10

""" Map Module

This module contains the layout for the map. It has a function to
randomly generate a map. The Map class also handles printing the map.

"""
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

		for i in range(ROWS):
			for j in range(COLS):
				""" Decide on room type """
				x = randint(1,100)
				if x >= 90:
					self.addRoom(i,j,Room(1))	""" Initialize puzzle room """
				else:
					self.addRoom(i,j,Room())	""" Initialize normal room """

				""" Randomly initialize room adjacencies """
				""" 
					0 - North adjacency
					1 - East adjacency
					2 - South adjacency
					3 - Weset adjacency
				"""
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
				""" there must be at least 1 corridor """
				if self.layout[i][j].adjacencyList[1] == 0 and self.layout[i][j].adjacencyList[2] == 0 and i != ROWS-1 and j != COLS-1:
					self.layout[i][j].adjacencyList[randint(1,2)] = 1
		""" Debug """
		for i in range(ROWS):
			for j in range(COLS):
				print(self.layout[i][j].adjacencyList, end = '')
			print()
		print()


	def printMap(self):
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
				if [i,j] in config.pL[0].playerPath:

					""" Top line North """
					if self.layout[i][j].adjacencyList[0] == 1:
						topLine += " | "
					elif self.layout[i][j].adjacencyList[0] == 2:
						topLine += colored(" | ", "red")
					else:
						topLine += "   "
					""" Mid line West """
					if self.layout[i][j].adjacencyList[3] == 1:
						midLine += "-"
					elif self.layout[i][j].adjacencyList[3] == 2:
						midLine += colored("-", "red")
					else:
						midLine += " "
					""" Mid line Room """
					if self.layout[i][j].roomType == 0:
						if not self.layout[i][j].playerList:
							midLine += "N"
						else:
							midLine += colored("N", "red")
					else:
						if not self.layout[i][j].playerList:
							midLine += "P"
						else:
							midLine += colored("P", "blue")
					""" Mid line East """
					if self.layout[i][j].adjacencyList[1] == 1:
						midLine += "-"
					elif self.layout[i][j].adjacencyList[1] == 2:
						midLine += colored("-", "red")
					else:
						midLine += " "
					""" Bot line South """
					if self.layout[i][j].adjacencyList[2] == 1:
						botLine += " | "
					elif self.layout[i][j].adjacencyList[2] == 2:
						botLine += colored(" | ", "red")
					else:
						botLine += "   "
				""" if player has not visited location leave it blank """
				else:
					topLine += '   '
					midLine += '   '
					botLine += '   '

			print(topLine)
			print(midLine)
			print(botLine)

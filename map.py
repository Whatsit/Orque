import config
from room import Room
from random import randint
from lib.termcolor import colored
from lib.colorama import init
init()

ROWS = 5
COLS = 10

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(COLS)] for x in range(ROWS)]
		print(self.layout)

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom

	#Randomly generated connected map with dimensions ROWSxCOLS
	def randomConnectedMap(self):
		print("Generating random connected map")

		for i in range(ROWS):
			for j in range(COLS):
				#Decide on room type
				x = randint(1,100)
				if x >= 90:
					self.addRoom(i,j,Room(1))	#Initialize puzzle room
				else:
					self.addRoom(i,j,Room())	#Initialize normal room

				#Randomly initialize room adjacencies
				#North adjacency
				if i == 0:
					self.layout[i][j].adjacencyList[0] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[0] = 2
					self.layout[i-1][j].adjacencyList[2] = 2
				else:
					self.layout[i][j].adjacencyList[0] = self.layout[i-1][j].adjacencyList[2]
				#East adjacency
				if j == COLS-1:
					self.layout[i][j].adjacencyList[1] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[1] = 2
				else:
					self.layout[i][j].adjacencyList[1] = randint(0,1)
				#South adjacency
				if i == ROWS-1:
					self.layout[i][j].adjacencyList[2] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[2] = 2
				else:
					self.layout[i][j].adjacencyList[2] = randint(0,1)
				#West adjacency
				if j == 0:
					self.layout[i][j].adjacencyList[3] = 0
				elif self.layout[i][j].roomType == 1:
					self.layout[i][j].adjacencyList[3] = 2
					self.layout[i][j-1].adjacencyList[1] = 2
				else:
					self.layout[i][j].adjacencyList[3] = self.layout[i][j-1].adjacencyList[1]
				#atleast 1 corridor
				if self.layout[i][j].adjacencyList[1] == 0 and self.layout[i][j].adjacencyList[2] == 0 and i != ROWS-1 and j != COLS-1:
					self.layout[i][j].adjacencyList[randint(1,2)] = 1
		#Debug
		for i in range(ROWS):
			for j in range(COLS):
				print(self.layout[i][j].adjacencyList, end = '')
			print()
		print()


	def printMap(self):
		for i in range(ROWS):
			topLine = ""
			midLine = ""
			botLine = ""
			for j in range(COLS):
				#Top line North
				if self.layout[i][j].adjacencyList[0] == 1:
					topLine += " | "
				elif self.layout[i][j].adjacencyList[0] == 2:
					topLine += colored(" | ", "red")
				else:
					topLine += "   "
				#Mid line West
				if self.layout[i][j].adjacencyList[3] == 1:
					midLine += "-"
				elif self.layout[i][j].adjacencyList[3] == 2:
					midLine += colored("-", "red")
				else:
					midLine += " "
				#Mid line Room
				if self.layout[i][j].roomType == 0:
					if not self.layout[i][j].playerList:
						midLine += "N"
					else:
						midLine += colored("N", "red")
				else:
					midLine += "P"
				#Mid line East
				if self.layout[i][j].adjacencyList[1] == 1:
					midLine += "-"
				elif self.layout[i][j].adjacencyList[1] == 2:
					midLine += colored("-", "red")
				else:
					midLine += " "
				#Bot line South
				if self.layout[i][j].adjacencyList[2] == 1:
					botLine += " | "
				elif self.layout[i][j].adjacencyList[2] == 2:
					botLine += colored(" | ", "red")
				else:
					botLine += "   "
				#

			print(topLine)
			print(midLine)
			print(botLine)
			#print(config.pL[0].playerPath)

'''
	#Simple ROWSxCOLS map with a puzzle room in the middle
	def simpleSquareMap(self):
		print(self.layout)
		for i in range(ROWS):
			for j in range(COLS):
				#print(i,j)
				self.addRoom(i,j,Room())
				if j == 0:
					self.layout[i][j].adjacencyList[0] = 0
					#print("No North")
				if i == COLS-1:
					self.layout[i][j].adjacencyList[1] = 0
					#print("No East")
				if j == ROWS-1:
					self.layout[i][j].adjacencyList[2] = 0
					#print("No South")
				if i == 0:
					self.layout[i][j].adjacencyList[3] = 0
					#print("No West")
				#print(self.layout[i][j].adjacencyList)
		#Set puzzle room at [1,1]
		self.layout[1][1].roomType = 1
		self.layout[1][1].adjacencyList[0] = 2
		self.layout[1][1].adjacencyList[1] = 2
		self.layout[1][1].adjacencyList[2] = 2
		self.layout[1][1].adjacencyList[3] = 2
		#Other room connections
		self.layout[1][0].adjacencyList[2] = 2
		self.layout[2][1].adjacencyList[3] = 2
		self.layout[1][2].adjacencyList[0] = 2
		self.layout[0][1].adjacencyList[1] = 2
<<<<<<< Updated upstream
=======
'''
#>>>>>>> Stashed changes

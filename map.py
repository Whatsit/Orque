from room import Room
from random import randint

ROWS = 3
COLS = 3

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(ROWS)] for x in range(COLS)]

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom

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

	#Randomly generated connected map with dimensions ROWSxCOLS 
	def randomConnectedMap(self):
		print("Generating random connected map")
		
		for i in range(ROWS):
			for j in range(COLS):
				#Initialize room
				self.addRoom(i,j,Room())
				#Randomly initialize room adjacencies
				#North adjacency
				if j == 0:
					self.layout[i][j].adjacencyList[0] = 0
				else:
					self.layout[i][j].adjacencyList[0] = self.layout[i][j-1].adjacencyList[2]
				#East adjacency
				if i == COLS-1:
					self.layout[i][j].adjacencyList[1] = 0
				else:
					self.layout[i][j].adjacencyList[1] = randint(0,2)
				#South adjacency
				if j == ROWS-1:
					self.layout[i][j].adjacencyList[2] = 0
				else:
					self.layout[i][j].adjacencyList[2] = randint(0,2)
				#West adjacency
				if i == 0:
					self.layout[i][j].adjacencyList[3] = 0
				else:
					self.layout[i][j].adjacencyList[3] = self.layout[i-1][j].adjacencyList[1]


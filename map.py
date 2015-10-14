from room import Room

MAPSIZE = 3 

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(MAPSIZE)] for x in range(MAPSIZE)]

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom

	#Simple 3x3 map with a puzzle room in the middle	
	def simpleSquareMap(self):
		print(self.layout)
		for i in range(MAPSIZE):
			for j in range(MAPSIZE):
				#print(i,j)
				self.addRoom(i,j,Room())
				if j == 0:
					self.layout[i][j].adjacencyList[0] = 0
					#print("No North")
				if i == MAPSIZE-1:
					self.layout[i][j].adjacencyList[1] = 0
					#print("No East")
				if j == MAPSIZE-1:
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



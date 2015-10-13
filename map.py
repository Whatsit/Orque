from room import Room

MAPSIZE = 3 

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(MAPSIZE)] for x in range(MAPSIZE)]

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom

	def simpleSquareMap(self):
		print(self.layout)
		for i in range(MAPSIZE):
			for j in range(MAPSIZE):
				print(i,j)
				self.addRoom(i,j,Room())
				if j == 0:
					self.layout[i][j].adjacencyList[0] = 0
					print("No North")
				if i == MAPSIZE-1:
					self.layout[i][j].adjacencyList[1] = 0
					print("No East")
				if j == MAPSIZE-1:
					self.layout[i][j].adjacencyList[2] = 0
					print("No South")
				if i == 0:
					self.layout[i][j].adjacencyList[3] = 0
					print("No West")
				print(self.layout[i][j].adjacencyList)

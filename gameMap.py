MAPSIZE = 3 

class Map:
	def __init__(self):
		self.layout = [[0 for x in range(MAPSIZE)] for x in range(MAPSIZE)]

	def addRoom(self,x,y,pRoom):
		self.layout[x][y] = pRoom
MAPSIZE = 3 

class Map:
	def __init__(self):
		self.layout = [[for x in range(MAPSIZE)] for x in range(MAPSIZE)]

	def addRoom(x,y,pRoom):
		layout[x][y] = pRoom
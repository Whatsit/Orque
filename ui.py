""" UI Module

Handles UI for Orque
"""
from tkinter import *
import config

class UI:
	"""UI class"""
	def __init__(self):
		""" Default Constructor 
		
		Initializes buttons and UI frame
		"""
		root = Tk()
		#root.resizable(width=FALSE, height=FALSE)
		#root.geometry('{}x{}'.format(200, 100))

		self.output = ""

		frame = Frame(root)
		frame.pack()
		root.title("Orque")
		# Quit button
		self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.button.pack(side = LEFT)
		# Command entry form
		self.form = Entry(frame)
		self.form.pack(side = LEFT)
		# Enter button
		self.entryButton = Button(frame, text="Enter", fg="green", command=self.setCommand)
		self.entryButton.pack(side=LEFT)
		# Text field and scroll bar
		self.scrollbar = Scrollbar(root)
		self.textField = Listbox(root, height=20, width=50)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.textField.pack(side=LEFT, fill=Y)
		self.scrollbar.config(command=self.textField.yview)
		self.textField.config(yscrollcommand=self.scrollbar.set)
		self.textField.insert(END, self.output)
		# Text field for map
		self.mapField = Text(root, height=config.ROWS*3, width=config.COLS*3)
		self.mapField.pack(side=BOTTOM, fill=Y)
		# Text field for map legend
		self.mapLegend = Listbox(root, width=36)
		self.mapLegend.pack(side=BOTTOM, fill=Y)
		self.mapLegend.insert(END, "MAP LEGEND")
		self.mapLegend.insert(END, "----------")
		self.mapLegend.insert(END, "X - Occupied room")
		self.mapLegend.insert(END, "O - Unoccupied room")
		self.mapLegend.insert(END, "# - Blocked hallway (requires a key)")
		self.mapLegend.insert(END, "P - Puzzle room")
		self.mapLegend.insert(END, "@ - Occupied puzzle room")
		# Stats box
		self.statsBox = Listbox(root, height = 8, width = 20)
		self.updateStats()
		self.statsBox.pack(side=BOTTOM, fill=X)
		# Key bindings
		root.bind("<Return>", self.ReturnPressed)

		self.uiPrintMap(0, 1)
		root.mainloop()
		root.destroy()
	
	def setCommand(self):
		""" setCommand 
		
		sets command of player = to what user types in ui form.
		"""
		config.pL[0].command = self.form.get()
		self.form.delete(0, END)
		self.textField.insert(0, config.pL[0].command)
		outputString = config.pL[0].parseCommand()
		if '@' in outputString:
			outputString = outputString.split('@')
			for string in outputString[::-1]:
				self.textField.insert(0, string)
		else:
			self.textField.insert(0, outputString)
		self.mapField.delete('1.0', 'end')
		self.uiPrintMap(0)
		self.updateStats()
		
	def updateStats(self):
		""" updateStats
		
		Updates the stats section of the UI.
		"""
		self.statsBox.delete(0, END)
		self.statsBox.insert(END, "PLAYER STATS")
		self.statsBox.insert(END, "------------")
		self.statsBox.insert(END, "Health:  " + str(config.pL[0].health))
		self.statsBox.insert(END, "Attack Range:  " + str(config.pL[0].attackRange[0]) + " to " + str(config.pL[0].attackRange[1]))
		self.statsBox.insert(END, "Defense:  " + str(config.pL[0].protection))
		self.statsBox.insert(END, "Attack Bonus: " + str(config.pL[0].attackBonus))
		self.statsBox.insert(END, "Outfit:  " + str(config.pL[0].outfit))
		self.statsBox.insert(END, "Weapon:  " + str(config.pL[0].weapon))

	def ReturnPressed(self, event):
		self.setCommand()
		# Clear text from entry widget
		self.form.delete(0, "end")

	def uiPrintMap(self, playerID, type=0):
		""" uiPrintMap
		
		Prints the map to the UI.
		"""
		uiMap = ""
		for i in range(config.ROWS):
			topLine = ""
			midLine = ""
			botLine = ""
			for j in range(config.COLS):
				if [i,j] in config.pL[playerID].playerPath or type == 1:
					#""" Top line North """
					if config.map.layout[i][j].adjacencyList[0] == 1:
						topLine += " | "
					elif config.map.layout[i][j].adjacencyList[0] == 2:
						topLine += " # "
					else:
						topLine += "   "
					#""" Mid line West """
					if config.map.layout[i][j].adjacencyList[3] == 1:
						midLine += "-"
					elif config.map.layout[i][j].adjacencyList[3] == 2:
						midLine += "#"
					else:
						midLine += " "
					#""" Mid line Room """
					if config.map.layout[i][j].roomType == 0:
						if not config.map.layout[i][j].playerList:
							midLine += "O"
						else:
							midLine += "X"
					else:
						if not config.map.layout[i][j].playerList:
							midLine += "P"
						else:
							midLine += "@"
					#""" Mid line East """
					if config.map.layout[i][j].adjacencyList[1] == 1:
						midLine += "-"
					elif config.map.layout[i][j].adjacencyList[1] == 2:
						midLine += "#"
					else:
						midLine += " "
					#""" Bot line South """
					if config.map.layout[i][j].adjacencyList[2] == 1:
						botLine += " | "
					elif config.map.layout[i][j].adjacencyList[2] == 2:
						botLine += " # "
					else:
						botLine += "   "
				#""" if player has not visited location leave it blank """
				else:
					topLine += '   '
					midLine += '   '
					botLine += '   '
			uiMap += topLine
			uiMap += midLine
			uiMap += botLine
		self.mapField.insert(END, uiMap)

""" UI Module

Handles UI for Orque
"""
from tkinter import *
from player import Player
import config

<<<<<<< HEAD
class UI:
	"""UI class"""
=======

class UI:
	"""UI class
	"""
>>>>>>> refs/remotes/Whatsit/master
	def __init__(self):
		""" Default Constructor 
		
		Initializes buttons and UI frame
		"""
		root = Tk()
		#root.resizable(width=FALSE, height=FALSE)
		#root.geometry('{}x{}'.format(200, 100))

		self.output = StringVar()

		frame = Frame(root)
		frame.pack()

		self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.button.pack(side = LEFT)

		self.form = Entry(frame)
		self.form.pack(side = LEFT)

		self.entryButton = Button(frame, text="Enter", fg="green", command=self.setCommand)
		self.entryButton.pack(side=LEFT)

		self.form2 = Entry(frame, text = self.output, width = 100)
		self.form2.pack(side = LEFT)

		root.mainloop()
		root.destroy()
<<<<<<< HEAD
	
	def setCommand(self):
		""" setCommand 
		
=======

	def setCommand(self):
		"""setCommand() Peramiters: None
>>>>>>> refs/remotes/Whatsit/master
		sets command of player = to what user types in ui form.
		"""
		config.pL[0].command = self.form.get()
		outputString = config.pL[0].parseCommand()
		self.output.set(outputString)

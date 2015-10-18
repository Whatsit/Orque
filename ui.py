from tkinter import *
from player import Player
import config

class UI:
	def __init__(self):
		root = Tk()

		frame = Frame(root)
		frame.pack()

		self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.button.pack(side=LEFT)

		self.hello = Button(frame, text="Hello", command=self.printHello)
		self.hello.pack(side=LEFT)

		self.moveN = Button(frame, text="North", fg="red",command=self.moveNorth)
		self.moveN.pack(side=LEFT)

		self.moveE = Button(frame, text="East", fg="red",command=self.moveEast)
		self.moveE.pack(side=LEFT)

		self.moveS = Button(frame, text="South", fg="red",command=self.moveSouth)
		self.moveS.pack(side=LEFT)

		self.moveW = Button(frame, text="West", fg="red",command=self.moveWest)
		self.moveW.pack(side=LEFT)

		root.mainloop()
		root.destroy()

	def printHello(self):
		print("Hello everybody")

	def moveNorth(self):
		config.pL[0].move(0,False)

	def moveEast(self):
		config.pL[0].move(1,False)

	def moveSouth(self):
		config.pL[0].move(2,False)

	def moveWest(self):
		config.pL[0].move(3,False)

		
		'''
		self.root = Tk()
		w = Label(self.root, text = "Hello World!")
		w.pack()
		self.root.mainloop()
		'''
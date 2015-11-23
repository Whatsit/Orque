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
		# Key bindings
		root.bind("<Return>", self.ReturnPressed)

		root.mainloop()
		root.destroy()
	
	def setCommand(self):
		""" setCommand 
		
		sets command of player = to what user types in ui form.
		"""
		config.pL[0].command = self.form.get()
		self.textField.insert(0, config.pL[0].command)
		outputString = config.pL[0].parseCommand()
		self.textField.insert(0, outputString)

	def ReturnPressed(self, event):
		self.setCommand()
		# Clear text from entry widget
		self.form.delete(0, "end")

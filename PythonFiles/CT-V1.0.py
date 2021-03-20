from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from random import *
import pickle
import ctuser
try:
	import pygame
except:
	print("Please install pygame")
	print("http://www.pygame.org/download.shtml")
	quit()

class Login():
	def __init__(self, root):
		self.root = root
		root.title("CT-Login")
		root.resizable(width=FALSE, height=FALSE)
		root.geometry("1000x1000+400+20")
		self.frame = Frame(root, height=1000, width=1000)
		self.frame.pack()
		self.canvas = Canvas(frame, width=1000, height=1000)
		self.canvas.pack()

class NewUser():
	def __init__(self, root):
		self.root = root
		root.title("CT-New User")
		root.resizable(width=FALSE, height=FALSE)
		root.state("zoomed")
		root.geometry("1000x1000+400+20")
		self.frame = Frame(root, height=1000, width=1000)
		self.frame.pack()

class CTUser():
	def __init__(self, root):
		self.root = root
		root.title("Climb Time")
		root.resizable(width=FALSE, height=FALSE)
		root.state("zoomed")
		root.geometry("1000x1000+400+20")
		self.frame = Frame(root, height=1000, width=1000)
		self.frame.pack()


if __name__ == "__main__":
	root = Tk()
	Login(root)
	root.mainloop()
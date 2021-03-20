import sys
import itertools
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar



path = open("ctusers.txt", "r")
test = open("test.txt", "w")
dict = {}
recomp = {}

for line in path:
	if (line.strip().startswith("#")):
		continue
	else:	
		user, xpcur, xpmax, vmax, cmax, cgrp, notes, awards, chist = line.split(" : ")
		dict[user.strip()] = [xpcur.strip(), xpmax.strip(), vmax.strip(), cmax.strip(), cgrp.strip(), notes.strip(), awards.strip().split("."), chist.strip().split("!")]

def recompilewriter ():	#change test to ctusers
	for key in dict.keys():	
		test.write(str(key) + " : ")# + str(dict[key]))
		dacount = 0
		for value in dict[key]:
			if (dacount == 6):
				for item in (dict[key][6]):
					location = (dict[key][6])
					if (item == (location[-1])):
						test.write(str(item)) 
					else:
						test.write(str(item + "."))
				test.write(" : ")
				dacount += 1
			elif (dacount == 7):
				if (value == 'None'): 
					test.write("None")
					dacount += 1
				else:
					for item in (dict[key][7]):
						location = (dict[key][7]) 
						if (item == (location[-1])):
							test.write(str(item))
						else:
							test.write(str(item) + "!")
					dacount += 1
			else:
				test.write(str(value) + " : ")
				dacount += 1
		test.write("\n")


		
			
class MainGUI(tk.Tk):
	

	def __init__(self):
		tk.Tk.__init__(self)
		self.logingui()
		
	def exiting (self,parent):
		eliminate = parent.destroy()
		
	def logingui (self):
		self.title("CT-Login")
		self.geometry("250x80+800+400")
		 
		self.uservar = StringVar()
		self.passvar = StringVar()
		
		self.label = tk.Label(self, text="User")
		self.label.grid(row=0, column=0, columnspan=2, sticky=E)
		self.label2 = tk.Label(self, text="Password")
		self.label2.grid(row=1, column=0, columnspan=2, sticky=E)
		
		self.userentry = tk.Entry(self, textvariable=self.uservar)
		self.userentry.grid(row=0, column=2, columnspan=2)
		self.userentry.bind("<Return>", self.userlogin)
		self.passwordentry = tk.Entry(self, textvariable=self.passvar, show = '\u047B')#u0488, u0468, u0466,u047A, u047B, u0489, u220E
		self.passwordentry.bind("<Return>", self.userlogin)
		self.passwordentry.grid(row=1, column=2, columnspan=2)
		
		self.userbutton = tk.Button(self, text=" Enter ")
		self.userbutton.grid(row=0, column=5)
		self.userbutton.bind("<Button-1>", self.userlogin)
		self.exitbutton = tk.Button(self, text=" -- Exit -- ")
		self.exitbutton.grid(row=2, column=2, columnspan=2)
		self.exitbutton.bind("<Button-1>", self.exiting)		
		self.createbutton = tk.Button(self, text="Create")
		self.createbutton.grid(row=1, column=5, columnspan=1)
		
	def userwindow (self,user): 
		self.exiting(self)#closes login window
		
		def escape (self):
			anahilate = uw.destroy()
			
		######user stats######
		xpcur = dict[user][0]
		xpmax = dict[user][1]
		vmax = dict[user][2]
		cmax = dict[user][3]
		cgrp = dict[user][4]
		notes = dict[user][5]
		awards = dict[user][6]
		chist = dict[user][7]
		
		climbvalues = {"5":"1","6":"2","7":"3","8":"4","9":"8","10":"10","11":"20","12":"30","13":"55","14":"90","15":"200"}
		vbouldervalues = {"0":"1","1":"2","2":"4","3":"8","4":"10","5":"20","6":"30","7":"37","8":"55","9":"65","10":"70","11":"75","12":"80","13":"85","14":"90","15":"110"}
		bbouldervalues = {"0":"1","1":"5","2":"10","3":"40","4":"80"}
		awardvalues = {"vm":"100","st":"100","mt":"500","bt":"2000","gt":"100000","sc":"20","mc":"50","lc":"100","xlc":"500","xxlc":"1000","xxxlc":"2000","ic":"5000","sttr":"50","sttr2":"2000","sttr3":"5000","sttr4":"15000","staff":"50"}
				
		def climbnum (climbs):
			if (chist[0] == "None"):
				return(0)
			else:
				return(len(chist))
		cnum = climbnum(chist)
		
		def xpadder (addition):
			toadd = addition
			xp = 0
			climbs = []
			subgrades = ["a", "b", "c", "d"]
			for item in chist:
				boulders = item[1:]
				if item[0] == "V":
					if boulders == "b":
						xp += 1
					elif int(boulders) > 15:
						xp += 110
					else:
						xp += int(vbouldervalues[boulders])
				elif item[0] == "B":
					if int(boulders) > 4:
						xp += 80
					else:
						xp += int(bbouldervalues[boulders])
				elif item[0] == "5":
					letter = item[-1]
					if letter in subgrades:
						difficulty = item[2:-1]
						climbs.append(difficulty)
					else:
						climbs.append(item[2:])
				else:
					continue
			for diff in climbs:
				if int(diff) < 5:
					xp += 1
				elif int(diff) > 15:
					xp += 200
				else:
					xp += int(climbvalues[diff])
			for item in awards:
				if item == "None":
					continue
				elif item == "cheat":
					dict[user][0] = 0
					del dict[user][6][:]
					dict[user][6] = "cheat"
					xp = 0
					break
				else:
					xp += int(awardvalues[item])
			return(xp)
		cumlativexp = xpadder(chist)
		
		def xpmaxx (highxp):
			if (int(cumlativexp) < int(xpmax)):
				return(xpmax)
			else:
				dict[user][1] = int(cumlativexp)
				return(int(cumlativexp))
		highestxp = xpmaxx(xpcur)
		
		def vmaxx (climbs):
			blist = []
			vlist = []
			for item in chist:
				if item[0] == "B":
					blist.append(int(item[1:]))
				elif item[0] == "V":
					if item[1] == "b":
						vlist.append(0)
						continue
					vlist.append(int(item[1:]))
				else:
					continue
			if len(vlist) == 0:
				vlist = [0]
			if len(blist) == 0:
				blist = [0]
			vm = max(vlist)
			bm = max(blist)		
			if (vm + bm) == 0:
				dict[user][2] = ("None")
				return("None")
			elif (float(bm) * 2.5) > (float(vm)):
				dict[user][2] = ("B" + str(bm))
				return("B" + str(bm))
			else:
				dict[user][2] = ("V" + str(vm))
				return("V" + str(vm))
		bouldergrade = vmaxx(chist)
		
		def cmaxx (climbgrade):
			cdict = {}
			subgrades = ["a", "b", "c", "d"]#assign value to subgrades
			for item in chist:
				if (item[0]) == "5":
					letter = item[-1]
					#difficulty = int(item[2:-1])
					if len(item) == 3:
						difficulty = int(item[2:])
					else:
						difficulty = int(item[2:-1])
					if letter in subgrades:
						if difficulty in cdict.keys():
							if str(letter) > str(cdict[difficulty]):
								cdict[difficulty] = (letter)
							else:
								continue
						else:
							cdict[difficulty] = (letter)
					else:
						cdict[int(item[2:])] = ""
				else:
					continue
			if len(cdict) == 0:
				dict[user][3] = ("None")
				return("None")
			else:
				cm = max(cdict.keys())
				cdvalue = list(cdict.values())
				dict[user][3] = ("5." + str(cm))
				return("5." + str(cm) + cdict[cm])
		climbgrade = cmaxx(chist)
		
		#def climbergroup (group):

		#def notetaker (note):

		#def awarder (award):
		
		def climberlevel (xp):
			if (xp <= 50):
				lvl = int(xp / 5)
				return(lvl)
			else:
				lvl = 0
				exp = ((int(xp) / 50) * 1.1) #might need to subtract 50xp from xp before division
				while((exp / 1.1) >= 1):
					exp /= 1.1
					lvl += 1
				return(int(lvl) + 9)
		level = climberlevel(int(cumlativexp))			

		#def xploser (lastclimb):
			
		#def ranker (climber):
		rank = "null" #ranker(xpcur)
		
		
		######user window gui######		
		uw = tk.Tk()#starts a new window
		uw.title(str(user) + ":  Climb Time")
		uw.geometry("1500x900+260+150")
		####Labels for climber stats####
		uw.userlabel = tk.Label(text="User: ")
		uw.userlabel.place(x=1000, y=100, width=200, height=25)
		uw.userlabel2 = tk.Label(text=str(user), relief=SUNKEN)#, width=20)
		uw.userlabel2.place(x=1200, y=100, width=200, height=25)
		
		uw.lvllabel = tk.Label(text="Level: ")
		uw.lvllabel.place(x=1000, y=150, width=200, height=25)
		uw.lvllabel2 = tk.Label(text=str(level), relief=SUNKEN)
		uw.lvllabel2.place(x=1200, y=150, width=200, height=25)	
		
		uw.cnumlabel = tk.Label(text="Number of Climbs: ")
		uw.cnumlabel.place(x=1000, y=200, width=200, height=25)
		uw.cnumlabel2 = tk.Label(text=str(cnum), relief=SUNKEN)
		uw.cnumlabel2.place(x=1200, y=200, width=200, height=25)		
	
		uw.highestxplabel = tk.Label(text="Highest XP: ")
		uw.highestxplabel.place(x=1000, y=250, width=200, height=25)
		uw.highestxplabel2 = tk.Label(text=str(highestxp), relief=SUNKEN)
		uw.highestxplabel2.place(x=1200, y=250, width=200, height=25)	
		
		uw.bouldergradelabel = tk.Label(text="Max Boulder Grade: ")
		uw.bouldergradelabel.place(x=1000, y=300, width=200, height=25)
		uw.bouldergradelabel2 = tk.Label(text=str(bouldergrade), relief=SUNKEN)
		uw.bouldergradelabel2.place(x=1200, y=300, width=200, height=25)			
		
		uw.climbgradelabel = tk.Label(text="Max Climb Grade: ")
		uw.climbgradelabel.place(x=1000, y=350, width=200, height=25)
		uw.climbgradelabel2 = tk.Label(text=str(climbgrade), relief=SUNKEN)
		uw.climbgradelabel2.place(x=1200, y=350, width=200, height=25)			
		
		uw.cgrouplabel = tk.Label(text="Climbing Group: ")
		uw.cgrouplabel.place(x=1000, y=400, width=200, height=25)
		uw.cgrouplabel = tk.Label(text=str(cgrp), relief=SUNKEN)
		uw.cgrouplabel.place(x=1200, y=400, width=200, height=25)			
		####exit button####
		uw.exitbutton = tk.Button(text="Exit")
		uw.exitbutton.place(x=650, y=800, width=200, height=25)
		uw.exitbutton.bind("<Button-1>", escape)
		####canvas for progressbar####
		uw.progresscanvas = tk.Canvas(bg="white", bd=2, highlightthickness=2, relief=RIDGE)
		uw.progresscanvas.place(x=300, y=700, width=900, height=50)
		#uw.progresscanvas.create_rectangel(0, 0, progress, 50
		
		uw.mainloop()#keeps user window
	
	def userlogin (self,click):
		value = self.uservar.get()
		if (value in dict.keys()):
			self.userwindow(value)
		elif (str(value) == "exit"):
			sys.exit()
		elif (value == "help"):
			print("Aint nuttin gunna help you")
			return ("help")
		elif (value == "create"):
			return ("create")
		else:
			print("--Invalid User ID (user ID is case sensitive)--")
			tk.messagebox.showerror("Invalid User ID", "  Please Enter a Valid User ID \n\n--User IDs are case sensitive--")
			self.logingui()

	
		
#root = tk.Tk()
gui = MainGUI()
gui.mainloop()

recompilewriter()
test.close()
path.close()

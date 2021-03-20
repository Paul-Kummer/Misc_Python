import sys
import itertools
import time
from tkinter import *
from tkinter import messagebox
#don't store any values that start with "V","B","5"

path = open("C:\\Users\\Tortrix\\Desktop\\ClimbingTime\\ctusers.txt", "r")
test = open("C:\\Users\\Tortrix\\Desktop\\ClimbingTime\\test.txt", "w")
dict = {}
recomp = {}

print(sys.version,"\n\n")

for line in path:
	if (line.strip().startswith("#")):
		continue
	else:	
		user, xpcur, xpmax, vmax, cmax, cgrp, notes, awards, chist = line.split(" : ")
		dict[user.strip()] = [xpcur.strip(), xpmax.strip(), vmax.strip(), cmax.strip(), cgrp.strip(), notes.strip(), awards.strip().split("."), chist.strip().split("!")]
print(dict)


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


def userlogin (value):
	if (value in dict.keys()):
		return(value)
	elif (str(value) == "exit"):
		sys.exit()
	elif (value == "help"):
		print("Aint nuttin gunna help you")
		return (value)
	elif (value == "create"):
		return (value)
	else:
		print("--Invalid User ID (user ID is case sensitive)--")
		return (False)
print("Enter (help)for help, (create)for new user, (exit) to exit program")
user = userlogin(input("Please Enter Your User ID and hit Enter: "))
while (user == False):
	user = userlogin(input("Please Enter Your User ID and hit Enter: "))

#Changes to these dictionary locations will be saved to ctusers.txt	
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

#definitions will need to point to the dict position to get up to date date. currently using old data
#class climbers (user):#connect the definitions to the class climbers
#	def __init__  (user, name)
#		user.name = user
	
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
		exp = ((int(xp) / 50) * 1.1)
		while((exp / 1.1) >= 1):
			exp /= 1.1
			lvl += 1
		return(int(lvl) + 9)
level = climberlevel(int(cumlativexp))			

#def xploser (lastclimb):
	
#def ranker (climber):
rank = "null" #ranker(xpcur)


print(dict[user])

#change these to make them actually help instead of crashing the program
if (user == "help"):
	print("helping")
elif(user == "create"):
	print("creating")
else:
	print("\n-------",user,"--------","\nCurrent XP: ",cumlativexp,"\nMax XP Earned: ",highestxp,"\nMax Boulder Difficulty: ",bouldergrade,"\nMax Climb Difficulty: ",climbgrade,"\nClimbing Group: ",cgrp,
	"\nNotes: ",notes,"\nAwards: ",awards,"\nClimbing History: ",chist,"\nNumber of Climbs Completed: ",cnum,"\nClimber Rank: ",rank,"\nClimber Level: ",level)



class maingui:
	def __init__(self, window):
		#****window building****
		self.window = window
		window.title("Climb Time")
		window.geometry("1200x800+350+200")#"500x500 is window size +700+200 is window position
		window.minsize(width=550, height=550)
		topframe = Frame(window)
		bottomframe = Frame(window)
		
		topframe.pack(side=TOP)
		bottomframe.pack(side=BOTTOM)
		
		#****buttons****
		self.exitbutton = Button(topframe, text="Exit", command=window.quit)
		self.userentry = Entry(topframe)
		self.userlabel = Label(topframe, text="user")
		self.userbutton = Button(topframe, text="user")
		
		self.userbutton.bind("<Button1>", userlogin(self.userentry.get()))
		
		self.userbutton.pack(side=RIGHT)
		self.exitbutton.pack(side=RIGHT)
		self.userentry.pack(side=RIGHT)
		self.userlabel.pack(side=RIGHT)
		
		#****menus****
		menu = Menu(window)
		window.config(menu=menu)
		
		subMenu = Menu(menu)
		menu.add_cascade(label="Options", menu=subMenu)
		subMenu.add_command(label="EXIT", command=window.quit)
		
		
		
		
		#****statusbar****
		status = Label(window, text="status is...", bd=1, relief=SUNKEN, anchor=W)
		status.pack(side=BOTTOM, fill=X)
		
		
		#****popup message****
		#messagebox.showinfo("This is prompting you", "select OK")
		answer = messagebox.askquestion("Inquiry from Admin", "Is it Climb Time?")
		if answer == "yes":
			print("lets go climb")
		else:
			print("No it is climb time")
			
		#****canvas****
		canvas = Canvas(window, width=500, height=500)
		canvas.pack(side=LEFT)
		
		
		#****images****
		wavebolt = PhotoImage(file=r"C:\\Users\Tortrix\\Desktop\ClimbingTime\Pictures\WaveBolt.png")
		canvas.image = wavebolt
		canvas.create_image(50,50, image=canvas.image, anchor=NW)		
		
	
	
	
	
	
	
	
	
	
	

window = Tk()
useme = maingui(window)
window.mainloop()
#if __name__ == "__main__":
#	main()
	
recompilewriter()
test.close()
path.close()		
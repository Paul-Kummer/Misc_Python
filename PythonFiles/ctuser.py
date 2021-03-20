
###Globals###
climbPointValues = {"5":"1","6":"2","7":"3","8":"4","9":"8","10":"10","11":"20","12":"30","13":"55","14":"90","15":"200"}
vBoulderPointValues = {"0":"1","1":"2","2":"4","3":"8","4":"10","5":"20","6":"30","7":"37","8":"55","9":"65","10":"70","11":"75","12":"80","13":"85","14":"90","15":"110"}
bBoulderPointValues = {"0":"1","1":"5","2":"10","3":"40","4":"80"}
awardValues = {"verticalMile":"100","smallTen":"100","mediumTen":"500","bigTen":"2000","godlyTen":"100000","smallChallenge":"20","mediumChallenge":"50","largeChallege":"100","extraLargeChallenge":"500","xxLargeChallenge":"1000","xxxLargeChallenge":"2000","insaneChallege":"5000","setterLevel1":"50","setterLevel2":"2000","setterLevel3":"5000","setterLevel4":"15000","climbingStaff":"50"}
deductionValues = {"smallDeduction":"10","mediumDeduction":"20","largeDeduction":"50","extraLargeDeduction":"100","majorDeduction":"1000","harnessOnImproper":"500","knotIncorrect":"500","dropClimber":"10000","belayIncorrect":"1000","CHEATER":"5000000"}
	###Award disambiguation###
	#name: points: discription
	
	#verticalMile: 100: complete 220 climbs
	#smallTen: 100: Ten  5.8 or 5.9 climbed with one minute or less rest between climbs, no falls
	#mediumTen: 500: Ten 5.10 or 5.11 climbed with one minute or less rest between climbs, no falls
	#bigTen: 2,000: Ten 5.12 or 5.13 climbed with one minute or less rest between climbs, no falls
	#godlyTen: 100,000: Ten 5.14 or higher climbed with five minute or less rest between climbs, no falls
	#smallChallenge: 20: Challege determined by the staff containing at least 3 routes or boulders not to exceed 5.8 level, no falls allowed
	#mediumChallenge: 50: Challege determined by the staff containing at least 3 routes or boulders between 5.8 and 5.9 level, no falls allowed
	#largeChallege: 100: Challege determined by the staff containing at least 3 routes or boulders between 5.9 and 5.11 level, no falls allowed
	#extraLargeChallenge: 500: Challege determined by the staff containing at least 3 routes or boulders between 5.11 and 5.12 level, no falls allowed
	#xxLargeChallenge: 1,000: Challege determined by the staff containing at least 4 routes or boulders between 5.11 and 5.12 level, no falls allowed
	#xxxLargeChallenge: 2,000: Challege determined by the staff containing at least 4 routes or boulders between 5.12 and 5.12 level, no falls allowed
	#insaneChallege: 5,000: Challege determined by the staff containing at least 5 routes or boulders not to be below 5.12 level, no falls allowed
	#setterLevel1: 50: Has taken a formal/informal setting class/clinic
	#setterLevel2: 2000: Is a certified level 2 route setter
	#setterLevel3: 5000: Is a certified level 3 route setter
	#setterLevel4: 15000: Is a certified level 4 route setter
	#climbingStaff: 50: Has worked at a climbing wall or still is working at a climbing wall


class CTUser():
	def __init__(self, user, group, deductions, awards, awardCount, climbCount, boulderCount, climbHistory):
		#string
		self.__user = user
		
		#string
		self.__group = group

		#2d list [["deduction", "mm:dd:yy", "witness", "location"],["deduction2", "mm:dd:yy", "witness", "location"]]
		self.__deductions = deductions
		
		#2d list [["award", "mm:dd:yy", "witness", "location"],["award2", "mm:dd:yy", "witness", "location"]]
		self.__awards = awards
		
		#string/integer
		self.__awardCount = awardCount
		
		#string/integer
		self.__climbCount = climbCount
		
		#string/integer
		self.__boulderCount = boulderCount
		
		#2d list [["climbGrade", "mm:dd:yy", "location],["climbGrade2", "mm:dd:yy", "location]]
		self.__climbHistory = climbHistory
	
	
	def __str__ (self):
		return("User: {1}\nMax Boulder Grade: {2}\nCompleted Boulders: {3}\nMax Climb Grade: {4}\nCompleted Climbs: {5}\nTotal Completed Climbs: {6}\nClimber Experience: {7}\nClimbing Group: {8}\nClimbging Awards: {9}"\
			.format(self.getUser(), self.getMaxBoulder(), self.getTotalBoulders(), self.getMaxClimb(), self.getTotalClimbs(), self.getBothClimbTotals(), self.getTotalXP(), self.getClimbingGroup(), self.getAwards())) #self.getClimbingHistory
		

###Accessors/Getters##
	def getUser(self):
		return(self.__user)
		
	def getMaxBoulder(self):
		bList = []
		vList = []
		for item in self.__climbHistory:
			climb = item[0]
			time = item[1]
			location = item[2]
			if climb[0] == "B":
				bList.append(int(item[1:]))
			elif climb[0] == "V":
				if climb[1] == "b":
					vList.append(0)
					continue
				vList.append(int(climb[1:]))
			else:
				continue
		if len(vList) == 0:
			vList = [0]
		if len(bList) == 0:
			bList = [0]
		vMax = max(vList)
		bMax = max(bList)		
		if (vMax + bMax) == 0:
			return("None")
		elif (float(bMax) * 2) > (float(vMax)):#magic number "2" estimates the grade conversion between the "b" scale and "v" scale
			return("B" + str(bMax))
		else:
			return("V" + str(vMax))
		

	def getTotalBoulders(self):
		boulderAccumulator = 0
		for item in self.__climbHistory:
			climb = item[0]
			time = item[1]
			location = item[2]
			if climb[0] == "B" or climb[0] == "V":
				boulderAccumulator += 1
		return(int(boulderAccumulator))
		
	def getMaxClimb(self):
		subgrades = ["a", "b", "c", "d"]
		climbList = []
		for item in self.__climbHistory:
			climb = item[0]
			time = item[1]
			location = item[2]
			#checks for subgrades, and gives them a slightly higher value than the other climbs
			if climb[0] == "5" and climb[-1] in subgrades:
				subgrade = climb[-1]
				difficulty = climb[2:-1]
				if subgrade == "a":
					difficulty = float(difficulty)+.1
					climbList.append(difficulty)
				elif subgrade == "b":
					difficulty = float(difficulty)+.2
					climbList.append(difficulty)
				elif subgrade == "c":
					difficulty = float(difficulty)+.3
					climbList.append(difficulty)
				elif subgrade == "d":
					difficulty = float(difficulty)+.4
					climbList.append(difficulty)
				else:
					pass
			elif climb[0] == "5" and climb[-1] not in subgrades:
				difficulty = climb[2:]
			else:
				pass
		return(max(climbList))
		
	def getTotalClimbs(self):
		climbAccumulator = 0
		for item in self.__climbHistory:
			climb = item[0]
			time = item[1]
			location = item[2]
			if climb[0] == "5":
				climbAccumulator += 1
		return(int(climbAccumulator))
		
	def getBothClimbTotals(self):
		boulderCount = self.getTotalBoulders()
		totalClimbCount = self.getTotalClimbs()
		return(int(boulderCount)+int(totalClimbCount))
		
	def getTotalXP(self):
		xp = 0
		subgrades = ["a", "b", "c", "d"]
		for item in self.__climbHistory:
			climb = item[0]
			time = item[1]
			location = item[2]
			boulderDifficulty = climb[1:]
			if climb[0] == "V":
				if boulderDifficulty == "b":
					xp += 1
				elif int(boulderDifficulty) > 15:
					xp += 110
				else:
					xp += int(vBoulderPointValues[boulderDifficulty])
			elif climb[0] == "B":
				if int(boulderDifficulty) > 4:
					xp += 80
				else:
					xp += int(bBoulderPointValues[boulderDifficulty])
			elif climb[0] == "5":
				subgrade = item[-1]
				if subgrade in subgrades:
					difficulty = climb[2:-1]
					if int(difficulty) < 5:
						xp += 1
					elif int(difficulty) > 15:
						xp += 200
					else:
						xp += int(climbPointValues[difficulty])
				else:
					difficulty = climb[2:]
					if int(difficulty) < 5:
						xp += 1
					elif int(difficulty) > 15:
						xp += 200
					else:
						xp += int(climbPointValues[difficulty])
			else:
				continue
		for item in self.__awards:
		#[award, date, witness, location]
			userAward = item[0]
			userAwardDate = item[1]
			userAwardWitness = item[2]
			userAwardLocation = item[3]
			if userAward in awardValues:
				xp += int(awardValues[int(userAward)])
		for item in self.__deductions:
			userDeduction = item[0]
			userDeductionDate = item[1]
			userDeductionWitness = item[2]
			userDeductionLocation = item[3]
			if userDeduction in deductionValues:
				xp -= int(deductionValues[int(userDeduction)])
		return(xp)
		
	def getMaxXP(self):
		pass
	
	def getGroup(self):
		return(self.__group)
		
	def getDeductions(self):
		return(self.__deductions)
		
	def getAwards(self):
		return(self.__awards)
		
	def getClimbingHistory(self):
		return(self.__climbHistory)
		
	def getClimberLevel(self):
		usersCurrentXP = int(self.getTotalXP)
		if (usersCurrentXP) <= 50:
			climberLevel = int(usersCurrentXP / 5)
			return(climberLevel)
		else:
			climberLevel = 9
			experience = ((usersCurrentXP / 50) * 1.1) #might need to subtract 50xp from xp before division
			while((experience / 1.1) >= 1):
				experience /= 1.1
				climberLevel += 1
			return(int(climberLevel))
		
		
###Mutators/Setters###
	def setUser(self):
		self.__user = user
		
	def setDeductions(self):
		self.__deductions = deductions
		
	def setGroup(self):
		self.__group = group
		
	def setClimbCount(self):
		self.__climbCount = climbCount
		
	def setBoulderCount(self):	
		self.__boulderCount = boulderCount
		
	def setAwardCount(self):
		self.__awardCount = awardCount	
		
	def setAwards (self):
		self.__awards = awards
		
	def setClimbingHistory(self):
		self.__climbHistory = climbHistory

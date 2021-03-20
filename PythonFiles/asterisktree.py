#Ch4Ex13
#Paul Kummer
#This program will display a triangle composed of asterisks starting at a size of 7 asterisks-
#and reducing in size each line to one asterisk.

#Sample asterisk tree to test against
#x = "*"
#for r in range (7, 0, -1):
#	print (x * r)

#Use the following code commented out to allow users to specify a size of asterisk tree
baseSize = int(input("how many asterisks would you like to go to? "))

#Specifies maximum number of asterisks the printed triangle will be, which is also the number of rows
#baseSize = 7

#Starts the triangle formation at the maximum base size value and reduces in size by one until reach-
#zero.	
for line in range (int(baseSize),0,-1):

	#Every time "row" changes value an asterisk is added to the whatever line the first loop is on. Using-
	#the "end" command after printing the asterisk prevents the loop from creating new lines.
	for row in range(int(line)):
		print ("*", end="")
		
	#Creates a new line to be populated by asterisks
	print()


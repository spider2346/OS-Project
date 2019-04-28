print
#list holds elements of all boolean values of TRUE/FALSE on whether the fruit is RED
fruitbool = []

#list holds elements of boolean values that return TRUE
redbool = []

#original list of elements
fruits = ['Red Apple', 'Red Pear', 'White Peach', 'Orange Mango', 'Red Grape', 'Red Grapefruit', 'Blood Orange' ]

#inserts a new element into the fruits list
fruits.insert(2, 'Green Apple')
print "Fruits:",fruits;

#sorts the fruits list in alphabetical order
fruits.sort()

#new list of sorted fruits
newFruits = list(fruits)

print
print "Sorted List:", newFruits	

#function to filter all "red" fruits from the sorted list
def filterFruits(newFruits):
	if 'Red' in newFruits:
		return True
	else:
		return False

#for loop that will loop through every index in the newFruits list and check to see if fruit is Red
for fruit in newFruits:
	red = filterFruits(fruit)
	fruitbool.append(red)

'''For loop that loops through fruitbool list and checks to see which values returned True and 
adds the True values to the redbool list based on their index position in the newFruits list.'''
for i in (i for i, x in enumerate(fruitbool) if x == True):
	redbool.append(newFruits[i])
print	
print "Red Fruits Only: ", redbool
print

#Asks the user for input on which index number he would like to remove from the redbool list
print "Index:\tFruits:"
for i in redbool:
	print (str(redbool.index(i)) + "\t" +i)
removeFruit = int(raw_input ("Which fruit would you like to remove? (Pick Index#): "))
del redbool[removeFruit]
print
print "Updated List:"

#prints an updated redbool list
for i in redbool:
	print (str(redbool.index(i)) + "\t" +i)




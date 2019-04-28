#Author: Sebastian Byczkowski
#List Management

print
fruits = [['Apple','Red',6],['Pear','Green',4],['Orange','Blood',3],['Grapefruit','Yellow',5]]
print "Fruits:", fruits
print
fruits += [['Pineapple','Yellow' ,5]]

newFruits = list(fruits)
newFruits.sort()

print "Sorted List:", newFruits
print
def filterFruits(alist):
    nFruitList= []
    for each in alist:
        if each[2] >= 4:
            nFruitList += [True]
        else:
            nFruitList += [False]
    return nFruitList

fruitBool = filterFruits(newFruits)

print "Boolean List:", fruitBool
print

newFruitList =[]
for i in range(len(fruitBool)):
    if fruitBool[i] == True:
        newFruitList += [newFruits[i]];

print "Weight - 4oz+:", newFruitList
print
print "[Index:]"
for i in newFruitList:
	print [newFruitList.index(i), i]
print
removeFruit = input('Which fruit would you like to remove? [Index#]: ')
if int(removeFruit) > (len(fruitBool)-1):
    print("Try again, that index does not exist.")
else:
    newFruitList.remove(newFruitList[int(removeFruit)])
print
print "Updated List:"
for i in newFruitList:
	print [newFruitList.index(i), i]
print
print




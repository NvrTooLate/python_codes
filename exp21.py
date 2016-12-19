the_count = [1,2,3,4,5]

fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for loop goes throught a list

for number in the_count:
	print "this is count: %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
for i in change:
	print "I have got %r" % i
	
#make an empty list
elements = []

for i in range(0,20):
	print "adding %d to the list: " % i
	#the append command is used to add stuff to a list 
	#elements refers to the list where you want to add stuff
	#the item inside the parantheses is the item you want to add
	elements.append(i)
	
for i in elements:
	print "element was : %d" % i 
#define the function
def cheese(count, boxes):
	print "Number of cheeses: %r" % count
	print "number of boxes: %r" % boxes
	
print "Enter number of Cheese types: "
count = raw_input("> ")

print "Enter number of boxes: "
boxes = raw_input("> ") 

cheese(count, boxes) #Call the fuction here

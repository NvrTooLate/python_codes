people  = raw_input("Enter number of people: ")
cats = raw_input("Enter number of cats: ")
dogs = raw_input("Enter number of dogs: ")

if people < cats:
	print "too many cats"
	
if people > cats:
	print "not many cats"
	
if people > dogs: 
	print "wet"
	
if people < dogs:
	print "dry"

if people >= dogs:
	print "people are greater than or equal to dogs"
	
if people <= dogs:
	print "people are less than or equal to dogs"	

if people == dogs:
	print "equality"
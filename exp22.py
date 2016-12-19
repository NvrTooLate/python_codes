def looper(x, number):
	i = 0
	numbers = []

	while i<number:
		print "at the top i is: %d " % i 
		numbers.append(i)
	
		i = i + x

		print "numbers now: ", numbers

		print "at the bottom i is: %d" % i 

	print "The numbers: "

	for n in numbers:
		print n
	

#this code can be used to create multiplication tables 
#for any number upto a certain limit
# number being "X" and the upper limit being "number"
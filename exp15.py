def add(a,b):
	print "adding %d and %d" %(a,b)
	return (a+b)
	
def subtract (a,b):
	print "subtracting %d from %d:" % (a,b)
	return (a-b)
	
def multiply (a,b):
	print "multiplying %d and %d" %(a,b)
	return (a*b)
	
def divide (a,b):
	print "Dividing %d and %d" %(a,b)
	return (a/b)
	
print "lets do some math with functions: "

a = add (30,20)
h = subtract (84,22)
w = multiply (22,4)  
i = divide (260,2)

print "Age: %d\n height: %d\n weight: %d\n iq = %d " %(a,h,w,i) 

puzzle = add(a, subtract(h, multiply(w, divide(i,2))))

print "Answer is %d: " %(puzzle)
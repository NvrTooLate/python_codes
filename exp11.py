def print2(*args):
	arg1,arg2 = args
	print "arg1: %r, arg2: %r" %(arg1,arg2)

def print2again(arg1,arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)	
	
def print1(arg1):
	print "arg1: %r" %arg1

def printzero():
	print"i got nothin"

print2("Ryan","Martins")
print2again("Martins", "Ryan")
print1("first comment!!!11!!11!")
printzero()

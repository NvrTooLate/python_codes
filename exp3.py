x = "there are %d types of people" % 10

binary = "binary"
do_not = "don't"

y = "those who know %s and those who %s" %(binary,do_not)

print x
print y

print "I said %s" % x
print "I also said %s" %y

hilarious = False
joke_eval = "Isn't that a funny joke %r" 

print joke_eval % hilarious

w = "this is the left side of..."
e = "a string with a right side"

print w+e
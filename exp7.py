from sys import argv

script,filename = argv

txt = open(filename)

print "Here is your file %r:" % filename

print txt.read()

print "type the filename again:"
again = raw_input("> ")

txt_again = open(again)

print txt_again.read()
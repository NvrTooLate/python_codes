from sys import argv

script, filename = argv

print "we're going to erase %r" % filename
print "if you do not want that, hit CTRL-C (^C) "
print "if you do want that, then hit RETURN/ENTER"

raw_input("?")

print "Opening file. . ."
target = open(filename,'w')

print "truncating file. . ."
target.truncate()

print "now i am going to ask you 3 lines:"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i am going to write these to the file"

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "finally we close the file. please access it by exiting"
print "thank you"

target.close()
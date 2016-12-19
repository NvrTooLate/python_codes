from sys import argv

script,filename = argv

print "press enter to edit the file"
print "press ctrl+c to exit the program"

raw_input ("> ")

print "the file contents are: "
target = open(filename)
print target.read()

print "the program is now going to edit the file"
print "Enter the 5 lines of contents to be written"

target = open(filename,'w')
target.truncate()

line1 = raw_input ("> ")
line2 = raw_input ("> ")
line3 = raw_input ("> ")
line4 = raw_input ("> ")
line5 = raw_input ("> ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")
target.write(line5)
target.write("\n")

print "The edited file is as follows: "
target = open(filename)
print target.read()

print "File is now being saved"
target.close()

from sys import argv
from os.path import exists

script,fromFile,toFile = argv

print "data is being copied from %s to %s" %(fromFile, toFile)

inFile = open(fromFile)
data = inFile.read()
print "the contents are: "
print data

print "the input file is %d bits long:" % len(data)

print "does the output file exist? %r" % exists (toFile) 
print "Press Enter to continue, or press ctrl+c to abort"
raw_input ("> ")

outFile = open(toFile, 'w')
outFile.write(data)

print "Copying is finished"

inFile.close()

outFile = open(toFile,'r')
print outFile.read() 
outFile.close()
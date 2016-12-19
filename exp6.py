from sys import argv

script, name = argv
prompt = "> "

print "Hello %s. I am the %s Script" %(name,script)
print "i'd like to ask you a few questions:"
print "Do you like me %s?"% name
like = raw_input(prompt)

print "Where do you live %s?" %name
live = raw_input(prompt)

print "What kind of computer do you use %s?" %name
pc = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, not too sure where that is.
And you have a %r computer. Not too shabby.
""" %(like,live,pc)
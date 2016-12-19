print "you enter a dark room with two doors.\n Do you take door 1, door 2, or door 3?"

for door in range(1,2,3):
	door = raw_input("> ")
	if door == "1":
		print "there is a giant bear here eating a cheese cake.\n What do you do?"
		print "1. Take the cake."
		print "2. Scream at the bear"
		print "3. Back away"
	
		bear = raw_input("> ")
	
		if bear == "1":
			print "the bear eats your face off. Sucker"
		elif bear == "2":
			print "the bear eats your legs off. Sucker"
		else:
			print "well, doing %s is probably better" %(bear)
		

	elif door == "2":
		print "you stare into the endlss abyss that is Cthulhu's eye.\n What do you do?"
		print "1. Blueberries"
		print "2. Yellow jacket clothespins"
		print "3. Understanding revolvers yelling melodies"
	
		insanity = raw_input("> ")
	
		if insanity == "1" or insanity == "2":
			print "Your body survives powered by a mind of jello. Sucker"
		else:
			print "The insanity rots your eyes into a pool of muck. Sucker"
		
	elif door == "3" :
		print "You stumble around, fall on a knife and die. What a loser."
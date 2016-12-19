for line in open("file.txt"):
	for word in line.split():
		if word.startswith('a') or word.endswith('g'):
			print(word)
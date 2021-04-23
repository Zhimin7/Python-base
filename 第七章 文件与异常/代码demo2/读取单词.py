infile = open('word.txt', 'r')
for line in infile:
	line = line.strip('.,\n')
	words = line.split()
	for word in words:
		print(word)
infile.close()
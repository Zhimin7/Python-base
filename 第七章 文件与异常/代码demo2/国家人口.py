infile = open('国家人口.txt', 'r')
line = infile.readline()
while line !='':
	countryName = line.rstrip()
	line = infile.readline()
	population = int(line)
	print('%s:%d' % (countryName, population))
	line = infile.readline()
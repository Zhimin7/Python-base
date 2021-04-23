inputfile = open('字符.txt', 'r')
char = inputfile.read(1)
while char != '':
	print(char, end = '')
	char = inputfile.read(1)
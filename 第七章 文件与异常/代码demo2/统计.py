letterCount = [0] * 26
inputfile = open('统计.txt', 'r')
char = inputfile.read(1)
while char != '':
	char = char.upper()
	if char >= 'A' and char <= 'Z':
		code = ord(char) - ord('A')
		letterCount[code] = letterCount[code] + 1
		char = inputfile.read(1)
print(letterCount)
inputfile.close()
##
# 该程序使用凯撒密码对文件进行加密

from sys import argv


DEFAULT_KEY = 3


def main():
	key = DEFAULT_KEY
	infile = ''
	outfile = ''

	files = 0
	for i in range(1, len(argv)):
		arg = argv[i]
		
		if arg[0] == '-':
			print(arg)
			option = arg[1]
		
			if option == 'd':
				key = -key
				
			else:
				usage()
				return
	
		else:
			files = files + 1
			if files == 1:
				infile = arg
			elif files == 2:
				outfile = arg
	if files != 2:
		usage()
		return
	inputfile = open(infile, 'r')
	outputfile = open(outfile, 'w')


	for line in inputfile:
		for char in line:
			newChar = encrypt(char, key)
			outputfile.write(newChar)

	inputfile.close()
	outputfile.close()






def encrypt(ch, key):
	LETTERS = 26 # 罗马字母表中字母的数量

	if ch >= 'A' and ch <= 'Z':
		base = ord('A')
	elif ch >= 'a' and ch <= 'z':
		base = ord('a')
	else:
		return ch

	offset = ord(ch) - base + key
	print(offset)
	if offset > LETTERS:
		offset = offset - LETTERS

	elif offset < 0:
		offset = offset + LETTERS
	return chr(base + offset)


def usage():
	print('Usage: python cipher.py -[d] infile outfile')


main()



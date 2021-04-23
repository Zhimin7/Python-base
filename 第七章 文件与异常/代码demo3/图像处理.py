def readInt(imgfile, offset):
	imgfile.seek(offset)
	theBytes = imgFile.read(4)
	result = 0
	base = 1
	for i in range(4):
		result = result + theBytes[i] * base
		base = base * 256

	return result

imgFile = open('img1.bmp', 'rb+')
fileSize = readInt(imgFile, 1)
start = readInt(imgFile, 10)
width = readInt(imgFile, 18)
height = readInt(imgFile, 22)
print(start, width, height)



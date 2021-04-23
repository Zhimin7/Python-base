##
# 该程序用来读取一个包含数字的文件，然后写入另一个文件
# 按列对齐，最后写入它们的总和和平均值
# 提示用户输入输出文件的名字

inputFileName = input('Input file name: ')
outputFileName = input('Output file name: ')


# 打开输入文件和输出文件
infile = open(inputFileName, 'r')
outfile = open(outputFileName, 'w')

# 读取输入文件，并写出输出文件
total = 0.0
count = 0

line = infile.readline()
while line != '':
	value = float(line)
	outfile.write('%15.2f\n' % value)
	total = total + value
	count = count + 1
	line = infile.readline()


outfile.write('%15s\n' % '-------------')
outfile.write('Total: %6.2f\n' % total)
print(count)
avg = total / count
outfile.write('Average: %6.2f\n' % avg)
infile.close()
outfile.close()
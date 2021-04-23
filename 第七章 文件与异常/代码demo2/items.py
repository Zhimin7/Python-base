##
# 该程序读取一个文件，其中的行包含项目和价格，就像：
# item name 1：price1
# item name 2：price2
# 每个项目的名字以冒号结束。
# 该程序写入一个文件，其中项目左对齐而价格右对齐
# 最后一行是价格总和

# 提示输入文件和输出文件的名字
inputFileName = input('Input file: ')
outputFileName = input('Output file: ')

# 打开输入文件和输出文件
inputFile = open(inputFileName, 'r', encoding='utf-8')
outputFile = open(outputFileName, 'w', encoding='utf-8')

# 读取输入并写入输出
total = 0.0

for line in inputFile:
	# 在冒号处切分记录
	print(line)
	parts = line.split('：')

	# 提取两个数据段
	item = parts[0]
	price = float(parts[1])

	# 增加total
	total += price

	# 写入输出
	outputFile.write('%-20s%10.2f\n' % (item, price))

# 写入价格总和
outputFile.write('%-20s%10.2f\n' % ('Total:', total))


# 关闭文件
inputFile.close()
outputFile.close()

# 成功提醒
print('处理完毕')


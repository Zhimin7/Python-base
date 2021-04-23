import time


def coding():
	for x in range(3):
		print('%s正在写代码' % x)
		time.sleep(1)


def drawing():
	for x in range(3):
		print('%s正在画图' % x)
		time.sleep(1)


def single_thread():
	coding()
	drawing()


if __name__ == '__main__':
	start = time.time()
	single_thread()
	end = time.time()
	print(end - start)
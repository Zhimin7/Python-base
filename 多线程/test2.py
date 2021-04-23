import threading
import time


def coding():
	for x in range(3):
		print('%s 正在写代码' % x)
		time.sleep(1)


def drawing():
	for x in range(3):
		print('%s 正在画图' % x)
		time.sleep(1)


def single_thread():
	coding()
	drawing()


def multi_thread():
	t1 = threading.Thread(target=coding)
	t2 = threading.Thread(target=drawing)

	t1.start()
	t2.start()



if __name__ == '__main__':
	start = time.time()
	multi_thread()
	end = time.time()
	print(end - start)
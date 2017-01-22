import time, threading

def loop():
	print("thread %s is running..." % threading.current_thread().name)
	n = 0
	while n < 5:
		n += 1
		print("Thread %s >>> %d" % (threading.current_thread().name, n))
		# time.sleep(1)
	print("Thread %s ended." % threading.current_thread().name)

print("Thread %s is running..." % threading.current_thread().name)
t1 = threading.Thread(target = loop, name='LoopThread1')
t2 = threading.Thread(target = loop, name='LoopThread2')
t1.start()
t2.start()
t1.join()
t2.join()
print("Thread %s ended." % threading.current_thread().name)
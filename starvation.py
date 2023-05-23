#task that executes a loop  and each iteration in the loop is a critical section that contains block call - mutex lock
from time import sleep
from threading import Thread
from threading import Lock

#task
def task(lock, identifier):
#acquire
	#with lock:
#execute the lock
	for i in range(5):
		lock.acquire()
		print(f"thread {identifier} working")
		sleep(1)
		lock.release()

lock = Lock()
threads = [Thread(target = task, args =(lock, i)) for i in range(2)]

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

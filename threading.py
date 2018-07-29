import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)
def threader():
    while True:
        worker = q.get()
	exampleJob(worker)
	q.task_done()

	q = Queue()
#Defining the threads/workers
for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
#dies when main thread dies
    t.start()

start = time.time() 
#starting time
for worker in ranger (20):
#instances for the threads is 20
    q.put(worker)

q.join()

print('Jobs took:', time.time()-start)
#how long time-start time


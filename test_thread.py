#!/usr/bin/python
import threading
import time
import Queue

exit = False
lock = threading.Lock()

class Test(threading.Thread):
    def __init__(self, thread_id, thread_name, queue):
	super(Test, self).__init__()
	self.thread_id = thread_id
	self.thread_name = thread_name
	self.queue = queue

    def run(self):
	print "start ", self.thread_name
	process(self.thread_name, self.queue)
	print "exit ", self.thread_name

def process(thread_name, queue):
    while not exit:
	lock.acquire()
	print "%s get the lock" % (thread_name)
	if not queue.empty():
	    number = queue.get()
	    lock.release()
	    print "%s release the lock" % (thread_name)
	    print "%s process %s" % (thread_name, number)
	else:
	    lock.release()
	    print "%s release the lock" % (thread_name)
	time.sleep(1)

thread_names = ["thread1", "thread2", "thread3"]
numbers = [1, 2, 3, 4, 5, 6]
queue = Queue.Queue(10)

threads = []
thread_id = 1

for thread_name in thread_names:
    thread = Test(thread_id, thread_name, queue)
    thread.start()
    threads.append(thread)
    thread_id += 1

lock.acquire()
print "master get the lock"
for number in numbers:
    queue.put(number)
lock.release()
print "master release the lock"

while not queue.empty():
    pass

exit = True

for thread in threads:
    thread.join()

print "exit master thread"

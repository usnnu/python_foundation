# _*_ coding:UTF-8 _*_


'''
concurrent execution

'''


#17.1 threading




import threading
import multiprocessing
import time

'''
# passing a callable object to the constructor 


def action(arg):
    time.sleep(1)
    print('the arg is:%s\n'%arg)

for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    t.start()

print('the main thread end!')


'''
'''
# override run()

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print('the arg is:%s\n'%self.arg)

for i in range(4):
    t = MyThread(i)
    t.start()

print('the main thread end!')





# set daemon = True

def action(arg):
    time.sleep(2)
    print('the arg is:%s\n'%arg)
    time.sleep(2)

for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    t.setDaemon(True)
    t.start()


print('the main thread end!')
print(t.is_alive())





class mythread(threading.Thread):
    def __init__(self, num, threadname):
        threading.Thread.__init__(self, name=threadname)
        self.num = num

    #重写run()方法
    def run(self):
        time.sleep(self.num)
        print(self.num)

#创建自定义线程类对象，daemon默认为False
t1 = mythread(1, 't1')
t2 = mythread(5, 't2')
#设置线程对象t2的daemon属性为True
t2.daemon = True
print(t1.daemon)
print(t2.daemon)
#启动线程
t1.start()
t2.start()

'''


'''
# join

def action(arg):
    time.sleep(5)
    print('the arg is:%s\n'%arg)
    time.sleep(2)

thread_list = []
for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    print(t)
    #t.setDaemon(True)
    thread_list.append(t)

print(thread_list)

for t in thread_list:
    t.start()

for t in thread_list:
    pass
    t.join()


print('the main thread end!')
print(t.is_alive())
'''



#  lock
'''
# no lock

gl_num = 0

def show(arg):
    global gl_num
    time.sleep(3)
    gl_num +=1
    print(str(gl_num)+'\n')

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread end!')


# use lock

gl_num = 0
lock = threading.RLock()

def show(arg):
    lock.acquire()
    global gl_num
    time.sleep(1)
    gl_num +=1
    print(gl_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread end!')





#  lock 

lock = threading.Lock()
a = lock.acquire()
print(a)
a =lock.acquire(timeout=5)
print(a)
a = lock.release()
print(a)
a = lock.acquire()
print(a)
a = lock.release()
print(a)




# RLock

rlock = threading.RLock()
a = rlock.acquire()
print(a)

a = rlock.acquire()
print(a)

a = rlock.release()
print(a)

a = rlock.release()
print(a)
'''



# condition 

'''
#condition 1
# producer and comsumer


product = None
con = threading.Condition()


# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print('produce...')
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print('consume...')
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()


'''

'''
# codition 2

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print("Producer(%s):deliver one, now products:%s" %(self.name, products))
                    condition.notify()#不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products))
                    condition.wait();#自动释放锁定
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("Consumer(%s):consume one, now products:%s" %(self.name, products))
                    condition.notify()
                    condition.release()
                else:
                    print("Consumer(%s):only 1, stop consume, products:%s" %(self.name, products))
                    condition.wait();
                time.sleep(2)

if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 3):
        c = Consumer()
        c.start()


'''

'''


# codition 3

alist = None
condition = threading.Condition()
 
def doSet():
    if condition.acquire():
        print(threading.current_thread())
        while alist is  None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()
 
def doPrint():
    if condition.acquire():
        print(threading.current_thread())
        while alist is None:
            condition.wait()
        for i in alist:
            print(i)
        condition.release()

 
def doCreate():
    global alist
    if condition.acquire():
        print(threading.current_thread())
        if alist is None:
            alist = [i for i in range(10)]
            condition.notify_all()
        condition.release()
 
tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()
    
'''







############## multiprocessing #######################

import multiprocessing
import time

def f(name):
    print(name)
    b = 30
    while b > 0:
        time.sleep(3)
        print('b = ',b)
        b -= 1

'''
if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('eerg',), name='bbb')
    p.start()
    p.join()
'''




'''
# 基础使用

from multiprocessing import Process

def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    #p.join()
    




from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()


'''





'''

# set_start_mehtod()

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

'''





'''
# Queue

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
'''



'''
# Pipe()
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

'''
'''
# lock

from multiprocessing import Process, Lock
from time import sleep

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
        sleep(2)

        print('555666')
        
    finally:
        l.release()
        pass

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

'''



'''
# shared memory


from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])



'''

'''
# manage server process

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()
        

        print(d)
        print(l)

'''


'''
# pool

from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")

'''

'''
# process method

import multiprocessing, time,signal

p = multiprocessing.Process(target=time.sleep, args=(1000,))
print(p, p.is_alive())
p.start()
print(p, p.is_alive())

p.terminate()
time.sleep(0.1)
print(p, p.is_alive())

print(p.exitcode == -signal.SIGTERM)

'''









'''

from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:         # start 4 worker processes
        result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))                     # prints "0"
        print(next(it))                     # prints "1"
        print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))        # raises multiprocessing.TimeoutError


'''

'''
from multiprocessing import Pool
import time

def func(args):
    time.sleep(1)   #程序休眠1s
    print("%s------>%s"%(args,time.ctime()))    #打印参数及时间

if __name__=="__main__":
    p1=Pool(2)  #设定开启2个进程池
    for i in range(10):
        p1.apply_async(func=func,args=(i,)) #设定异步执行任务

    p1.close()  #关闭进程池
    #time.sleep(2)   #程序休眠2s
    #p1.terminate()  #关闭进程池
    p1.join()   #阻塞进程池
    print("ending")     #打印结束语句





# multiprocess logging
import multiprocessing, logging
logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)
logger.warning('doomed')

'''




'''

# 17.7 queue.Queue
import queue
import threading

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

num_worker_threads = 5

q = queue.Queue()
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()

'''




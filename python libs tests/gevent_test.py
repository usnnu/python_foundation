#coding:utf-8


# coroutine


'''
# coroutine:yield

def consumer(name):
    print(name)
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer:%s %s ' %(n,name))
        r = '200 OK'


def produce(c,d):
    c.send(None)
    d.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('producer:%s' %n)
        r = c.send(n)
        d.send(n)
        print('producer: consumer return %s' %r)
    c.close()
    d.close()

c = consumer('B')
d = consumer('A')
produce(c,d)

'''


'''
# coroutine:greenlet
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
'''








'''
# gevent
from gevent import monkey; monkey.patch_socket()

import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0)


g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()
'''

#coding:utf-8


# coroutine

"""
greenlet
----------------------------------------
greenlet 
----------------------------------------

----------------------------------------

"""

from greenlet import greenlet

'''
print(dir(greenlet))

def test1():
    print(12)
    print(greenlet.getcurrent())
    gr2.switch()
    print(13)
    

def test2():
    print(22)
    print(greenlet.getcurrent())
    gr1.switch()
    print(23)


gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2,run=)
gr2.switch()
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

def callback_t(event, args):
    print('{} from {} to {}'.format(event, id(args[0]), id(args[1])))
    


def test1(x, y):
    z = gr2.switch(x+y)
    print(z)

def test2(u):
    print(u)
    gr1.switch('wefweeger')

main = greenlet.getcurrent()
gr1 = greenlet(test1)
gr2 = greenlet(test2)
print('main is {}, gr1 is {}, gr2 is {}.'.format(id(main), id(gr1), id(gr2)))
oldtrace = greenlet.settrace(callback_t)
gr1.switch("hell", " world")





# _*_ coding:UTF-8 _*_

##python 100例







#4#####################################################


'''
 python document/tutorial/4-controlflow
 

'''

'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('do you really want to quit?')
#ask_ok('sdfwe')




# arbitrary argument lists

def concat(*args, sep='/'):
    return sep.join(args)

c = concat('fwewfe', 'fwegre', 'ergrt34')
print(c)

c = concat('fwewfe', 'fwegre', 'ergrt34', sep='999999')
print(c)

# unpacking argument lists

c = list(range(3, 6))
print(c)
'''

'''

# lambda expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

'''
'''
# default argument

def f1(a,b=7):
    print(a,b)



def f2(a,b=7,*,c,d):
    print(a,b,c,d)


def f3(a,b,c=7,d=8,*args,e,f,**kwargs):
    print("a,b:",a,b)
    print('c,d:',c,d)
    print('e,f:',e,f)
    print('args:',args)
    print('kwargs:',kwargs)


#f3(3,4,5,6)
#f3(3,4,5,6,78,43,34,56,e=9,f=0,u=75)
f3(3,4,5,6,e=7,f=8)
#f3(3,4,c=5,d=6)

f3(3,4,5,6,7,8,9,6,5,e=45,f=32,u=56,k=32)

'''

#############################################################






'''
 python document/tutorial/5-data structure
 

'''



'''

# lists operation

lis = [x for x in range(13)]
pr = lis
print(pr)

pr.append(34)
pr.extend([x for x in range(34, 45)])
pr.insert(7, 90)
pr.remove(4)
pr.pop(5)
#pr.clear()
print(pr.index(11))

print(pr)
'''
'''

from collections import deque

queue = deque(['e', 't', 'u'])
queue.append("te")
queue.popleft()

squares = list(map(lambda x:x**2, range(10)))
s
print()
print()
print()
print()
print()
print()

'''


#8######################################







'''
python document/tutorial/8.errors and exceptions

'''

'''

#1 syntax errors


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print("The int is",x)
    finally:
        print("program end!")



'''






#10##########################



'''
 python document/tutorial/10 brief tour of the standard library
 

'''


'''
#

class maping():
    __a = 1
    _a =  2
    a = 3


    
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

    def mapprint(self):
        print(__a)
'''



'''
# generator expression

a = (x for x in range(10))
'''



'''
#1 operating system interface
import os


def os_oper():
    pr = os.getcwd()
    os.chdir("e:/")
    pr = os.getcwd()
    os.system('mkdir a')

    return pr




print(os_oper())
'''









# r,u,b

a = r'www\nwerwer'
b = 'www\nwerwer'
print('a= """{0}"""'.format(a))

print('b= """{}"""'.format(b))






def first(func):
    print('%s() was post to first()'%func.__name__)
    def _first(*args,**kwargs):
        print('call the function %s() in _first().'%func.__name__)
        return func(*args, **kwargs)
    return _first

def second(func):
    print('%s() was post second()'%func.__name__)
    def _second(*args, **kwargs):
        print('call the function %s() in _second.'%func.__name__)
        return func(*args, **kwargs)
    return _second

@first
@second
def test():
    return 'hello'


test()










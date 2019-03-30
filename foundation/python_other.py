# _*_ coding:UTF-8 _*_

##python 100例







# decorator


'''
# 原理
def test(f):  
    print("before ...")
    f()  
    print("after ...")


@test  
def func():  

    print("func was called"      )



'''

'''
# 简单使用
def fun1(f):
    print('decorator')
    def inner(*args):
        print('inner')
        f(*args)
    return inner


@fun1
def exe(b):
    print('b=',b)


exe(4)
'''


'''
# 简单使用
def fun1(f):
    print('decorator')
    def inner(*args):
        print('inner')
        f(*args)
    return inner


@fun1
def exe(b):
    print('b=',b)


lisa= [1,2,3,4,5]

#exe(*lisa) error more position argument
exe(4) # it's ok
'''


'''
# 多参数

def loud(f):
    def new_func(*args, **kw):
        print('calling with', args, kw)
        rtn = f(*args, **kw)
        print('return value is', rtn)
        return rtn
    return new_func

loudlen = loud(len)
lisa = [10,20,30]
loudlen(lisa)

'''



'''

# 多重装饰1

def dec1(func):  
    print("1111")  
    def one():  
        print("2222")  
        func()  
        print("3333")  
    return one  

def dec2(func):  
    print("aaaa")  
    def two():  
        print("bbbb")  
        func()  
        print("cccc")  
    return two  

@dec1  
@dec2  
def test():  
    print("test test")  

#test()  

'''

'''
# 多重装饰2

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

'''

'''
# 装饰器带参数

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():" %(text, func.__name__))
            print(args,kw)
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def now(*args,**kwargs):
    print("time.ctime()")




now(1,2,3)

'''




    
'''
反射

'''

'''

class foo(object):

    def __init__(self):
        self.name = 'abc'

    def func(self):
        return 'ok'



obj = foo()
ret = getattr(obj, 'func')
r = ret()
print(r)
'''

'''


if __name__ == "__main__":
    a = 7


    obj = __import__('python_var')
    b = getattr(obj, 'fun2')

'''











'''
python/变量
 

'''



#变量作用域

'''
g_count = 0

def outer():
    o_count = 1
    def inner():
        i_count = 2


print(o_count)
'''

'''
# 全局变量和局部变量

total = 10

print(total, id(total))
def sum(arg1, arg2):
    total = arg1 + arg2
    print(total, id(total))
    return total

c = sum(34, 12)
print(c, total, id(total))




total = 10
print(total, id(total))
def sum():
    
    total = 9
    print(total, id(total))



sum()
print(total, id(total))

'''

'''
# global  

num = 1

def fun1():
    global num
    print(num, id(num))
    num = 123
    print(num, id(num))

fun1()
print(num, id(num))
'''


'''
# nonlocal

def outer():
    num = 10
    print(num, id(num))
    def inner():
        nonlocal num
        num = 100
        print(num, id(num))
    inner()
    print(num, id(num))

outer()


# nonlocal

def outer():
    num = 10
    print(num, id(num))
    def inner():
        #nonlocal num
        num = 100
        print(num, id(num))
        def inner2():
            nonlocal num
            print(num, id(num))
            num = 300
        inner2()
    inner()
    print(num, id(num))

outer()
    




# error example

a = 10
def test():
    a = a + 1
    print(a)
test()
'''
'''
a = 10

def fun1():
    print(a)
    a = 15

fun1()

'''

#######################
# yield

'''
# example:1
def fab(max):
    n,a,b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

#f = fab(7)
f = yield from fab(7)
print(f)
for i in f:
    print(i)

'''

# example:2
'''
def node._get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild


'''

# example:3


'''
def fab(max):
    n,a,b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1


def func_yield():
    x = yield 8
    print(x)
    x = yield x+6
    print(x)
    x = yield 23
    print(x)
    return 14
    
a = func_yield()

print('step 1:')
print(a.send(None))
print('step 2:')
print(a.send(11))
print('step 3:')
print(a.send(12))
print(a.send(13))


def func():
    yield 8
    yield 9
    yield 10
    return 11
'''


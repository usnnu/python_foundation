# _*_ coding:UTF-8 _*_

##python 100例




'''
 python document/standard library/built-in functions
 
 

'''



'''

def f(x):
    return x**2

lista = [x for x in range(18)]
listb = list(map(f, lista))

print(listb)
'''





'''
abs() absolute value

all() return True if all elements of the iterable are true

any()

map() return an iterator that applies function to every item on iterrable.

reduce() #已取消，放入functools中


chr() return the string representing a character whose Unicode code
point is the intager i. 


print(chr(97))


'''


'''
# eval

x = 10
def func():
    y = 20   #局部变量y
    a = eval("x+y")
    print("a:",a)      #x没有就调用全局变量
    b = eval("x+y",{"x":1,"y":2})     #定义局部变量，优先调用
    print("b:",b)
    c = eval("x+y",{"x":1,"y":2},{"y":3,"z":4})  
    print("c:",c)  
    d = eval("print(x,y)")
    print("d:",d)   #对于变量d，因为print()函数不是一个计算表达式，因此没有返回值
func()

'''


'''
# exec()

x = 10
expr = """
z = 30
sum = x + y + z   #一大包代码
print(sum)
"""
def func():
    y = 20
    exec(expr)   #10+20+30
    exec(expr,{'x':1,'y':2}) #0+1+2
    exec(expr,{'x':1,'y':2},{'y':3,'z':4}) #30+1+3，x是定义全局变量1，y是局部变量

func()

'''


'''
# compile

s = """              #一大段代码
for x in range(10):
    print(x, end='')  
print()
"""
code_exec = compile(s, '<string>', 'exec')   #必须要指定mode，指定错了和不指定就会报错。
code_eval = compile('10 + 20', '<string>', 'eval')   #单个表达式
code_single = compile('name = input("Input Your Name: ")', '<string>', 'single')   #交互式

a = exec(code_exec)   #使用的exec，因此没有返回值
b = eval(code_eval)  

c = exec(code_single)  #交互
d = eval(code_single)

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('name: ', name)
print('d: ', d)
print('name; ', name)

'''

'''

# filter


"""filter(function, iterable)
Construct an iterator from those elements of iterable for which function returns true.
iterable may be either a sequence, a container which supports iteration,
or an iterator.
If function is None, the identity function is assumed, that is,
all elements of iterable that are false are removed.
Note that filter(function, iterable) is equivalent to the generator expression
(item for item in iterable if function(item))
if function is not None and (item for item in iterable if item) if function is None.
"""

def func(x):
    return x%2 ==1

def func1():
    pass

la = [x for x in range(30)]
lb = filter(func,la)

'''


# 进制
"""
bin()
hex()
oct()
int('34',8)
"""


#round

print(round(45.3434,2))


# slice()
import string
a = string.ascii_lowercase
b = slice(5)
b = slice(3, 7, None)
c = a[b]
print(c)


#vars





















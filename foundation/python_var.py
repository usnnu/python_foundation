# _*_ coding:UTF-8 _*_

##python 100例


a = 5

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


# 全局变量和局部变量






# 奇怪的测试
def fun1():
    num = 5
    
    def fun2():
        #global num
        #num = 6
        print('fun2',num)
        def fun3():
            num = 7
            print('fun3',num)
            def fun4():
                global num
                num = 9
                print('fun4',num)
            fun4()
        fun3()
    fun2()
        
    

fun1()
print(num)


def fun2():
    print(a)

'''
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
    
'''



# error example
'''
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


'''
print(5 or 0)

class a():
    def __init__(self):
        pass


    def __len__(self):
        return 0
    



d = a()



c = a()

if c != d:
    print(999)




c = 5
a = [c for x in range(40)]
#a[1:20] = 50
print(a)





st1 = "fwgerg wefergef er gdge ge"
b = st1.capitalize()


'''







    

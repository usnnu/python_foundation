# _*_ coding:UTF-8 _*_

'''
metaclass

'''



def fun(a,b,c):
    print('d')
    print('metaclass function')
    print(locals())
    attrs = ((name, value) for name, value in c.items() if not name.startwith('__'))
    print(attrs)
    print('www=\n',a,b,c,sep='\n')
    return type(a,b,c)






class f(object,metaclass=fun):
    def __init__(self,name):
        self.name = name



class f2():
    def __init__(self):
        pass

    def dl(self):
        pass

e = f('de')



class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args)
        return cls._instance

class A(object):
    def __init__(self,xing,gender):         #！#1
        self.namea="aaa"                    #！#2
        self.xing = xing                    #！#3
        self.gender = gender                #！#4
         
    def funca(self):
        print("function a : %s"%self.namea)
  
class B(A):
    def __init__(self,xing,age):            #！#5
        super(B,self).__init__(xing,age)    #！#6（age处应为gender）
        self.nameb="bbb"                    #！#7
        ##self.namea="ccc"                  #！#8
        ##self.xing = xing.upper()          #！#9
        self.age = age                      #！#10
         
    def funcb(self):
        print("function b : %s"%self.nameb)

b = B('lin', 23)



# _*_ coding:UTF-8 _*_

##python build in types


li = [x for x in range(4,30)]

def fun(b=1,*,a,d,e):
    print(type(a))
    print(a)
    #for i in a:
     #   print(i)

fun(1,a=2,d=3,e=4)

# _*_ coding:UTF-8 _*_

##python 100例

'''
#1 数组逆向输出
#

a=[99,66,25,10,3,4]

if __name__=='__main__':
    n=len(a)
    print(a)
    for i in range(int(len(a) / 2)):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        print(a)




#3 pingfangshu

import math

for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x == i+100) and(y*y==i+268):
        print(i,x,y)





#4
year=int(input("year:\n"))
month=int(input("month:\n"))
day=int(input("day:\n"))

months=(0,31,59,90,120,151,181,212,243,273,304,334)

if 0<month <= 12:
    sum = months[month-1]
else:
    print("data error.")

leap = 0

if(year%400 == 0) or ((year%4 == 0) and (year%100 == 0)):
    leap=1

if (leap==1) and (month > 2):
    sum+=1

print(sum)




#6
#fenbonaqishulie

def fib(n):
    a,b=1,1
    for i in range(10):
        a,b=b,a+b
    return(a)

def fib1(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[i-2]+fibs[i-1])
    return fibs


if __name__=='__main__':
    print(fib1(15))





#8九九乘法表

for x in range(1,10):
    print()
    for y in range(1,1+x):
        print("%d*%d=%d" %(x,y,x*y),end='\t')




#9
import time

myD = {1:'a',2:'b'}
for key,value in dict.items(myD):
    print("%s %s" %(key,value))
    time.sleep(1)




#10

import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(3)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))



#11

a1,b2=1,1
for i in range(1,21):
    print("%12ld %12ld" % (a1,b2),end=' ')
    if ((i % 3) == 0):
        print('')
    a1=a1+b2
    b2=a1+b2



#18

from functools import reduce
tn=0
sn=[]
n=5
a=4

for count in range(n):
    tn=tn+a
    a=a*10
    sn.append(tn)
    print(tn)

sn = reduce((lambda x,y:x+y),sn)
print(sn)


def fn(i,o):
    return i+o

d=[1,2,3]
dt=reduce(fn,d)


 #19

sn=100.0
hn=sn/2

for n in range(2,11):
    sn += 2*hn
    hn /=2

print('%f...%f' %(sn,hn))





def dayin():
    for i in range(8):
        for j in range(4-i+1):
            print(' ')
        for k in range(4+i+1):
            print('*')
        print()




def fa(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fa(j-1)
    return sum


for i in range(10):
    print('%d! = %d' %(i,fa(i)))





#26
#digui

def out(s,l):
    if l == 0:
        return
    print(s[l-1])
    out(s,l-1)





s = input('input a string:')
l = len(s)
out(s,l)





#27
#digui

def age(n):
    if n == 1:
        c = 10
    else:
        c=age(n-1)+2
    return c


print(age(5))





#32



a=12345

b=str(a)

print('%d,%s' %(a,b))


l=[1,2,3]
d='df'
c=d.join(l)

print(c)


a=['one','tow',32,'ieirg']
print(a)
for i in a[::-1]:
    print(i)



#33

l=[1,2,3,4,5]

sl=''.join(str(n) for n in l)
print(sl)

dt=''.join(l)





#35

class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "www.iplaypy.com 提示：此时文字颜色为浅黄色" + bcolors.ENDC)



#36
#区间素数输出

lower = int(input('input the lower:'))
upper = int(input('input the upper:'))

for num in range(lower,upper+1):
    if num >1 :
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)



#37

if __name__== "__main__":
    N=10
    print('please input ten num:\n')
    l=[]
    for i in range(N):
        l.append(int(input('input a number:')))
    print()
    print(l)

    #sort ten num

    for i in range(N-1):
        min = i
        for j in range(i+1,N):
            if l[min] > l[j]:
                min = j
        l[i],l[min]=l[min],l[i]
    print[l]



#38

if __name__== '__main__':
    a=[]
    sum=0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('input a num:')))
    for i in range(3):
        sum += a[i][i]
    print(sum)
    print(a)
    print(len(a))




#40

a=[1,2,4,354,56,34,56,7,9]

print(a)
N=len(a)
for i in range(len(a)//2):
    a[i],a[N-i-1] = a[N-i-1],a[i]

print(a)




#44
#矩阵相加

x=[[12,7,3],
   [4,5,6,],
   [7,8,9]]

y=[[5,8,1],
   [6,7,3],
   [4,5,9]]

result=[[0,0,0],[0,0,0],[0,0,0]]
result[2][2]=15
print(result[1],result[2])

for i in range(len(x)):
    for j in range(len(x[0])):
        #print('%d %d %d' %(result[i][j],x[i][j]),y[i][j]))
        result[i][j] = x[i][j] + y[i][j]
        print('%d %d %d' %(result[i][j],x[i][j],y[i][j]))
        print(i,j)
        print(result[i])

print(len(result))
for t in result:
    print(t)




#45

res=0

for i in range(1,50):
    res += i

print(res)




#46

while 1:
    num = int(input('input a number:'))
    if num*num<50:
        break
    else:
        continue



#49

x=10
y=20

t = lambda x,y:x
#if x>y  else y
print(t(x,y))


#50
import random


print(random.uniform(10,20))



#515253

a=0o76
b=a & 3
c=a| 4

print(a,b,bin(c))



#56

from Tkinter import *

canvas = Canvas(width=800,height=600,bg='yellow')
canvas.pack(expand=YES,fill=BOTH)
k=1
j=1
for i in range(0,26):
    canvas.create_oval(310 - k,250 - k,310 + k,250 + k,withd = 1)
    k+=j
    j+=0.3

mainloop()




#61
#杨辉三角形

a=[]
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a[i][0] = 1
    a[i][i] = 1

for i in range(2,10):
    for j in range(1,i):
        a[i][j] = a[i-1][j-1] + a[i-1][j+1]

from sys import stdout
for i in range(10):
    for j in range(i+1):
        print(a[i][j],end=' ')

        #stdout.write(str(a[i][j]))
        #stdout.write('')
    print()




#62
sStr1 = 'abcdefg'
sStr2 = 'cde'

print(sStr1.find(sStr2))






#63
#画椭圆

from tkinter import *

x = 360
y = 160

top = y - 30
bottom = y -30

canvas = Canvas(width = 400,height = 600,bg ='white')
for i in range(20):
    canvas.create_oval(250-top,250 - bottom,250 + top, 250 + bottom)
    top -=5
    bottom += 5
canvas.pack()
mainloop()



#66

if __name__ == '__main__':
    n1= int(input('n1 = :'))
    n2= int(input('n2 = :'))
    n3= int(input('n3 = :'))

    def swap(p1,p2):
        return p2,p1

    if n1 > n2: n1,n2 = swap(n1,n2)
    if n1 > n3: n1,n3 = swap(n1,n3)
    if n2 > n3: n2,n3 = swap(n2,n3)

    print(n1,n2,n3)




# 69
num = int(input('input the number:'))
ar = [i for i in range(1, num + 1)]
print(ar)

i = 0
m = 0
k = 0

while m < num - 1:
    # if i == num: i=0
    if ar[i] != 0: k += 1
    if k == 3:
        ar[i] = 0
        k = 0
        m += 1
    i += 1
    if i == num: i = 0

i = 0
while ar[i] == 0: i += 1
print(ar[i])



ptr = []
for i in range(5):
    num = int(input("please input a number:\n"))
    ptr.append(num)
print(ptr)
ptr.reverse()
print(ptr)



a=[6,1,2,3]
b = [4,5,6]

a.sort()
print(a)

a.extend(b)
print(a)



#76
def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n+1,2):
        s += 1.0/i
    return s

def podd(n):
    s = 0.0
    for i in range(1,n+1,2):
        s += 1.0/i
    return s

def dcall (fp,n):
    s = fp(n)
    return s

n = int(input("input a number:"))
if n%2 == 0:
    sum = dcall(peven,n)
else:
    sum = dcall(podd,n)

print(sum)



#80
i,j,x = 0,1,0

while (i<5):
    x = 4 * j
    for i in range(0,5):
        if (x%4 != 0):
            break
        else:
            i +=1
        x = (x/4)*5 + 1
    print(j,i)
    j+=1
print(x,j)


n,j,k=1,0,0

#function2
x=1
j,k,l=0,0,0

while True:
    j=4*x
    for i in range(0,6):
        if (j%4 != 0):
            break
        else:
            j = (j/4)*5 + 1
            #l +=1
    print(x,i)
    if i == 5:
        break
    x +=1
    
    
print(j,k,i,l,x)


#81
a = 809
for i in range(10,100):
    b = i * a
    if b>=1000 and b <=10000 and 8*i<100 and 9*i>=100:
        print(b,'=800*',i,'+9*',i)




#82

n = 0
p = input('input a number')
for i in range(len(p)):
    n = n*8 + ord(p[i])-ord('0')
print(n)




#88

n=1
while n<=7:
    a=int(input('input a number:'))
    while a<1 or a >50:
        a = int(input("input a number:"))
    print(a*'*')
    n+=1




#
tl = [10086,"中国移动",[1,2,3,4,5]]

print(len(tl))

print(tl.pop(1))
print(tl)


import time
start =time.time()
for i in range(3000):
    print(i)
end = time.time()

print(end - start)


y='aefsf'
x=1
print(x,y)

for i in range(10):
    x= (x+1)*2
    print(x)

print(x)
'''


import uuid

def get_id(num):
    list_id = []
    for i in range(num):
        id = str(uuid.uuid1()).replace('-','')
        list_id.append(id)
    return list_id

id = get_id(200)
with open('file_id.txt','w') as file:
    for i in id:
        file.write(i+'\n')




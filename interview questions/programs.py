# coding:utf-8

__author__ = "sn"



"""


"""


'''
1.交叉单链表求交点
方法1;常规方法
方法2：类似查找链表环，指针a追赶b至追上为止。

'''
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1
def jiaocha1(listnode1, listnode2):
    len1, len2 = 0, 0
    lt1 = listnode1
    while lt1.next:
        lt1 = lt.next
        len1 += 1
    lt2 = listnode2
    while lt2.next:
        lt2 = lt2.next
        len2 += 1
    if lt1 != lt2:
        return None

    lt1, lt2 = listnode1, listnode2

    if len1 > len2:
        for _ in range(len1-len2):
            lt1 = lt1.next
    else:
        for _ in range(len2-len1):
            lt2 = lt2.next

    while lt1 and lt2:
        if lt1.next == lt2.next:
            return lt1.next
        else:
            lt1 = lt1.next
            lt2 = lt2.next


# 方法2

def jiaocha2(listnode1, listnode2):
    lt1, lt2 = listnode1, listnode2
    while lt1 != lt2:
        lt1 = listnode2 if lt1 == None else lt1.next
        lt2 = listnode1 if lt2 == None else lt2.next
    return lt1
'''    

    
class Foo():
    name = 4
    c = []
    def __init__(self, age):
        self.age = age
        self.k = []


class Foo1():
    name = 4
    c = []
    def __init__(self, age):
        self.age = age
        self.k = []



a = Foo(6)
b = Foo(8)



c = []
d = []





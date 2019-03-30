#coding:utf-8

'''
说明：常用排序算法实现
'''







# sequence search

def sequence_search(lst, target):
    if len(lst) == 0:
        return None
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None



# 二分查找Binary Search

def binary_search(lst, target):
    if len(lst) == 0:
        return None
    
    l,r = 0, len(lst)-1
    while l <= r:
        mid = (r+l)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None
            
    
# 斐波那契查找

def fibnacci_search(lst, target):
    if target < lst[low] or target > lst[high]:
        return None
    
    # 需要一个斐波那契列表，其最大元素的值必须大于lst中元素的个数
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]

    low, high = 0, len(lst) - 1

    k = 0
    while high > F[k]-1:
        k += 1
    i = high
    while F[k]-1 >i:
        lis.append(lis[high])
        i += 1


    # 算法主逻辑
    while low <= high:
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1]-1

        if target < lis[mid]:
            high = mid - 1
            k -= 1
        elif target > lis[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                return mid
            else return high
    return None
                
        
        

    
# 二叉排序树

class BSTNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.lchild = left
        self.rchild = right



class BinarySortTree():
    """
    基于BSTNode类的二叉排序数。维护一个根节点的指针。
    """

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.lchild
            elif key > entry:
                bt = bt.rchild
            else:
                return entry
        return None

    def insert(self, key):
        """
        插入操作
        ：param key:目标值
        :return bool
        """

        bt = self._root
        if not bt:
            self._root = BSTNode(key)
            return
        while True:
            value = bt.value
            if key < value::
                if bt.lchild is None:
                    bt.lchild = BSTNode(key)
                    return
                bt  = bt.left
            elif key > value:
                if bt.rchild is None:
                    bt.rchild = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.value = key
                return

    def delete(self, key):
        """
        :param key: key word
        :return: bool
        """

        p, q = None, self._root
        if not q:
            print("empty tree!")
            return

        # find a node q which q.value == key, q's parent node p
        while q and q.value != key:
            p = q
            if key < q.value:
                q = q.lchild
            else:
                q = q.rchild
            if not q:
                return

        if not q.lchild:
            if p is None:
                self._root = q.rchild
            elif q is p.lchild:
                p.lchild = q.rchild
            else:
                p.rchild = q.rchild

        r = q.lchild
        while r.rchild:
            r = r.rchild
        r.rchild = q.rchild
        if p is None:
            self._root = q.lchild
        elif p.lchild is q:
            p.lchild = q.lchild
        else:
            p.rchild = q.lchild

        
        

    
    
                






#测试部分代码


from random import random
from json import dumps, loads

def dump_random_array(file='numbers.json', size= 10 ** 4):
    fo = open(file, 'w', 1024)
    numlst = list()
    for i in range(size):
        numlst.append(int(random()*10 ** 10))
    fo.write(dumps(numlst))
    fo.close()

def load_random_array(file='numbers.json'):
    fo = open(file, 'r', 1024)
    try:
        numlst = fo.read()
    finally:
        fo.close()
    return loads(numlst)


from datetime import datetime

def exectime(func):
    def iner(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(inter.seconds, inter.microseconds))
        return result
    return iner

if __name__ == "__main__":
    #dump_random_array()
    #exit(0)

    #array = load_random_array()
    array = [x for x in range(10000,0,-1)]
    #array = [x for x in range(20,0,-1)]

    x = exectime(counting_sort)
    lis = x(array,10000)
    
    '''
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            print('error')
    '''
    fo = open('sort_result.json', 'w', 1024)
    fo.write(dumps(lis))
    fo.close()


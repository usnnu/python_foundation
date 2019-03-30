#coding:utf-8

'''
说明：常用排序算法实现
'''



#插入排序
def insert_sort(lis):
    for i in range(1, len(lis)):
        for j in range(i):
            if lis[i] < lis[j]:
                lis.insert(j, lis.pop(i))
                break
    return lis




#希尔排序 效率较低
def shell_sort(lis):
    gap = len(lis)
    while gap >= 1:
        gap = gap // 2
        for i in range(gap, len(lis)):
            for j in range(i % gap, i, gap):
                if lis[i] < lis[j]:
                    lis[i], lis[j] = lis[j], lis[i]
    return lis


# 另一种希尔排序
def shell_sort(lis):
    n = len(lis)
    gap = n
    while gap >=1:
        gap = gap//2
        for i in range(gap,n):
            j = i
            while j >=gap and lis[j] < lis[j-gap]:
                lis[j], lis[j-gap] = lis[j-gap], lis[j]
                j -= gap
    return lis

# 换步长试一试
'''
def shell_sort(lis):
    #assert 0,print("www")
    n = len(lis)
    h = 1
    while h < n/3:
        h = h*3 + 1
    while h >=1:
        for i in range(h,n):
            j = i
            while j >= h and lis[j] < lis[j-h]:
                lis[j], lis[j-h] = lis[j-h], lis[j]
                j -= h
        h = h//3
    return lis
'''


#简单选择排序
def select_sort(lis):
    for i in range(len(lis)):
        x = i
        for j in range(i, len(lis)):
            if lis[i] < lis[j]:
                x = j
        lis[i], lis[x] = lis[x], lis[i]

    return lis






#堆排序
def sift_down(array, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break

        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1

        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


def heap_sort(array):
    #初始化大顶堆
    length = len(array)
    
    for i in range(length//2-1, -1, -1):
        sift_down(array, i, length-1)
        
    
    #已构造大顶堆，将堆顶array[0]与堆尾array[-1]互换，则array[-1]是有
    #序的，对array[:-1]继续构造大顶堆，互换首尾，重复得到结果
    for i in range(length-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i-1)

    return array
    
        








#bubble_sort
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array






# quick_sort

def quick_sort(array):
    def recursive(begin, end):
        if begin >= end:
            return
        left, right = begin, end
        key = array[left]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            while left < right and array[left] <= key:
                left += 1
            array[left], array[right] = array[right], array[left]
            
        array[left], array[begin] = key, array[left]
        recursive(begin, left -1)
        recursive(right + 1, end)

    recursive(0, len(array)-1)
    return array




# quick_sort 非递归


def quick_sort1(lis):
    def recursive(begin, end):
        if begin >= end:
            return begin
        left, right = begin, end
        key = array[left]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            while left < right and array[left] <= key:
                left += 1
            array[left], array[right] = array[right], array[left]
        array[left], array[begin] = key, array[left]
        return left

    
    if len(lis) < 2:
        return lis
    length = len(lis)
    stack = []
    stack.append([0,length-1])
    while stack:
        l, r = stack.pop()
        mid = recursive(l,r)
        if mid + 1 < r:
            stack.append([mid+1,r])
        if mid - 1 > l:
            stack.append([l, mid-1])
    return lis
        





# merge_sort

def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array_temp = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array_temp.append(arr_l.pop(0))
            else:
                array_temp.append(arr_r.pop(0))
        array_temp += arr_l
        array_temp += arr_r
        return array_temp

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(array)




# counting sort

'''
# 有问题-争议
def couting_sort(lis):
    length = len(lis)
    array_temp = [None]*length
    for i in range(length):
        p = q = 0
        for j in range(length):
            if lis[j] < lis[i]:
                p += 1
            elif lis[j] == lis[i]:
                q += 1
        for k in range(p, p+q):
            array_temp[k] = lis[i]
    return array_temp
'''

def counting_sort(lis, k):
    n = len(lis)
    result = [None]*n
    lis_c = [0]*(k+1)

    for i in lis:
        lis_c[i] += 1
    for i in range(1,k+1):
        lis_c[i] = lis_c[i] + lis_c[i-1]

    for i in range(n-1,-1,-1):
        result[lis_c[lis[i]]-1] = lis[i]
        lis_c[lis[i]] -= 1
    return result


# bucket sort

def bucket_sort(lis):
    num_min = min(lis)
    buckets = [0] *(max(lis) - min(lis) + 1)
    for i in range(len(lis)):
        buckets[lis[i]-num_min] += 1
    res = []
    for i,j in enumerate(buckets):
        if j != 0
            res.extend([i + num_min]*j)
    return res 

        
            


# radix_sort(array):

def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket =[[] for j in range(10)]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[1])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array























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


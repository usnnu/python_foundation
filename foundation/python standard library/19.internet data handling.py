# _*_ coding:UTF-8 _*_


# heapq code example



'''
# 8.5 heapq

import random
import heapq

la = [x for x in range(30)]
random.shuffle(la)

heap = []

for i in la:
    heapq.heappush(heap, i)

print(heapq.heapify(la))

    
'''


# 19.2 json

import json


'''
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
with open('a.txt', 'w', encoding='utf-8') as fi:
    js_dump = json.dump(data, fi)
print(js_dump)

js = json.dumps(data)

print(type(js))     #<class 'str'>


'''

#'''
a = [1,2,3,4,5,6,7,8,9]
b = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
c = 5
d = 'string.sfowjeiosdjfioerg'
e = ('23', 5, 'eder',67)
with open('a.txt', 'a', encoding='utf-8') as fi:
    js_dump = json.dump(a, fi)
    json.dump(b,fi)
    json.dump(c,fi)
    json.dump(d,fi)
    json.dump(e,fi)
    


#'''
with open('a.txt', 'r', encoding='utf-8') as fi:
    data = json.load(fi)
    
print(type(data))











    

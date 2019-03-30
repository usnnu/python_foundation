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



# 8.10 copy


import copy

la = [1, 2, 3, ['a', 'b', 'c']]
lb = la

print(id(lb) == id(la)) #True

la.append(5)
print(id(lb) == id(la)) #True

# copy
lb = copy.copy(la)
print(id(lb) == id(la)) #False
print(id(lb[3]) == id(la[3])) #True

# deep copy

#lb = copy.deepcopy(la)

print(id(lb) == id(la)) #False
print(id(lb[3]) == id(la[3])) #False








s = '%(name)s:start_urls'
nam = 'name'

a = s %{nam:'wedfger'}



print(a)











    

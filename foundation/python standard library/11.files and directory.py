# _*_ coding:UTF-8 _*_


# heapq code example



# 11 os operation
'''
import os


pr = os.getcwd()


print(pr)


# file object
#a = os.fdopen('a.txt')

#a.write('wgegege')
'''



# 11.2 os.path
import os
import os.path as pa

a = os.getcwd()

# 
# abspath(path) 输出规范化路径
print(pa.abspath(a))

# exists(path) exists the path

# isdir(),isfile(),islink(),

# split(path) 将路径分为路径+文件名的二元组返回。


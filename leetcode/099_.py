# coding:utf-8

__author__ = "sn"

"""


"""

"""


"""


a = '''# coding:utf-8

__author__ = "sn"

"""


"""

"""


"""
'''

for i in range(100, 200):
    with open(str(i)+"_.py", "w+")as fi:
        fi.write(a)
    

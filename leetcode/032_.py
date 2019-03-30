# coding:utf-8

__author__ = "sn"

"""


"""

"""


"""


import re
stra = "99999999999999123456789457690"

resulta = re.findall(r'(\w)(((?=\w\w\w)(\w))+)',stra)


print(resulta)



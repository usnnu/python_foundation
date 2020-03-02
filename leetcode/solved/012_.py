# coding:utf-8
__author__ = "sn"

"""


"""

"""
1.使用变量k替代循环条件判断中的len(list2)可减少3ms运行时间
2.方法2比方法1基本上快5ms
    方法2 中生成迭代器时使用dict.__iter__()比iter(dict)快2-3ms
    方法2 中使用列表然后生成字典时非常慢
3.方法3最快...
    
"""

import datetime
import time


class Solution:
    #方法1
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        list2 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = " "
        i = 0
        while num > 0 and i < len(list2):
            if num >= list2[i]:
                result = result + list1[i]
                num -= list2[i]
            else:
                i += 1
        return result

    #方法2
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        a = dic.__iter__()
        result = ""
        b = a.__next__()
        while num > 0 and b is not None:
            if num >= b:
                result = result + dic[b]
                num -= b
            else:
                b = a.__next__()
        return result

    #方法3 另一种解法

    def intToRoman(self, num):
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
    
    #方法3的变种
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (num // v) * numerals[i]
            num %= v
        return res


res = Solution()
starttime = time.time()
for i in range(1,4000):
    print(res.intToRoman(i))

endtime = time.time()
print(endtime-starttime)


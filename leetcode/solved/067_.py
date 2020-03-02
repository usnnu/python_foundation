# coding:utf-8

__author__ = "sn"

"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

"""

"""
思路：
1.按位相加，进位；
2.pythonic


"""


class Soution():
    def addBinary(self, a, b):
        carry, result = '', 0
        i, j = len(a) -1, len(b) -1
        while i>=0 or j >= 0 or carry:
            cur = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, rem = divmod(cur + carry, 2)
            result = 'rem' + result
            i -= 1
            j -= 1
        return result

    #其它写法
    # return bin(int(a, 2) + int(b, 2))[2:]

    

# coding:utf-8

__author__ = "sn"

"""
66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

"""
思路：

1.从尾到头遍历，如果为9则置0，下一位继续加1，如果非9则加1返回；
该设计主要是为了满足进位要求
如果数组为全9，数组头部加一个元素1返回

"""


#利用取反简化写法
class Solution():
    def plusOne(self, digits):
       for i in range(len(digits)):
           if digits[~i] < 9:
               digits[~i] += 1
               return digits
            digits[~i] = 0
        return [1] + [0]*len(digits)







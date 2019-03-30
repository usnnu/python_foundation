# coding:utf-8

__author__ = "sn"

"""
36.Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""

"""
思路：
1.常规循环
步骤一：得到最后一个非空格字符的下标，
步骤二：得到最后一个字条前一个空格字符的下标
步骤三：二者相减得到差值，返回

注意边界和特殊情况；

2.pythonic写法

"""



class Solution():
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while s[i] == ' ' and i >= 0:
            i -= 1
        end = i
        while s[i] != ' ' and i >=0:
            i -= 1
        return end - i




"""
error function:没考虑清特殊情况
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        else:
            return len(s.split(' ')[-1]) 

"""
     def lengthOfLastWord(self, s):
         str_split = s.split()

        if len(str_split) == 0:
            return 0
        else:
            return len(str_split[-1])



# coding:utf-8

__author__ = "sn"

"""
题目写得有点不清楚，理解为求列表中每个字符串的前多少位是相等的，返回相等部分；

"""

"""
思路：
使用zip将strs中的每个字符串按字符进行组合，然后判断组合内的字符是否相等（使用set()）


"""



class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

res = Solution()
str = ["abc", "ab", "abue"]
print(res.longestCommonPrefix(str))

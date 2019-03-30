# coding:utf-8
# 005
# Longest Substring Without Repeating Characters
__author__ = "sn"

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

找出最长的回文字符串并输出
"""

"""
思路：
对每个字符做上下文判断
"""


class Solution(object):
    def longestPalindrome(self, s):
        maxl = 0
        lens = len(s)
        start = [1, 1]
        for i in range(1, lens):
            if s[i] == s[i - 1]:
                n = 0
                while n < i and i + n < lens and s[i + n] == s[i - n - 1]:
                    n += 1
                if (n * 2) >= maxl:
                    maxl = n * 2
                    start = [i - n, i + n]

            if i + 1 < lens and s[i + 1] == s[i - 1]:
                n = 1
                while n <= i and i + n < lens and s[i - n] == s[i + n]:
                    n += 1
                    if (n * 2 - 1) >= maxl:
                        maxl = n*2-1
                        start = [i-n+1, i+n-1]
                        print(i)

        return start


# str = "acdcedacd"
# str = "laksdgabcdikidcbajoweio"
# str = "abbbb"
# str = "aaaabbb"
st = "abbbba"
exam = Solution()
star = exam.longestPalindrome(st)
print(star)
print(str[star[0]: star[1]])

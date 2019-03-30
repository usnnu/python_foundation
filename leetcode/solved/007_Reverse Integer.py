# coding:utf-8
# ZigZag Conversion
__author__ = "sn"
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
反转整数，大数返回0
"""

"""
思路：
未实现大数返回0

"""


class Solution(object):
    def reverse(self, x):
        x_str = str(x)
        if not x_str[0].isdigit():
            return int(x_str[0] + x_str[1:][::-1])
        else:
            return int(x_str[::-1])

    # 另一种方法
    def reverse(self, x):
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10
        return sign * answer


s = 1270
s = -12980
temp_class = Solution()
print(temp_class.reverse(s))

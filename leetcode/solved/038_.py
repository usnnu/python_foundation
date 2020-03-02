# coding:utf-8

__author__ = "sn"

"""

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"
 
Example 2:
Input: 4
Output: "1211"

Input Constraints:
1 <= n <= 30
"""

"""
思路：
1.最简单的思路，根据前一项推导后一项至满足要求，二层循环，第一层控制循环次数，
第二层生成字符串；
2.pythonic写法；

"""


def countAndSay(n):
    s = '1'
    for _ in range(n-1):
        let, temp, count = s[0], '', 0
        for item in s:
            if let == item:
                count +=1
            else:
                temp += str(count) + let
                let = item
                count = 1
        temp += str(count) + let
        s = temp
    return s



#pythonic
import re
def countAndSay(n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s


print(countAndSay(9))




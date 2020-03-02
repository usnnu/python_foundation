# coding:utf-8
# ZigZag Conversion
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
字符串Z型化
"""

"""
思路：
建立长度为numRows的list，逐个添加元素，到前后端反转方向
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        re = [""]*numRows
        j, k = 0, 1
        for i in s:
            re[j] += i
            if j == 0:
                k = 1
            elif j == numRows-1:
                k = -1
            j += k

        #return  "".join(re)
        return re


s = "abcdefghijklmn"
temp_class = Solution()
print(temp_class.convert(s, 4))

# coding:utf-8

__author__ = "sn"

"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

"""
思路：
二层循环，第一层控制haystack遍历，第二层判断是否与needle相等；
time O(N*M) space O(1)
测试发现python切片的效率还高一些；

"""
import time

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1


    #pythonic            
    def strStr1(self, haystack, needle):
        print("pythonic")

        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


time_start = time.time()
haystr = "abcdefghijkl"
nee = "cde"
so = Solution()
print(so.strStr(haystr, nee))
print(time.time()- time_start)    
                

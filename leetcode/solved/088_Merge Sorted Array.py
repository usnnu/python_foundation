# coding:utf-8

__author__ = "sn"

"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

"""
解法：
1.最简方法，从nums2向nums1插入，不过效率较低；因为移动比较多
2.新生成一个列表，分别取最小值插入，插入m+n次，无移动；
3.倒序插入，向nums1尾部插入，利用空闲位；

"""
class Solution():
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums1[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]



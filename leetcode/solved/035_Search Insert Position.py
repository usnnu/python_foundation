# coding:utf-8

__author__ = "sn"

"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

"""

"""
思路：
1.顺序查找（无代码）
2.二分查找 time o(logn) space o(1)
3.其它几种pythonic的写法

"""

class Solution():
    def searchInsert(self, nums, target):

        if target < nums[0]:
            return 0

        if target >= nums[-1]:
            return len(nums)

        start, end = 0, len(nums)-1
        while start <= end:
            m = (start + end)/2
            if nums[m] > target:
                end = m -1
                if end >=0:
                    if nums[end] < target:
                        return end + 1
                else:
                    return 0
            elif nums[m] < target:
                start = m + 1
                if start < len(nums):
                    if nums[start] > target:
                        return end
                else:
                    return len(nums)
            else:
                return m



    def searchInsert(self, nums, target):
        retrun len[x for x in numx if x < target]

    def searchInsert(self, nums, target):
        return sorted(nums + [target]).index(target)

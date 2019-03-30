# coding:utf-8

__author__ = "sn"

"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.

"""

"""
思路：
1.复写掉数组中等于val的元素：定义J表示数组中当前有效位置，遍历数组，如元素！=val，nums[j]=nums[i],j+=1;
返回nums[:j]

"""



class Solution():
    def removeElement(self, nums, val):
        j = 0
        for i in nums:
            if num != val:
                nums[j] = i
                j += 1
        return j


    #改进，将等于val的元素交换到数组尾部
    def removeElement(self, nums, val):
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start
    
    









    

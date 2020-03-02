# coding:utf-8

__author__ = "sn"

"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""

"""
方法1：

两个参数，一个用于保存现值，一用于计数；
方法2：
将现值保存于列表中，缺点是会改变列表；符合题目要求；


"""


class Solution():
    def removeDuplicates(self, nums):
        """

        """
        if not nums:
            return 0
        
        length = 1
        x = nums[0]
        for i in nums[1:]:
            if i != x:
                length +=1
            x = i
        return length

    def removeDuplicates1(self, nums):
        
        if not nums:
            return 0
        
        tailnum = 0
        for i in range(0,len(nums)):
            if nums[i] != nums[tailnum]:
                tailnum += 1
                nums[tailnum] = nums[i]

        return tailnum + 1


nums = [1,2,3,3,4,5]
solu = Solution()
print(solu.removeDuplicates1(nums))
    

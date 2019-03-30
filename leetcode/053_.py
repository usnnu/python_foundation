# coding:utf-8

__author__ = "sn"

"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

"""

"""
思路：
1.遍历
2.动态规划
对于任意一个元素，如果左侧元素的连续组合最大值为负，那么可以以该元素为现最大值；
但现最大值并不一定是整个数组下的连续组合最大值，另设一参数保存该值；
有点像递归；

3.分治
将数组均分为两个部分，那么最大数组会存在于
左侧数组的最大子数组
右侧数组的最大子数组
左侧数组的以右侧边界为边界的最大子数组+右侧数组的以左侧边界为边界的最大子数组



"""



    
class Solution():
    def maxSubArray(self, nums):
        if not nums:
            return 0
        
        maxsum = nums[0]
        for i in range(len(nums)):
            sums = 0
            j = i
            while j <len(nums):
                sums += nums[j]
                j +=1
                if sums > maxsum:
                    maxsum = sums

        return maxsum


    
    def maxSubArray1(self, nums):
        if not nums:
            return 0

        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(maxsum, cursum)

        return maxsum

    #使用数组保存局部最大值
    def maxSumArray2(self, nums):
        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)
    
    #分治
    def maxSubArray3(self, nums):
        pass

a = [8,3,4,5,-3,4,-30,-3,2,4,30]        
so = Solution()

result = so.maxSubArray(a)
print(result)

#8，11，15，20，17，21，-9，-3，2，6，36

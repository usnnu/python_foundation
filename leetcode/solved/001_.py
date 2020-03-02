# coding:utf-8
"""
twosum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution():
    # 1
    '''
    def twoSum(self, nums, target):
        answer = []

        for i in range(len(num_length)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append([i,j])
        return answer
    '''

    
    # 返回一次，
    # 思路：列表中每一项与target的差值加上当前下标组成字典的项
    # 继续迭代时如在字典中找到该KEY，则value及当前列表下标及为所求下标组
    #问题：列表必须按小》大排序，否则会出现漏项
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        result = []
        di = {}
        for i in range(len(nums)):
            if nums[i] in di:
                result.append([di[nums[i]], i+1])
            else:
                di[target - nums[i]] = i+1
        return result   









lis = [1, 2, 3, 4, 5, 6,7,8,8,9,10, 10, 10,7,5,11,12,13,14]
a = Solution()
answer = a.twoSum(lis, 14)
print(answer)

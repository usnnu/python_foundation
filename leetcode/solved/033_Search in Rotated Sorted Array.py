# coding:utf-8

__author__ = "sn"

"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

"""


"""
思路：
1.顺序查找，O(N)
2.二分查找，O(LOGN)
    二分查找的问题在于需要处理最大值在中间的问题
    需要确定有序部分，有序部分在mid左侧或者右侧，采用排除法即可。


"""



def search(nums, target):
    if not target:
        return -1

    low, high = 0, len(nums)-1

    while low <= high:
        mid = low + (high-low)//2
        if target == nums[mid]:
            return mid

        if nums[low] < nums[mid]:
            if nums[low] <= target <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1



a = [5,6,7,8,9,11,1,2,3,4]
print(search(a, 9))
                

# coding:utf-8
# Container With Most Water
__author__ = "sn"
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
求最大容器
"""

"""
思路：
排除法
左右指针指向数组头尾，假设a[0]<a[n]，那么以a[0]为边界对应的最大面积为a[0]*[n-0]
左指针+1
对每一数组成员做同样操作，取面积中最大者即可

"""


class Solution(object):
    def maxArea(self, height):
        max = [0,0,0]
        start = 1
        end = len(height)-1

        while start < end:
            if height[start] <= height[end]:
                if max[2] <= height[start]*(end-start):
                    max = [start,end,height[start]*(end-start)]
                start +=1
            else:
                if max[2] <= height[end]*(end-start):
                    max = [start, end, height[end] * (end - start)]
                end -=1
        return max


s = [4,6,34,56,2,67,8,23,67,6]
temp_class = Solution()
print(temp_class.maxArea(s))

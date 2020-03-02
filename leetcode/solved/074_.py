# coding:utf-8

__author__ = "sn"

"""
74 search a 2D Matrix
Write an efficient algorithm that searches for a value in 
an m x n matrix. This matrix has the following properties:

1.Integers in each row are sorted from left to right.
2.The first integer of each row is greater than the last integer of the previous row.

"""

"""
解法：
根据描述，它是一个从左到右，从上到下依次增大的二维数组；
把它当做一个列表就行了，二分查找；

"""

class Solution():
    def searchMatrix(self, martix, target):
        if not martix or target is None:
            return False

        rows, cols = len(martix), len(martix[0])
        low, high = 0, rows * cols -1

        while low < high:
            mid = (low + high) // 2
            num = max[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False




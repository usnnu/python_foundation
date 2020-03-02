# coding:utf-8
__author__ = "sn"
# Median of Two Sorted Arrays
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
返回两串相加的中位值，如果两串长度之和为偶数，返回2个中位数相加/2
"""

"""
思路：
类似于二分查找
字符串a,b,返回第k个值，使用递归
lena > lenb 
如果a[k//2]<= b[k-k//2] 则a列表的前k//2项可以排除
如果a[k//2]> b[k-k//2] 则b列表的前k-k//2项可以排除
加上边界处理，逻辑等部分完成
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.findthek(nums1, nums2, length//2)
            pass
        else:
            return (self.findthek(nums1, nums2, length // 2)+self.findthek(nums1, nums2, length//2+1))/2

    # 返回第k位数
    def findthek(self, a, b, k):
        lena, lenb = len(a), len(b)
        if k == 0 or k > (lena + lenb):
            raise ValueError
        if lena < lenb:
            return self.findthek(b, a, k)

        if not b:
            return a[k - 1]
        if k == 1:
            return min(a[0], b[0])

        n = k // 2
        pa = min(lenb, n)
        if a[n - 1] <= b[pa - 1]:
            return self.findthek(a[n:], b, k - n)
        else:
            return self.findthek(a, b[lenb-pa:], k - pa)


l1 = [1, 3, 5, 7, 8, 9, 15, 17, 56]
l2 = [2, 4, 6, 8, 9, 15, 17, 54, 98]

temp_class = Solution()
print(temp_class.findMedianSortedArrays(l1, l2))

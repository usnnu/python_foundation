# coding:utf-8

__author__ = "sn"

"""
69 sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
Contributor

"""

"""
思路：
二分查找


"""

def mysqrt(x):
    if x == 0:
        return 0
    left, right = 1, x
    while true:
        mid = left + (right - left)//2
        if mid*mid >x:
            right = mid - 1
        else::
            if (mid+1)*(mid+1) > x:
                return mid
            left = mid + 1            
            
    

def mysqrt(x):
    r = x
    while r*r >x:
        r = (r + x//r)//2
    return r

num = 0
print(mysqrt(num))


    

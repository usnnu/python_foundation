# coding:utf-8

__author__ = "sn"

"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.


"""

"""
思路：
1.基本思路是做减法，但是显然太简单了
2.不能做减法，只能做位运算了


"""


def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            print(res)
            i <<= 1
            temp <<=1

    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)


print(divide(35, 4))

print((5>0) is (6>0))
    

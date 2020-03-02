# coding:utf-8

__author__ = "sn"

"""
Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

"""

"""
判断一个数字是否为回文，比较简单，可用2 种方法
1.字符串化，
2.取头尾数字进行比较


"""


class Solutiona(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        ls = int(str(x)[::-1])
        if ls == x:
            return True
        else:
            return False


class Solutionb(object):
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True


a = 101
print(a)
temp = Solutiona()
temp = Solutionb()
print(temp.isPalindrome(a))




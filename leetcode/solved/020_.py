# coding:utf-8

__author__ = "sn"

"""
20 20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


"""
思路：
使且栈，如果是左侧符号入栈；
如果是右侧符号则进行出栈操作并进行判断；
如果出栈失败函数返回False
前述步骤均通过返回True


"""


class Solution():
    def isValid(self, s):
        """

        """
        stack = []
        dic = {'(':')', '[':']', '{':'}'}
        for ch in s:
            if ch in dic:
                stack.append(ch)
                print("www")
            elif  stack == {} or dic[stack.pop()] !=ch:
                return False
        return not stack


s = "()"
so = Solution()
print(so.isValid(s))

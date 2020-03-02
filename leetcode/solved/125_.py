# coding:utf-8

__author__ = "sn"

"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，
只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""

"""
思路：

1.双指针
从边缘至中心迭代

2.先过滤再反向比较

"""


class Solution:
    def isPalindrome_pythonic(self, s: str) -> bool:
        """
        pythonic的写法。
        :param s:
        :return:
        """
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        """
        双指针实现。
        :param s:
        :return:
        """
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i + 1, j - 1
        return True



def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    input_str = 'abccba'
    #input_list = [7,6,4,3,1]
    for _ in func_list:
        func = getattr(so, _)
        res = func(input_str)
        print("方法：%s\r\n说明：%s"%( func.__name__, func.__doc__), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass














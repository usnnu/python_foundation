# coding:utf-8

__author__ = "sn"

"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


"""

"""
思路：


"""


class Solution(object):
    def reverseString_recursion(self, s) -> None:
        """
        递归
        逐一交换首尾元素。
        时间复杂度：O(N),N/2
        空间复杂度：O(N) 递归占用空间
        """
        def helper(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l + 1, r - 1)
        helper(0, len(s) - 1)
        return s


    def reverseString_pythonic(self, s) -> None:
        """
        pythonic.
        """
        s.reverse()
        return s

    def reverseString_pointer(self, s) -> None:
        """
        指针迭代
        时间复杂度：O(N)。执行了 N/2 次的交换。
        空间复杂度：O(1)，只使用了常数级空间。
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s


def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    input_str = ["h","e","l","l","o"]

    #input_list = [2,4,7,4,2,15,15,1,1]
    for i, _ in enumerate(func_list):
        input_str = ["h", "e", "l", "l", "o"]
        func = getattr(so, _)
        res = func(input_str)
        print("*"*40, "\r\n方法[%s]：%s\r\n说明：%s"%(i, func.__name__, func.__doc__.replace('    ', '')), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*2)
    print(input_str)



if __name__ == "__main__":
    test()
    pass














# coding:utf-8

__author__ = "sn"

"""
509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。
"""

"""
思路：

"""




class Solution(object):
    def fib_recursion(self, n):
        """
        递归求斐波那契数列第N项
        时间复杂度：O(2**N)，求解过程可以形象化为一颗二叉树，
        高度为N，所以简化化为2**N
        空间复杂度：O(N)
        :param n:
        :return:
        """
        #assert n < 20, '数值太大，不要测试'
        #if n >=20:return '数值太大，测试状态不运行！'
        if n <= 1:
            return n
        return self.fib_recursion(n-1) + self.fib_recursion(n-2)

    def fib_iteration(self, n):
        """
        递推法
        时间复杂度：O(N)
        空间复杂度：O(1)，只用了3个变量
        :param n:
        :return:
        """
        if n <= 2:
            return n
        p, q = 1, 1
        for x in range(3,n+1):
            p, q = q, p + q
        return q


import timeit
from collections import Iterable

def processing_func(cls, func_name, *ar, **kw):
    func = getattr(cls, func_name)

    if isinstance(ar[0], Iterable):
        res = func(*ar[0])
    else:
        res = func()
    # 打印执行结果
    print('执行结果：', res)



import timeit
def test_func(cls, *ar):

    # 方法执行耗时
    time_cost = dict()

    # 获取并执行Solution类中的解决方法
    func_list = [x for x in dir(cls) if not x.startswith('__')]
    print('\r\n', "共计有<%d>个方法："%(len(func_list)), func_list)
    # 设置参数


    # 依次执行Solution类中的方法
    for i, _ in enumerate(func_list):
        # 设置参数
        func = getattr(cls, _)
        # print(cls, func_num, func, ar)

        # 打印方法说明文档
        print("\r\n", "*" * 40, "\r\n方法[%s]：%s\r\n说明：%s" % (i, _, func.__doc__.strip()),)

        # 执行方法并记录执行时长
        t = timeit.timeit(stmt="processing_func(so, '{}', para)".format(_),
                      setup='from __main__ import processing_func, so, para',
                      number= 1
                      )
        time_cost[_] = t
    print('\r\n执行时长：{}'.format(time_cost), '\r\n'*2)


if __name__ == "__main__":
    # 实例化解决方案类
    so = Solution()
    # 参数设定
    para = (20, )

    test_func(so, para)
    pass

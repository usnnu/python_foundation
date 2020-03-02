# coding:utf-8

__author__ = "sn"

"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。
你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""

"""
思路：

"""




class Solution(object):
    def climbStairs_1(self, n: int) -> int:
        """
        暴力穷举法
        :param n:
        :return:
        """
        def clim_stairs(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            return clim_stairs(i+1, n) + clim_stairs(i+2, n)
        return clim_stairs(0, n)


    def climbStairs_2_1(self, n: int) -> int:
        """
        记忆化递归
        dict 实现
        时间复杂度：O(n)，树形递归的大小可以达到 n。
        空间复杂度：O(n)，递归树的深度可以达到 n。
        :param n:
        :return:
        """
        memo = dict()

        def climb_stairs(i, n, memo):
            if i > n: return 0
            if i == n: return 1
            if memo.get(i, 0): return memo.get(i)
            memo[i] = climb_stairs(i+1, n, memo) + climb_stairs(i+2, n, memo)
            return memo[i]
        return climb_stairs(0, n, memo)

    def climbStairs_2_2(self, n: int) -> int:
        """
        记忆化递归
        List 实现
        :param n:
        :return:
        """
        memo = [0]*n

        def climb_stairs(i, n, memo):
            if i > n: return 0
            if i == n: return 1
            if memo[i]: return memo[i]
            memo[i] = climb_stairs(i+1, n, memo) + climb_stairs(i+2, n, memo)
            return memo[i]
        return climb_stairs(0, n, memo)

    def climbStairs_dp(self, n):
        """
        动态规划
        时间复杂度：O(n)，单循环到n。
        空间复杂度：O(n)，dp数组用了n的空间。
        :param n:
        :return:
        """
        if n == 1:
            return 1

        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


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
    for i, _ in enumerate(func_list, 1):
        # 跳过
        if i == 1: continue
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
    print('\r\n执行时长：', *time_cost.items(), sep='\r\n')


if __name__ == "__main__":
    # 实例化解决方案类
    so = Solution()
    # 参数设定
    para = (19, )

    test_func(so, para)
    pass

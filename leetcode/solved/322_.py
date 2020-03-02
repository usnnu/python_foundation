# coding:utf-8

__author__ = "sn"

"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

说明:可以认为每种硬币的数量是无限的。
"""

"""
思路：
暴力穷举
动态规划

"""

class Solution:
    def coinChange_1_1(self, coins, amount):
        """
        暴力穷举
        递归
        def _helper(coins, num, leftamount, cur_coins_list):
        递归函数，coins：硬币池; num：下标; leftamount：剩余钱数; cur_coins_list:当前硬币序列
        时间复杂度：O(S^N)；因为最坏情况下每种硬币最多可能有S/Ci个；
        所以可能的组合数为S/C1 * S/C2 * S/C3 ......S/Cn=S^N/C1*C2*C3......Cn
        简化一下就是S^N
        S为金额，N为硬币种数。
        空间复杂度：O(N)最坏情况下，递归的最大深度为N。
        :param coins:
        :param amount:
        :return:
        """
        assert coins is not None and amount > 0, 'value error.'
        mincount = amount + 1
        # 反转coins排序方式为大至小
        coins = list(reversed(coins))

        # 递归函数
        def _helper(coins, num, leftamount, cur_coins_list):
            nonlocal mincount
            cur_coins_list.append(coins[num])

            length = len(cur_coins_list)
            if leftamount == 0:
                if length < mincount:
                    mincount = length
            elif leftamount > 0:
                if length >= mincount:
                    return
                for i in range(num, len(coins)):
                    _helper(coins, i, leftamount-coins[i], cur_coins_list[:])

        for x in range(len(coins)):
            _helper(coins, x, amount - coins[x], [])

        return -1 if mincount > amount else mincount

    def coinChange_1_2(self, coins, amount):
        """
        暴力穷举
        :param coins:
        :param amount:
        :return:
        """
        coins = list(reversed(coins))
        def _helper(index, coins, amount):
            if amount == 0: return 0

            if index < len(coins) and amount > 0:
                mincost = float('inf')
                for i in range(0, amount//coins[index]+1):
                    if amount >= i * coins[index]:
                        res = _helper(index+1, coins, amount - i * coins[index])
                        if res != -1:
                            mincost = min(mincost, res+i)
                return -1 if mincost == float('inf') else mincost
            return -1
        return _helper(0, coins, amount)

    def coinChange_2_1(self, coins, amount):
        """
        动态规划
        从下至上
        :param coins:
        :param amount:
        :return:
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_2_2(self, coins, amount):
        """
        动态规划/递归穷举/回溯法
        自上而下
        :param coins:
        :param amount:
        :return:
        """
        def _helper(coins, leftamount, count_list):
            if leftamount < 0: return -1
            if leftamount == 0: return 0
            if count_list[leftamount-1] != 0: return count_list[leftamount - 1]
            mincount = float('inf')
            for x in range(len(coins)):
                res = _helper(coins, leftamount - coins[x], count_list)
                if res >= 0 and res < mincount:
                    mincount = res + 1
            count_list[leftamount - 1] = mincount if mincount != float('inf') else -1
            return count_list[leftamount - 1]

        return _helper(coins, amount, [0]*amount)





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
        #if i == 1: continue
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
    li = [1,2,5,10,20]
    para = (li, 118)

    test_func(so, para)
    pass














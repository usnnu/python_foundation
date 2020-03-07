# coding:utf-8

__author__ = "sn"

"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，
请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
思路：
暴力穷举
动态规划

"""




class Solution:
    def minPathSum_1(self, grid):
        """
        暴力法
        时间复杂度 ：O(2^(m+n})。每次移动最多可以有两种选择。
        空间复杂度 ：O(m+n)。递归的深度是 m+n。
        :param grid:
        :return:
        """
        len_i, len_j = len(grid), len(grid[0])

        def _helper(grid, i, j, len_i, len_j):
            if i == len_i or j == len_j:
                return float('inf')
            if i == len_i - 1 and j == len_j - 1:
                return grid[i][j]
            return grid[i][j] + min(_helper(grid, i+1, j, len_i, len_j),
                                    _helper(grid, i, j+1, len_i, len_j),)

        return _helper(grid, 0, 0, len_i, len_j)

    def minPathSum_2(self, grid):
        """
        二维动态规划
        时间复杂度 ：O(mn)。遍历整个矩阵恰好一次。
        空间复杂度 ：O(n)。额外的矩阵。
        :param grid:
        :return:
        """
        len_i, len_j = len(grid), len(grid[0])
        dp = [[0 for _ in range(len_j)] for _ in range(len_i)]

        for i in range(len_i - 1, -1, -1):
            for j in range(len_j - 1, -1, -1):
                if i == len_i - 1 and j != len_j - 1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif j == len_j -1 and i != len_i - 1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif j != len_j -1 and i != len_i - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]

    def minPathSum_3(self, grid):
        """
        动态规划 一维数组
        上面的动态规划保存了整个矩阵，
        但实际只用保存一行/列的数据即可
        时间复杂度 ：O(mn)。遍历整个矩阵恰好一次。
        空间复杂度 ：O(n)。额外的一维数组，和一行大小相同。
        :param grid:
        :return:
        """
        len_i, len_j = len(grid), len(grid[0])
        dp = [0]*len_j

        for i in range(len_i - 1, -1, -1):
            for j in range(len_j - 1, -1, -1):
                if i == len_i - 1 and j != len_j - 1:
                    dp[j] = grid[i][j] + dp[j+1]
                elif j == len_j - 1 and i != len_i - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != len_i - 1 and j != len_j - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j+1])
                else:
                    dp[j] = grid[i][j]
        return dp[0]


    def minPathSum_4(self, grid: [[int]]) -> int:
        """
        动态规划
        不使用额外空间
        时间复杂度：O(MN）
        空间复杂度：O（1）
        :param grid:
        :return:
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]





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
    li = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    para = (li,)

    test_func(so, para)
    pass














# coding:utf-8

__author__ = "sn"

"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
"""

"""
思路：
暴力穷举
动态规划

"""

class Solution:
    def isMatch_1(self, s, p):
        """
        递归法
        原始写法
        :param s:
        :param p:
        :return:
        """
        if not p:
            return not s

        if len(p) > 1 and p[1] == '*':
            return self.isMatch_1(s, p[2:]) or \
                   ( s and p[0] in [s[0], '.'] and
                    self.isMatch_1(s[1:], p))
        else:
            return s and p[0] in [s[0], '.'] and self.isMatch_1(s[1:], p[1:])

    def isMatch_1_1(self, s, p):
        """
        递归法
        整理一下
        时间复杂度：
        空间复杂度：
        :param s:
        :param p:
        :return: bool
        """
        if not p:
            return not s

        first_match = s and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.isMatch_1_1(s, p[2:]) or (first_match and self.isMatch_1_1(s[1:], p))
        else:
            return first_match and self.isMatch_1_1(s[1:], p[1:])

    def isMatch_2(self, s, p):
        """
        记忆化搜索
        :param s:
        :param p:
        :return:
        """
        def _helper(s, p, mem):
            s_len, p_len = len(s), len(p)
            if p_len == 0: return s_len == 0

            if mem[s_len][p_len] is not None: return mem[s_len][p_len]
            first_match = s_len != 0 and p[0] in {s[0], '.'}
            if p_len > 1 and p[1] == '*':
                mem[s_len][p_len] = _helper(s, p[2:], mem) or \
                                    ( first_match and
                                     _helper(s[1:], p, mem))
            else:
                mem[s_len][p_len] = first_match and _helper(s[1:], p[1:], mem)
            return mem[s_len][p_len]

        s_len, p_len = len(s), len(p)
        mem = [[None for _ in range(p_len+1)] for _ in range(s_len + 1)]
        return _helper(s, p, mem)

    def isMatch_3_1(self, s, p):
        """
        动态规划
        自顶向下
        :param s:
        :param p:
        :return:
        """
        s_len, p_len = len(s), len(p)
        memo = {}

        def dp(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == p_len:
                return i == s_len
            first_match = i < s_len and p[j] in {s[i], '.'}
            if j <= p_len - 2 and p[j+1] == '*':
                tmp = dp(i, j+2) or first_match and dp(i+1, j)
            else:
                tmp = first_match and dp(i+1, j+1)
            memo[(i,j)] = tmp
            return tmp
        return dp(0,0)

    def isMatch_3_2(self, s, p):
        """
        动态规划
        自底向上
        :param s:
        :param p:
        :return:
        """
        if not p: return not s
        if not s and len(p) == 1:return False

        s_len, p_len = len(s), len(p)
        dp = [[False for _ in range(p_len + 1)] for _ in range(s_len+1)]
        dp[0][0] = True

        for j in range(2, p_len + 1, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = False
        return dp[-1][-1]




# 测试代码
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
    s = 'cc'
    p = 'c*a*.*'
    para = (s, p)
    # para = ('cc','cc*')
    para = ('cc', '.*')
    #para = ('aaccdd', 'a*d*.*t*')
    #para = ("aaab", "a*a*b")
    test_func(so, para)
    pass

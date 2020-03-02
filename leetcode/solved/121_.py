# coding:utf-8

__author__ = "sn"

"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），
设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
"""

"""
思路：

我们需要找出给定数组中两个数字之间的最大差值（即，最大利润）。此外，
第二个数字（卖出价格）必须大于第一个数字（买入价格）。
形式上，对于每组 ii 和 jj（其中 j > ij>i）需要找出 
max(prices[j] - prices[i])max(prices[j]−prices[i])。

1.暴力法

2.迭代


"""



class Solution(object):
    def maxProfit(self, prices) -> int:
        """
        暴力穷举任意两个元素之间的差值以得到最大值。
        时间复杂度 : O(N**2)。循环运行n(n-1)/2次。
        空间复杂度 : O(1)。只使用了一个变量。
        :param root:
        :return:
        """
        maxprofit = 0
        length = len(prices)
        for i in range(length - 1):
            for j in range(i+1, length):
                maxprofit = max(maxprofit, prices[j] - prices[i])
        return maxprofit


    def maxProfit_ergodic_once(self, prices):
        """
        一次遍历法
        时间复杂度：O(N)，只遍历一次。
        空间复杂度：O(1)，只使用了两个变量。
        :param prices:
        :return:
        """
        minprice, maxprofit = float('inf'), 0
        length = len(prices)
        for i in range(length):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
            else:
                pass
        return maxprofit





def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    input_list = [7,1,5,3,6,4]
    #input_list = [7,6,4,3,1]
    for _ in func_list:
        func = getattr(so, _)
        res = func(input_list)
        print("方法：%s\r\n说明：%s"%( func.__name__, func.__doc__), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass














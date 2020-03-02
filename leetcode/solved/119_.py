# coding:utf-8

__author__ = "sn"

"""
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
"""

"""
思路：
1.新行首末元素为1，中间元素计算方法如下：
new_row[i]=cur_row[i-1] + cur_row[i]

2. 新行等于上一行分别首尾加0后逐项相加
new_row = [a+b for a,b in zip([0]+cur_row, cur_row+[0])]

"""



class Solution:
    def getRow(self, rowIndex: int):
        """
        根据给定的行数，生成杨辉三角该行元素。
        :param rowIndex:杨辉三角的层数。
        :return:
        """
        if rowIndex <=0: return []
        cur_row = []
        for n in range(rowIndex+1):
            new_row = [None for _ in range(n + 1)]
            # 首末元素均为1
            new_row[0], new_row[-1] = 1, 1
            # 生成新行数据
            for j in range(1, n):
                new_row[j] = cur_row[j-1] + cur_row[j]
            cur_row = new_row
        return cur_row

    def getRow_2(self, row_nums):
        """
        根据给定行数返回杨辉三角该行元素。
        相比上一方法的改进之处是复用了当前列。
        以时间换空间。
        :param row_nums: 给定行数
        :return: res:list 该行元素
        """
        res = [1]
        for i in range(1, row_nums+1):
            res.insert(0,0)
            for j in range(i):
                res[j] = res[j] + res[j+1]
        return res

    def getRow_3(self, rowIndex):
        """
        根据给定行数返回杨辉三角该行元素列表。
        pythonic
        :param rowIndex:
        :return:
        """
        res = [1]

        for _ in range(rowIndex):
            res = [a+b for a,b in zip([0]+res, res+[0])]
        return res

def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*5, "方法列表：", func_list, '\r\n'*2)

    for _ in func_list:
        func = getattr(so, _)
        res = func(6)
        print("方法：%s\r\n说明：%s"%( func.__name__, func.__doc__), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass











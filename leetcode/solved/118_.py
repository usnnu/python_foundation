# coding:utf-8

__author__ = "sn"

"""
118. 杨辉三角
给定一个非负整数 numRows，
生成杨辉三角的前 numRows 行。

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
    def generate(self, numRows: int):
        """
        生成杨辉三角。
        :param numRows:杨辉三角的层数。
        :return:
        """
        res = []
        if numRows <=0: return res

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            # 首末元素均为1
            row[0], row[-1] = 1, 1
            # 生成新行数据
            for j in range(1, row_num):
                row[j] = res[row_num-1][j-1] + res[row_num-1][j]
            res.append(row)

        return res

    def generate_new(self, numRows: int):
        """
        生成杨辉三角。
        :param numRows:杨辉三角的层数。
        :return:
        """
        if numRows <= 0: return []
        res = [[1]]
        while len(res) < numRows:
            new_row = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(new_row)
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
        func_print_list(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass











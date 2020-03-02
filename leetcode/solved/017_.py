# coding:utf-8

__author__ = "sn"

"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，
返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。
注意：1 不对应任何字母。


"""

"""
思路：
穷举

"""


class Solution:
    def letterCombinations(self, digits):
        """
        回溯算法
        时间复杂度：O(a**N * 4**M）
        N为输入序列中有三个字母的数字键的数量，
        M对输入序列中有4个字母的数字键的数量；
        空间复杂度：O(3**N * 4**M）因为需要保存这么多个结果。
        :type digits: str
        :rtype: List[str]
        """
        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def backtrack(combination, next_digits):
            # 没有更多输入了
            if len(next_digits) == 0:
                # 结果添加到output
                output.append(combination)
            # 仍有输入
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[int(next_digits[0])]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

    def letterCombinations_pythonic(self, digits):
        """
        pythonic
        :param digits:
        :return:
        """
        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if not digits: return []
        res = ['']
        for i in digits:
            res = [x + y for x in res for y in phone[int(i)]]
        return res

def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    input_str = '3498'
    #input_list = [2,4,7,4,2,15,15,1,1]
    for i, _ in enumerate(func_list):
        func = getattr(so, _)
        res = func(input_str)
        print("*"*40, "\r\n方法[%s]：%s\r\n说明：%s"%(i, func.__name__, func.__doc__.replace('    ', '')), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*2)



if __name__ == "__main__":
    test()
    pass














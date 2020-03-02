# coding:utf-8

__author__ = "sn"

"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 
你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""

"""
思路：
总而言之要保存已经出现过的数，列表或HASH表；

另外一种思路是抵消法，a*a = 0？有的，xor操作。

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        1.遍历nums；
        2.如果数字是新的，加入暂存列表；
        3.如果数字已存在于暂存列表，删除它。

        时间复杂度：两次查询O(N**2)
        空间复杂度：O(N)，最坏情况下需要一个大小为N/2的列表。
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

    def singleNumber_hash(self, nums):
        """
        1.遍历nums
        2.查找has_table是否有当前元素
        3.如果没有，插入hash_table
        4.最后hash_table中仅有一个元素，即为目的元素。
        时间复杂度：O(N*1)=O(N)；
        与上一方法相比变化在于dict的pop操作时间复杂度为O(1)
        空间复杂度：O(N)
        :param nums: list[int]
        :return: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber_xor(self, nums):
        """
        异或运算
        原理：
        a xor 0 = a
        a xor a = 0
        XOR 满足交换律和结合律
        a xor b xor a = (a xor a) xor b = 0 oxr b = b
        换言之就是将数组中所有的数进行XOR操作，留下的便是唯一数。
        :param nums:
        :return:int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    #input_str = 'abccba'
    input_list = [2,4,7,4,2,15,15,1,1]
    for i, _ in enumerate(func_list):
        func = getattr(so, _)
        res = func(input_list)
        print("方法[%s]：%s\r\n说明：%s"%(i, func.__name__, func.__doc__), '\r\n执行结果：')
        #func_print_list(res)
        print(res)
        print('\r\n'*2)



if __name__ == "__main__":
    test()
    pass














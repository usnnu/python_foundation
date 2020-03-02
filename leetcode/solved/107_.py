# coding:utf-8

__author__ = "sn"

"""
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""

"""
思路：
1. 递归
2.迭代

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def levelOrderBottom_iteration(self, root: TreeNode):
        """
        返回给定二叉树自底向上的层次遍历列表。
        :param root:
        :return: list
        """
        res = []
        dq = deque([root,])
        while dq:
            cur_layer_val = []
            length = len(dq)
            for _ in range(length):
                node = dq.popleft()
                cur_layer_val.append(node.val)
                # 左右子树处理
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.insert(0, cur_layer_val)
        return res

    def levelOrderBottom(self, root: TreeNode):
        """

        :param root:
        :return:
        """
        res = []

        def func_recur(tr, depth):
            if not root: return
            if depth == len(res):
                res.insert(0, [])
            res[-(depth + 1)].append(root.val)
            func_recur(tr.left, depth + 1)
            func_recur(tr.right, depth + 1)

        func_recur(root, 0)
        return res



def test():
    from leet_code_pkg import BinaryTree
    t_c = BinaryTree()
    #t_c.binarytreemake()
    #t_c.print_tree_BFS_layer(t_c.tree)

    t= TreeNode
    bt = tr = t('a')
    tr.left, tr.right = t('b'), t('b')
    tr = bt.left
    tr.left, tr.right = t('c'), t('d')
    tr = bt.right
    tr.left, tr.right = t('d'), t('c')

    t_c.tree = bt
    t_c.print_tree_BFS_layer(t_c.tree)


    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*5, "方法列表：", func_list, '\r\n'*2)

    for _ in func_list:
        func = getattr(so, _)
        res = func(t_c.tree)
        print("方法：%s\r\n说明：%s"%( func.__name__, func.__doc__), '\r\n执行结果：')
        print(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass











# coding:utf-8

__author__ = "sn"

"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。
"""

"""
思路：

1. 递归
时间复杂度:O(n)
空间复杂度:O(h)，h是树的高度

2.迭代
时间复杂度:O(n)
空间复杂度:O(h)，h是树的高度


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    """
    """
    def inorderTraversal_recursion(self, root: TreeNode):
        """递归实现中序遍历二叉树"""
        res = []
        def dfs(tr):
            if not tr:
                return
            if tr.left:
                dfs(tr.left)
            res.append(tr.val)
            if tr.right:
                dfs(tr.right)

        dfs(root)
        return res

    def inorderTraversal_recursion(self, root: TreeNode):
        """迭代实现中序遍历二叉树"""

        res = []
        nq = []
        p = root

        while nq or p:
            if p :
                nq.append(p)
                p = p.left
            else:
                p = nq.pop()
                res.append(p.val)
                p = p.right




def test():
    from leet_code_pkg import BinaryTree
    t_c = BinaryTree()
    t_c.binarytreemake()
    t_c.print_tree_BFS_layer(t_c.tree)

    so = Solution()
    res = so.is_same_tree_queue()
    pass

if __name__ == "__main__":
    test()










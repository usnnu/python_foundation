# coding:utf-8

__author__ = "sn"

"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

"""

"""
思路：
解法1：
遍历节点，如果无子节点则记录该处深度，
比较所有深度，返回最大深度。

解法2：递归
任意节点的深度为左右子节点深度的较大值+1
如节点为空，深度为0

复杂度分析

时间复杂度：每个结点只访问一次，因此时间复杂度为 O(N)O(N)，
其中 N 是结点的数量。
空间复杂度：在最糟糕的情况下，树是完全不平衡的，
例如每个结点只剩下左子结点，递归将会被调用 NN 次（树的高度），
因此保持调用栈的存储将是 O(N)O(N)。
但在最好的情况下（树是完全平衡的），树的高度将是 \log(N)log(N)。
因此，在这种情况下的空间复杂度将是 O(\log(N))O(log(N))。




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
    递归
    return: 返回数字代表二叉树的深度。
    """
    def max_depth(self, root):
        if not root:
            return 0
        ldepth = self.max_depth(root.left)
        rdepth = self.max_depth(root.right)
        return max(ldepth, rdepth) + 1

    def _print_res(self, tr):
        res = self.max_depth(tr)
        print('二叉树的深度为 %d .'%(res))



def test():
    from leet_code_pkg import BinaryTree
    t_c = BinaryTree()
    t_c.binarytreemake()
    t_c.print_tree_BFS_layer(t_c.tree)

    so = Solution()
    so._print_res(t_c.tree)
    pass

if __name__ == "__main__":
    test()

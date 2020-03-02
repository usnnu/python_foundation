# coding:utf-8

__author__ = "sn"

"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，
则认为它们是相同的。
"""

"""
思路：
实质是遍历并比较，如果不等则返回。
解法1：
递归遍历节点，如果不等则返回，
时间复杂度：O(N)，因为每个节点访问一次。
空间复杂度：最优情况（完全二叉树）时为O(log(N))；
最坏情况（完全不平衡二叉树）时为O(N),用于维护递归栈。

解法2：
迭代层次遍历

时间复杂度：O(N),因为每个节点访问一次。
空间复杂度 : 最优情况（完全平衡二叉树）时为O(log(N))，
最坏情况下（完全不平衡二叉树）时为O(N)，用于维护双向队列。
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
    def is_same_tree_recursion(self, p, q):
        """递归法判断两棵树是否相同。"""
        if not p and not q:
            return True

        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return self.is_same_tree_recursion(p.left, q.left) and \
            self.is_same_tree_recursion(p.right, q.right)

    def is_same_tree_queue(self, p, q):
        """
        迭代法判断两棵树是否相同。
        :p: tree node
        :q:tree node
        :return: bool
        """
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        dq = deque([(p, q),])
        while dq:
            p, q = dq.popleft()
            if not check(p, q):
                return False

            if p:
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))

        return True




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










# coding:utf-8

__author__ = "sn"

"""
## 111. 二叉树的最小深度
题目：
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

"""

"""
思路：
遍历节点，如果无子节点则记录该处深度，
比较所有深度，返回最小深度。

DFS:
1.1 递归


1.2 

BFS:
2.1 迭代
2.2 栈


复杂度：
1 时间复杂度：
    平均和最坏为O(N)，N为树中节点数；
2 空间复杂度：
    最小深度前树的宽度；
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
    1.栈
    2.递归
    return: 返回数字代表二叉树的深度。
    """
    def minDepth_DFS_recursion(self, root: TreeNode):
        """
        递归遍历，找出最小深度

        复杂度分析
        N - 节点数量

        时间复杂度：O(N)
        访问所有节点一次

        空间复杂度：
        最坏情况下，树是非平衡树，O(N)
        最好情况下，完全平衡树，高度只有log(N)，这时复杂度只有O(log(N))

        :param root:
        :return:
        """
        if not root: return 0

        children = [root.left, root.right]
        if not any(children): return 1

        min_depth = float('inf')
        for x in children:
            if x:
                min_depth = min(self.minDepth_BFS_recursion(x), min_depth)
        return min_depth + 1
        pass

    def minDepth_BFS_queue(self, root: TreeNode):
        """

        :param root:
        :return:
        """
        if not root:
            return 0

        stack = deque([(root, 1),])

        while stack:
            node, depth = stack.popleft()
            if not node.left and not node.right: return depth
            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))



def test():
    from leet_code_pkg import BinaryTree
    t_c = BinaryTree()
    t_c.binarytreemake()
    t_c.print_tree_BFS_layer()

    so = Solution()
    res = so.minDepth_DFS_recursion(t_c.tree)
    print(res)
    pass

if __name__ == "__main__":
    test()










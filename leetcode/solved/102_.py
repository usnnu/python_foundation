# coding:utf-8

__author__ = "sn"

"""
102. 二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 
（即逐层地，从左到右访问所有节点）。

返回列表格式如下：
[
  [3],
  [9,20],
  [15,7]
]
"""

"""
思路：

1. 递归
时间复杂度：O(N)，因为每个节点恰好会被运算一次。
空间复杂度：O(N)，保存输出结果的数组包含 N 个节点的值。

2.迭代
时间复杂度：O(N)，因为每个节点恰好会被运算一次。
空间复杂度：O(N)，保存输出结果的数组包含 N 个节点的值。


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
    def levelOrder_recursion(self, root: TreeNode):
        """
        递归实现层次遍历二叉树，并逐层返回该层的值列表。
        :param root:
        :return: list
        """
        res = []
        if not root:
            return []

        def _recur_func(node, level):
            # start the current level
            if len(res) == level:
                res.append([])

            # append the currrent node value
            res[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                _recur_func(node.left, level + 1)
            if node.right:
                _recur_func(node.right, level + 1)

        _recur_func(root, 0)
        return res


    def levelOrder_iteration_t(self, root: TreeNode):
        """
        迭代实现层次遍历二叉树，并逐层返回该层的值列表。
        :param root:
        :return: res
        """
        if not root:
            return []

        res = [[]]
        len_cur, len_next = 1, 0
        dq = deque([root,])
        while dq:
            if len_cur:
                n = dq.popleft()
                len_cur -= 1
                res[-1].append(n.val)
                if n.left:
                    dq.append(n.left)
                    len_next += 1
                if n.right:
                    dq.append(n.right)
                    len_next += 1
            else:
                len_cur, len_next = len_next, 0
                res.append([])
        return res

    def levelOrder_iteration(self, root: TreeNode):
        """
        迭代实现层次遍历二叉树，并逐层返回该层的值列表。
        :param root:
        :return: res
        """
        res = []

        if not root:
            return res

        level = 0
        dq = deque([root,])

        while dq:
            # start the current level
            res.append([])
            # number of elements in the current level
            level_length = len(dq)

            for _ in range(level_length):
                node = dq.popleft()
                res[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            # go to the next level
            level += 1

        return res





def test():
    from leet_code_pkg import BinaryTree
    t_c = BinaryTree()
    t_c.binarytreemake()
    t_c.print_tree_BFS_layer(t_c.tree)

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*5, "方法列表：", func_list, '\r\n'*2)

    for _ in func_list:
        func = getattr(so, _)
        res = func(t_c.tree)
        print("方法：%s\r\n说明：%s"%( func.__name__, func.__doc__), '\r\n执行结果：')
        for element in res:
            print(element)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass











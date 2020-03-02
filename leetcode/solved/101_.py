# coding:utf-8

__author__ = "sn"

"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""

"""
思路：

1. 递归
算法的时间复杂度是O(n)，因为要遍历n个节点
空间复杂度是O(n)，空间复杂度是递归的深度，
也就是跟树高度有关，最坏情况下树变成一个链表结构，高度是n。

2.迭代
时间复杂度是O(n)，
空间复杂度是O(n)


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
    def isSymmetric_recursion(self, root: TreeNode) -> bool:
        """
        检查给定二叉树是否是镜像对称的。
        递归实现。
        :param root:
        :return: bool
        """
        if not root:
            return True

        def is_same(t1, t2):
            if t1 is None and t2 is None:
                return True

            if not all([t1, t2]):
                return False

            if t1.val != t2.val:
                return False

            return is_same(t1.left, t2.right) and is_same(t1.right, t2.left)
        return is_same(root.left, root.right)



    def isSymmetric_iteration(self, root: TreeNode) -> bool:
        """
        检查二叉树是否是镜像对称的。
        迭代实现。
        :param root:
        :return: bool
        """
        if not root or not (root.left or root.right):
            return True

        dq = deque([root.left, root.right])

        while dq:
            lt, rt = dq.popleft(), dq.popleft()
            # compare two node
            if not (lt or rt): continue
            if not (lt and rt): return False
            if lt.val != rt.val: return False

            # 子节点入队列
            dq.extend([lt.left, rt.right, lt.right, rt.left])
        return True



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











# coding:utf-8

__author__ = "sn"

"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""

"""
思路：
1.递归

2.迭代


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def isValidBST(self, root):
        """
        递归法判定给出的二叉树是否为BST。
        复杂度分析
        时间复杂度 : O(N)。每个结点访问一次。
        空间复杂度 : O(N)。跟进了整棵树。
        :param root:
        :return:
        """
        def func_recursion(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not func_recursion(node.left, lower, val):
                return False
            if not func_recursion(node.right, val, upper):
                return False
            return True

        return func_recursion(root)

    def isValidBST_iteration(self, root):
        """
        迭代法判断二叉树是否为BST
        复杂度分析
        时间复杂度 : O(N)O(N)。每个结点访问一次。
        空间复杂度 : O(N)O(N)。我们跟进了整棵树。
        :param root:
        :return:
        """
        if not root:
            return True

        stack =[(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            stack.append((node.left, lower, val))
            stack.append((node.right, val, upper))
        return True

    def isValidBST_inorder(self, root):
        """
        中序遍历
        :return:
        """
        if not root:
            return True

        dq = []
        prev = float('-inf')
        while dq or root:
            if root:
                dq.append(root)
                root = root.left
            else:
                root = dq.pop()
                if root.val > prev:
                    prev = root.val
                    root = root.right
                else:
                    return False


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
        #func_print_list(res)
        print(res)
        print('\r\n'*5)



if __name__ == "__main__":
    test()
    pass














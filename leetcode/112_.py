# coding:utf-8

__author__ = "sn"

"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.


"""

"""
思路：
按一定


"""

class solution():
    #2 dfs Recursively
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)



    #3 DFS with stack

    def hasPathsum3(self, root, sum):
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            curr, value = stack.pop()
            if not curr.left and not curr.right and curr.val == value:
                return True
            if curr.left:
                stack.append((curr.right, value - curr.val))
            if curr.right:
                stack.append((curr.left, value - curr.val))
        
        return False


    #4 BFS with queue

    def hasPathSum4(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False















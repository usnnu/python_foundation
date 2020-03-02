# coding:utf-8
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
思路：
值相加求余得本节点值，求整除10加入下一级
单链表负向解决办法
1.起始时多设置一个节点
2.返回时剔除该节点
3.问题，多余节点未回收

"""

class ListNode():
    def __init__(self, x=None, node=None):
        self.val = x
        self.next = node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        c = 0
        dummy = cur = ListNode(0)
        while l1 !=None or l2 != None or c == 1:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            cur.next = ListNode(c%10)
            cur = cur.next
            c = c//10
        return dummy.next




# 定义链表类
class ListNode_handle():
    def __init__(self):
        self.cur_node = None
        self.length = 0


    def add(self,data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        self.length +=1
        return node

    def print_ListNode(self):
        node = self.cur_node
        while node:
            print(node, node.val, node.next)
            node = node.next

    def reverse_ListNode(self):
        pre = self.cur_node
        cur = self.cur_node.next
        pre.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        self.cur_node = pre



# 测试
l1 = ListNode(4,ListNode(7,ListNode(5)))
l2 = ListNode(4,ListNode(5,ListNode(7)))

lt = Solution()
llt = lt.addTwoNumbers(l1,l2)

ls = llt
while ls:
    print(ls.val)
    ls = ls.next



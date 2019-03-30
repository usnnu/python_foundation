# coding:utf-8

__author__ = "sn"

"""


"""

"""
思路：
需要3个指针，一个指向当前，一个指向start，一个当作中间变量
注意边界处理

"""



#coding:utf-8

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#生成链表
s = t = ListNode(0)
for i in range(5):
    node = ListNode(i)
    t.next = node
    t = node




class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <=1:
            return head
        curr = head.next
        if curr or curr.next is None:
            return head
        pre_node = head
        while k>1:
            star = curr
            curr = curr.next
            star.next = pre_node
            pre_node = star
            if curr is None:
                break
            k -= 1

        head.next = curr
        return star

res = Solution()
result = res.reverseKGroup(s.next,4)

slt = result
print("result")
while slt is not None:
    print(slt.val)
    slt = slt.next

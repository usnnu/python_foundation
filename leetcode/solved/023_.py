# coding:utf-8

__author__ = "sn"

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
链表合并并保持顺序

"""

"""
思路：
1.使用列表，将所有节点加入，排序，再生成链表，但不符合要求；
2.抛出2个链表，合并为1个，再抛出1个与现有列表合并，重复至只剩一个链表
选取链表使用了递归
时间开销：O(kN)
空间开销：O(1)

3.取每个链表的头，比较大小，选取最小的加入，重复至完成...
Time complexity : O(kN)O(kN) where \text{k}k is the number of linked lists.
Space complexity :
O(n)O(n) Creating a new linked list costs O(n)O(n) space.
O(1)O(1) It's not hard to apply in-place method - connect selected nodes instead of creating new nodes to fill the new linked list.


"""



class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge(lis1, lis2):
            result = pt = ListNode(0)
            while lis1 and lis2:
                if lis1.val > lis2.val:
                    pt.next = lis1
                    lis1 = lis1.next
                else:
                    pt.next = lis2
                    lis2 = lis2.next
                pt = pt.next
            pt.next = lis1 if not lis2 else lis2
            return result.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)/2
        left = mergeKLists(lists[:mid])
        right = mergeKLists(lists[mid:])

        return merge(left,right)
		
		
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        temp_lst = []
        lists_len = len(lists)
        for item in enumerate(lists):
            temp_lst.append(item.val)
        while lists_len > 1:
            k=min(temp_lst)
            index = temp_lst.index(k)
            if lists[index].next == None:
                temp_lst.pop(index)
                lists.pop(index)
            else:
                lists[index] = lists[index].next
                temp_lst[index] = lists[index].val 
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

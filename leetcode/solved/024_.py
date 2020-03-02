# coding:utf-8

__author__ = "sn"

"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，
而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

"""
思路：
1.递归

2.迭代

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归法
        交换前两个结点，递归后续链表
        时间复杂度：O(N)，
        空间复杂度：O(N)，递归过程使用的堆栈空间。
        :param head:
        :param n:
        :return:ListNode
        """

        if not head or not head.next:
            return head

        q = head.next
        head.next = self.swapPairs(q.next)
        q.next = head
        return q




    def swapPairs_iteration(self, head: ListNode) -> ListNode:
        """
        迭代
        A->B->C->D
        交换BC：
        t = a
        t.next = c
        b.next, c.next = c.next, b
        # 清理以进行下一步
        head, t = b.next, b

        时间复杂度：O(L)
        空间复杂度O(1)
        :param head:
        :param n:
        :return:ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy

        while head and head.next:
            p = head.next
            prev_node.next = p
            head.next, p.next = p.next, head
            prev_node, head = head, head.next
        return dummy.next






def func_print_list(li):
    for _ in li:
        print(_)

def test():

    # 获取并执行Solution类中的解决方法
    so = Solution()
    func_list = [x for x in dir(so) if not x.startswith('__')]
    print('\r\n'*2, "方法列表：", func_list, '\r\n'*2)

    # 生成链表
    from leet_code_list_pkg import LinkedList
    ll_class = LinkedList()
    linked_list = ll_class.make_linkedlist(list(range(1,10)))
    ll_class.print_linkedlist(linked_list)

    # 设置参数
    #para = (linked_list, 3)

    # 依次执行Solution类中的方法
    for i, _ in enumerate(func_list):
        # 设置参数
        linked_list = ll_class.make_linkedlist(list(range(1, 10)))
        para = (linked_list, )
        func = getattr(so, _)
        res = func(*para)
        # 打印方法说明文档
        print("*"*40, "\r\n方法[%s]：%s\r\n说明：%s"%(i, func.__name__, func.__doc__.replace('    ', '')), '\r\n执行结果：')
        # 打印执行结果
        ll_class.print_linkedlist(res)
        #func_print_list(res)
        #print(res)
        print('\r\n'*2)



if __name__ == "__main__":
    test()
    pass














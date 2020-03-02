# coding:utf-8

__author__ = "sn"

"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

"""
思路：

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k: int):
        """
        每k个结点为一组进行翻转
        在首部添加dummy后使用尾插法实现
        边界处理方法为如果最后一次翻转的结点数量小于k，对该组结点再翻转一次
        时间复杂度：O(N)+O(k)= O(N)，遍历一次
        空间复杂度：O(1)
        :param head:
        :param k:
        :return:
        """
        dummy = ListNode(0)
        dummy.next = head

        p = dummy

        while p and p.next:
            # k个为一组进行翻转
            pre, p = p, p.next
            n = k
            while n > 1 and p.next:
                q = p.next
                p.next, q.next = q.next, pre.next
                pre.next = q
                n -= 1
            # 尾部结点不足k个处理
            if n > 1:
                p = pre.next
                while p.next:
                    q = p.next
                    p.next, q.next = q.next, pre.next
                    pre.next = q
                break
        return dummy.next


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
        linked_list = ll_class.make_linkedlist(list(range(1, 18)))
        para = (linked_list, 5)
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














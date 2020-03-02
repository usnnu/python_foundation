# coding:utf-8

__author__ = "sn"

"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int):
        """
        尾插法
        :param head:
        :param n:
        :return:ListNode
        """
        prev = head
        for x in range(m-2):
            prev = prev.next
        p = prev.next
        for y in range(m, n):
            q = p.next
            p.next, q.next = q.next, prev.next
            prev.next = q
        return head

    def reverseBetween_recursion(self, head: ListNode, m: int, n: int):
        """
        递归法
        """

        def _helper(head, num):
            if not num or not head or not head.next:
                return head
            new_head = _helper(head.next, num-1)
            t = head.next.next
            head.next.next = head
            head.next = t
            return new_head

        prev = head
        for i in range(m-2):
            prev = prev.next
        prev.next = _helper(prev.next, n-m)
        return head


    def reverseBetween_interchangedata(self, head: ListNode, m: int, n: int):
        """
        递归互换val
        """
        if not head: return None

        left, right = head, head
        stop = False

        def _helper_recursion(right, m, n):
            nonlocal left, stop

            if n == 1: return
            right = right.next
            if m > 1:
                left = left.next

            _helper_recursion(right, m-1, n-1)

            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        _helper_recursion(right, m, n)
        return head







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
        para = (linked_list, 3, 6)
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














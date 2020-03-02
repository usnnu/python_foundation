# coding:utf-8

__author__ = "sn"

"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，
并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
"""

"""
思路：
1.问题可以转换为删除第len(list)-n+1个结点。
当然这需要两次遍历链表。

2.在解决链表环的问题时有一种方法：快慢指针法
如果指针2比指针1慢n步，当指针1指向链表尾端时，
指针2会指向第len(list)-n个结点



"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd_twice(self, head: ListNode, n: int):
        """
        双遍历法，
        第一次得出链表长度；
        第二次删除结点。
        时间复杂度O(L)L为链表长度，操作执行了 2L-n2L−n 步，时间复杂度为 O(L)O(L)。
        空间复杂度：O(1)常量级额外空间。
        :param head:
        :param n:
        :return:ListNode
        """
        before_head = ListNode(0)
        before_head.next = head

        length = 0
        node = before_head
        while node:
            length += 1
            node = node.next
        # 获取需要删除的结点的编号
        length = length - n
        node = before_head
        # 找到目的结点的前一结点，所以需要减1
        for _ in range(length - 1):
            node = node.next
        # 删除结点
        node.next = node.next.next
        return before_head.next


    def removeNthFromEnd_onece(self, head: ListNode, n: int):
        """
        单次遍历法，
        快慢指针，后一个指针慢n步；
        当前指针到达尾部，后指针指向删除结点前一结点。
        时间复杂度：O(L)
        空间复杂度O(1)
        :param head:
        :param n:
        :return:ListNode
        """
        before_head = ListNode(0)
        before_head.next = head

        fir, sec = before_head, before_head
        # 考虑到添加了一个结点，循环次数+1
        for i in range(n+1):
            fir = fir.next

        while fir != None:
            fir, sec = fir.next, sec.next
        sec.next = sec.next.next
        return before_head.next


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
        para = (linked_list, 3)
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














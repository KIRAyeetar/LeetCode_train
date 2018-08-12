# encoding:utf-8

"""
two method to deal with the problem
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result_tmp = ListNode(0)
    result = result_tmp

    while True:
        l1_var = l1.val if l1 is not None else 0
        l2_var = l2.val if l2 is not None else 0

        tmp = l1_var + l2_var + result_tmp.val
        result_tmp.val = tmp % 10
        carry = int(tmp) / 10

        if l1 is not None: l1 = l1.next
        if l2 is not None: l2 = l2.next
        if (l1 is None) & (l2 is None): break
        else:
            result_tmp.next = ListNode(carry)
            result_tmp = result_tmp.next
    if carry==0:
        return result
    else:
        result_tmp.next = ListNode(carry)
        return result


def addTwoNumbers_sec(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result_tmp = ListNode(0)
    result = result_tmp
    while True:
        tmp = l1.val + l2.val + result_tmp.val
        result_tmp.val = tmp % 10
        carry = int(tmp) / 10
        if (l1.next is None) & (l2.next is None):
            if carry == 0:
                return result
            else:
                result_tmp.next = ListNode(carry)
                return result
        if l1.next is None:
            l1.val = 0
        else:
            l1 = l1.next

        if l2.next is None:
            l2.val = 0
        else:
            l2 = l2.next
        result_tmp.next = ListNode(carry)
        result_tmp = result_tmp.next


if __name__ == '__main__':
    a = ListNode(5)
    a.next = ListNode(3)
    a.next.next = ListNode(3)

    b = ListNode(5)
    b.next = ListNode(4)
    b.next.next = ListNode(5)

    node = addTwoNumbers(a, b)
    print(node.val)
    print(node.next.val)
    print(node.next.next.val)

    node = addTwoNumbers_sec(a, b)
    print(node.val)
    print(node.next.val)
    print(node.next.next.val)
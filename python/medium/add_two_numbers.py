"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    def get_rem(an ,bn ,rem):
        a , b = 0 ,0
        if an: a = an.val
        if bn: b = bn.val
        tot = a + b + rem
        return (tot % 10, int(tot / 10))

    output = []
    prev = None
    rem = 0
    while True:
        sum_ ,rem = get_rem(l1 ,l2 ,rem)
        node = ListNode(sum_)
        if prev:
            prev.next = node
        output.append(node)
        prev = node
        l1 = l1.next if (l1) else None
        l2 = l2.next if (l2) else None
        if (not l1) and (not l2):
            break
    if rem:
        output[-1].next = ListNode(rem)

    return output[0]


if __name__ == "__main__":
    pass
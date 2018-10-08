# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        len1, len2 = self.get_len(l1), self.get_len(l2)

        if len1 < len2:
            long_l, short_l = l2, l1
        else:
            long_l, short_l = l1, l2

        node, carry = self.recur(long_l, short_l, abs(len1 - len2))
        if not carry:
            return node
        new_node = ListNode(carry)
        new_node.next = node
        return new_node

    def recur(self, long_l, short_l, diff):
        if not long_l and not short_l:
            return (None, 0)
        if diff != 0:
            node = ListNode(long_l.val)
            node.next, carry = self.recur(long_l.next, short_l, diff - 1)
        else:
            node = ListNode(long_l.val + short_l.val)
            node.next, carry = self.recur(long_l.next, short_l.next, diff)
        node.val += carry
        next_carry, node.val = divmod(node.val, 10)
        return (node, next_carry)

    def get_len(self, l):
        l_len = 0

        while l:
            l = l.next
            l_len += 1

        return l_len



# naive one
class Solution:
    def addTwoNumbers(self, l1, l2):
        str1, str2 = [], []

        while l1:
            str1.append(l1.val)
            l1 = l1.next

        while l2:
            str2.append(l2.val)
            l2 = l2.next

        len1, len2 = len(str1), len(str2)
        if len1 < len2:
            str1 = [0] * (len2 - len1) + str1
        if len1 > len2:
            str2 = [0] * (len1 - len2) + str2

        tenth = 0
        ret = None
        for i in range(1, max(len1, len2) + 1):
            digit = str1[-i] + str2[-i] + tenth
            tenth = digit // 10
            digit = digit % 10

            node = ListNode(digit)
            node.next = ret
            ret = node

        if tenth:
            node = ListNode(tenth)
            node.next = ret
            ret = node

        return ret
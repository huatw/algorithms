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

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        cur = l1
        stack1 = []
        while cur:
            stack1.append(cur)
            cur = cur.next

        cur = l2
        stack2 = []
        while cur:
            stack2.append(cur)
            cur = cur.next

        stack1, stack2 = stack1[::-1], stack2[::-1]
        if len(stack2) > len(stack1):
            stack1, stack2 = stack2, stack1

        res = []
        tenth = 0
        for n1, n2 in zip(stack1, stack2):
            tenth, digit = divmod(n1.val + n2.val + tenth, 10)
            res.append(ListNode(digit))

        for n in stack1[len(stack2):]:
            tenth, digit = divmod(n.val + tenth, 10)
            res.append(ListNode(digit))

        if tenth:
            res.append(ListNode(tenth))

        res = res[::-1]
        for prev_node, next_node in zip(res, res[1:]):
            prev_node.next = next_node

        return res[0]

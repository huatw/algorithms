class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(None)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next




class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        tenth = 0

        while l1 and l2:
            digit = l1.val + l2.val + tenth
            tenth = digit // 10
            digit = digit % 10
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode(digit)
            cur = cur.next

        # tenth l1 l2
        rest = l1 or l2
        while rest and tenth:
            digit = rest.val + tenth
            tenth = digit // 10
            digit = digit % 10
            rest = rest.next
            cur.next = ListNode(digit)
            cur = cur.next

        cur.next = ListNode(tenth) if tenth else rest

        return dummy.next

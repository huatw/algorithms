class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next = head
        len = m - n + 1

        prev_end, next_start = dummy, head
        while m > 1:
            m -= 1
            prev_end = prev_end.next

        while n > 0:
            n -= 1
            next_start = next_start.next

        self.reverse(prev_end.next, len, prev_end, next_start)

        return dummy.next

    def reverse(self, head, len, prev_end, next_start):
        prev, cur = ListNode(None), head

        while len > 0:
            len -= 1
            curnext = cur.next
            cur.next = prev
            prev, cur = cur, curnext

        prev_end.next = prev
        head.next = next_start
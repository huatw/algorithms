class Solution:
    def rotateRight(self, head, k):
        if not head or not k:
            return head

        len = 1
        tail = head
        while tail.next:
            len += 1
            tail = tail.next

        k = len - (k % len)

        if k == len:
            return head

        ret = head
        while k > 1:
            k -= 1
            ret = ret.next

        tail.next = head
        retHead = ret.next
        ret.next = None

        return retHead


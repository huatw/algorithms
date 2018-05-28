class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head

        fast, slow = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

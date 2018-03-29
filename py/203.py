class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head
        ret = dummy

        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return ret.next




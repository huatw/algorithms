class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy

        while cur and cur.next and cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                temp = cur.next.next.next
                while temp and temp.val == cur.next.val:
                    temp = temp.next
                cur.next = temp

        return dummy.next




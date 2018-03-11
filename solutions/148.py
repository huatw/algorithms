# Onlogn merge sort
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)
        mid, middle.next = middle.next, None

        return self.mergeList(self.sortList(head), self.sortList(mid))


    def mergeList(self, head1, head2):
        dummy = ListNode(None)
        cur = dummy

        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next

        cur.next = head1 if head1 else head2

        return dummy.next


    def getMiddle(self, head):
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow




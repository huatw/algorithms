class Solution:
    def partition(self, head, x):
        l1 = ListNode(None)
        dummy_l1 = l1
        l2 = ListNode(None)
        dummy_l2 = l2

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None #!!! elsewise TLE
        l1.next = dummy_l2.next

        return dummy_l1.next





class Solution:
    def partition(self, head, x):
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy

        less_x_dummy = ListNode(None)
        cur_less_x = less_x_dummy

        while cur and cur.next:
            if cur.next.val < x:
                cur_less_x.next = cur.next
                cur_less_x = cur_less_x.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        cur_less_x.next = dummy.next

        return less_x_dummy.next
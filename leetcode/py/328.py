class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd_head, even_head = head, head.next
        cur_odd, cur_even = head, head.next

        while cur_even.next:
            cur_odd.next = cur_odd.next.next
            cur_odd = cur_odd.next
            cur_even.next = cur_even.next.next
            if cur_even.next:
                cur_even = cur_even.next

        cur_odd.next = even_head
        return odd_head


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd_head = ListNode(None)
        ret_odd_head = odd_head
        even_head = ListNode(None)
        ret_even_head = even_head

        while head:
            odd_head.next = head
            odd_head = odd_head.next
            even_head.next = head.next
            even_head = even_head.next

            head = head.next.next if head.next else None

        odd_head.next = ret_even_head.next

        return ret_odd_head.next


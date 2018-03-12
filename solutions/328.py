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

            head = head.next.next if head.next else head.next

        odd_head.next = ret_even_head.next

        return ret_odd_head.next




class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd_head = ListNode(None)
        ret_odd_head = odd_head
        even_head = ListNode(None)
        ret_even_head = even_head

        is_odd = True

        while head:
            if is_odd:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next

            head = head.next
            is_odd = not is_odd

        even_head.next = None
        odd_head.next = ret_even_head.next

        return ret_odd_head.next
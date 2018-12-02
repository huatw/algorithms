# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = dummy
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow




class Solution(object):
    def detectCycle(self, head):
        node_map = set()

        while head:
            if head in node_map:
                return head
            node_map.add(head)
            head = head.next

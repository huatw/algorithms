# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev, cur, next = None, head, head.next

        while next:
            cur.next = prev
            prev, cur, next = cur, next, next.next

        cur.next = prev

        return cur




class Solution:
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        node = head.next
        head.next = prev
        return self.reverseList(node, head)




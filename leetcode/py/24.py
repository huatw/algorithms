# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy

        while cur and cur.next and cur.next.next:
            nxt, nnxt = cur.next, cur.next.next
            cur.next = nnxt
            nxt.next = nnxt.next
            nnxt.next = nxt
            cur = nxt

        return dummy.next


# recur
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        next_node, next_head = head.next, head.next.next
        head.next, next_node.next = self.swapPairs(next_head), head
        return next_node



class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        ret = head.next
        head.next, ret.next = self.swapPairs(ret.next), head

        return ret

'''
1 2 3 4 5 6 7
1   2   3   4
  7    6   5
'''
class Solution:
    def reorderList(self, head):
        if not head:
            return head

        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        stack = []
        rest = slow
        while rest:
            stack.append(rest)
            rest = rest.next

        cur = head
        while cur != slow:
            node = stack.pop()
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        cur.next = None

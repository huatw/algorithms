class Solution:
    def reverseList(self, head):
        def recur(node, cont):
            if not node:
                return cont
            next_node = node.next
            node.next = cont
            return recur(next_node, node)

        return recur(head, None)


# 1 2 3 4 5
# O(1) space
class Solution:
    def reverseList(self, head):
        if not head:
            return

        prev_cur, cur = None, head
        while cur:
            next_cur = cur.next
            cur.next = prev_cur
            prev_cur, cur = cur, next_cur

        return prev_cur


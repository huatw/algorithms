class Solution:
    def deleteNode(self, node):
        if not node:
            return

        node.val = node.next.val
        node.next = node.next.next


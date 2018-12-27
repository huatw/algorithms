class Solution(object):
    def inorderSuccessor(self, root, p):
        def in_order_traversal(node):
            if not node:
                return

            # yield from in_order_traversal(node.left)
            for val in in_order_traversal(node.left):
                yield val
            yield node
            # yield from in_order_traversal(node.right)
            for val in in_order_traversal(node.right):
                yield val

        found = False
        for node in in_order_traversal(root):
            if found:
                return node
            if node == p:
                found = True

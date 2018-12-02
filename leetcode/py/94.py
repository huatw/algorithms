# recur
class Solution:
    def inorderTraversal(self, root):
        res = []
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            res.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)
        return res

# iter
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [(root, False)]

        while stack:
            node, is_left_traversed = stack.pop()
            if not is_left_traversed:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
            else:
                res.append(node.val)
                if node.right:
                    stack.append((node.right, False))

        return res


# morris
class Solution:
    def inorderTraversal(self, root):
        res = []
        cur = root

        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur
                temp = cur
                cur = cur.left
                temp.left = None
            else: # visit node, go right branch
                res.append(cur.val)
                cur = cur.right

        return res




class Solution:
    def inorderTraversal(self, root):
        def in_order_traversal(node):
            if not node:
                return
            yield from in_order_traversal(node.left)
            yield node.val
            yield from in_order_traversal(node.right)

        return list(in_order_traversal(root))

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


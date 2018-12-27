class Solution:
    def findTarget(self, root, k):
        def in_order_traversal(node):
            if not node:
                return
            yield from in_order_traversal(node.left)
            yield node.val
            yield from in_order_traversal(node.right)

        seen = set()
        for val in in_order_traversal(root):
            if val in seen:
                return True
            seen.add(k - val)
        return False

class Solution:
    def findTarget(self, root, k):
        seen = set()
        def inorder(node):
            if not node:
                return False
            if inorder(node.left) or k - node.val in seen:
                return True
            seen.add(node.val)
            return inorder(node.right)

        return inorder(root)


class Solution:
    def findTarget(self, root, k):
        stack = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            stack.append(node.val)
            traverse(node.right)

        traverse(root)

        lo, hi = 0, len(stack) - 1
        while lo < hi:
            if stack[lo] + stack[hi] > k:
                hi -= 1
            elif stack[lo] + stack[hi] < k:
                lo += 1
            else:
                return True
        return False
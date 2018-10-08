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
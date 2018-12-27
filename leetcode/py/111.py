class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left, right = float('inf'), float('inf')
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        return 1 + min(left, right)


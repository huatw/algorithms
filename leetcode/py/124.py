class Solution:
    def maxPathSum(self, root):
        self.ret = -float('inf')

        def recur(node):
            if not node:
                return 0

            left = max(0, recur(node.left))
            right = max(0, recur(node.right))

            self.ret = max(self.ret, left + right + node.val)

            return node.val + max(left, right)

        recur(root)
        return self.ret
class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0

        def recur(node):
            nonlocal res
            if not node:
                return 0
            left_len, right_len = recur(node.left), recur(node.right)
            res = max(res, left_len + right_len)
            return max(left_len, right_len) + 1

        recur(root)
        return res

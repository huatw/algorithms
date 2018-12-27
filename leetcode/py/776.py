class Solution:
    def splitBST(self, root, V):
        if not root:
            return [None, None]

        if root.val > V:
            left, right = self.splitBST(root.left, V)
            root.left = right
            return [left, root]
        else:
            left, right = self.splitBST(root.right, V)
            root.right = left
            return [root, right]
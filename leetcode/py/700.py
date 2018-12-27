class Solution:
    def searchBST(self, root, val):
        if not root:
            return

        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root

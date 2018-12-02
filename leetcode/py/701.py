class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root


class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        prev, cur = None, root
        while cur:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            return root.left


class Solution:
    def deleteNode(self, root, key):
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            left, right = root.left, root.right
            if left and right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = left
                return root.right
            return left or right


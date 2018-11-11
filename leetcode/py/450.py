class Solution:
    def deleteNode(self, root, key):
        if root == None:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.right and root.left:
                connect_node = root.right
                while connect_node and connect_node.left:
                    connect_node = connect_node.left
                connect_node.left = root.left
                return root.right
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None

class Solution:
    def flipEquiv(self, root1, root2):
        def recur(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return (recur(node1.left, node2.left) and recur(node1.right, node2.right)) or\
            (recur(node1.left, node2.right) and recur(node1.right, node2.left))

        return recur(root1, root2)

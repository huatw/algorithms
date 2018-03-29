class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def check(l_node, r_node):
            if l_node and r_node:
                return l_node.val == r_node.val
                    and check(l_node.left, r_node.right)
                    and check(l_node.right, r_node.left)

            return l_node == r_node

        return check(root.left, root.right)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def check(l_node, r_node):
            if not l_node and not r_node:
                return True
            if not l_node or not r_node or l_node.val != r_node.val:
                return False
            return check(l_node.left, r_node.right) and check(l_node.right, r_node.left)

        return check(root.left, root.right)


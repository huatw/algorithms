# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recur
class Solution:
    def preorderTraversal(self, root):
        res = []

        def recur(node):
            if not node:
                return

            res.append(node.val)
            recur(node.left)
            recur(node.right)

        recur(root)
        return res





# iter
class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res




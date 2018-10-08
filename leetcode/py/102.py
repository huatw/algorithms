# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recur
class Solution:
    def levelOrder(self, root):
        res = []

        def recur(level):
            vals = []
            next_level = []
            for node in level:
                if not node:
                    continue
                vals.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
            if vals:
                res.append(vals)
                recur(next_level)

        recur([root])
        return res






# iter
class Solution:
    def levelOrder(self, root):
        res = []
        stack = [root]
        while stack:
            level = []
            next_stack = []

            for node in stack:
                if not node:
                    continue
                level.append(node.val)
                next_stack.append(node.left)
                next_stack.append(node.right)

            if level:
                res.append(level)
            stack = next_stack

        return res

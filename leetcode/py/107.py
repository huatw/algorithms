# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        res = []
        def level_traverse(level):
            level_vals = []
            next_level = []
            for node in level:
                level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                level_traverse(next_level)
            res.append(level_vals)

        level_traverse([root])
        return res
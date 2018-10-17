# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        level = [root]

        while level:
            res.append(level[-1].val)

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return res

# DFS
class Solution:
    def rightSideView(self, root):
        res = []
        def recur(node, level):
            if not node:
                return
            if len(res) == level:
                res.append(node.val)
            recur(node.right, level + 1)
            recur(node.left, level + 1)

        recur(root, 0)
        return res




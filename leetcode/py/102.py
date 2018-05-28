# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        level = [root]
        res = []

        while level:
            nextLevel = []
            values = []
            for node in level:
                if node:
                    values.append(node.val)
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)

            res.append(values)
            level = nextLevel

        return res[:-1]
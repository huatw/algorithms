# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        level = [root]
        res = []
        order = True

        while level:
            order = not order
            nextLevel = collections.deque()
            values = []
            for node in level:
                if node:
                    values.append(node.val)
                    if order:
                        nextLevel.appendleft(node.right)
                        nextLevel.appendleft(node.left)
                    else:
                        nextLevel.appendleft(node.left)
                        nextLevel.appendleft(node.right)

            res.append(values)
            level = nextLevel

        return res[:-1]
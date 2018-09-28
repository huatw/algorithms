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



class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        stack = [root]
        order = True

        while stack:
            order = not order
            next_stack = []
            res.append([])
            for node in reversed(stack):
                res[-1].append(node.val)
                if order:
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)
                else:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)

            stack = next_stack

        return res
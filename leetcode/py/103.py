# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        level = [root]
        is_left_to_right = True
        while level:
            level_vals = []
            next_level = []
            for node in reversed(level):
                if not node:
                    continue
                level_vals.append(node.val)
                if is_left_to_right:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.append(node.right)
                    next_level.append(node.left)

            is_left_to_right = not is_left_to_right
            if level_vals:
                res.append(level_vals)
            level = next_level

        return res


'''
          1             1
    2          3        2 3
 4    5     6     7     7 6 5 4
8 9 10 11 12 13 14 15   8 9 10 11 12 13 14 15

stack: [1]
       [2, 3]
        ...
need a flag to indicate current traverse direction
go through stack from idx n - 0
2 3 -> append node.right node.left to next level
7 6 5 4 -> append node.left node.right ..
'''




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
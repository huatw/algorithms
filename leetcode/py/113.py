# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def pathSum(self, root, sum):
        res = []
        stack = [(root, 0, [])] if root else []

        while stack:
            next_stack = []
            for node, val, path in stack:
                new_val = val + node.val
                new_path = [*path, node.val]

                if new_val == sum and not node.left and not node.right:
                    res.append(new_path)
                else:
                    if node.left:
                        next_stack.append((node.left, new_val, new_path))
                    if node.right:
                        next_stack.append((node.right, new_val, new_path))

            stack = next_stack

        return res

# DFS
class Solution:
    def pathSum(self, root, sum):
        res = []

        stack = [(root, 0, [])] if root else []

        while stack:
            node, val, path = stack.pop()
            nsum = val + node.val
            npath = path[:] + [node.val]

            if node.left:
                stack.append((node.left, nsum, npath))
            if node.right:
                stack.append((node.right, nsum, npath))
            if not node.left and not node.right and nsum == sum:
                res.append(npath)

        return res





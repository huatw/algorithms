# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            return True

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# BFS
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        level = [(root, 0)]

        while level:
            new_level = []

            for node, val in level:
                nsum = val + node.val

                if not node.left and not node.right and nsum == sum:
                    return True
                if node.left:
                    new_level.append((node.left, nsum))
                if node.right:
                    new_level.append((node.right, nsum))

            level = new_level

        return False




# DFS
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        level = [(root, 0)]

        while level:
            node, val = level.pop()
            nsum = val + node.val

            if not node.left and not node.right and nsum == sum:
                return True
            if node.left:
                level.append((node.left, nsum))
            if node.right:
                level.append((node.right, nsum))

        return False





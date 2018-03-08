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





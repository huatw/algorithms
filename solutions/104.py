# BFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        def recur(level, depth = 0):
            if not level:
                return depth

            newLevel = []

            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            return recur(newLevel, depth + 1)

        return recur([root])




# DFS
class Solution(object):
    def maxDepth(self, root):
        def recur(node):
            if not node:
                return 0

            return 1 + max(recur(node.left), recur(node.right))

        return recur(root)




# iter BFS
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        res = 0
        level = [(root, 1)]

        while level:
            res = max(level[-1][1] - level[0][1], res)
            next_level = []
            for (node, val) in level:
                if node.left:
                    next_level.append((node.left, 2 * val - 1))
                if node.right:
                    next_level.append((node.right, 2 * val))
            level = next_level

        return res + 1


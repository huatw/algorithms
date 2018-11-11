# BFS
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return

        level = [root]
        res = None

        while level:
            next_level = []
            res = level[0].val
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return res

# DFS
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return
        max_depth = 0
        res = None

        def dfs(node, depth):
            nonlocal res, max_depth
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    res = node.val
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return res

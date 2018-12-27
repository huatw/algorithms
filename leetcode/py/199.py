# DFS
class Solution:
    def rightSideView(self, root):
        def dfs(node, depth, res):
            if node:
                if len(res) == depth:
                    res.append(node.val)
                dfs(node.right, depth + 1, res)
                dfs(node.left, depth + 1, res)
            return res

        return dfs(root, 0, [])


# BFS
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        level = [root]

        while level:
            res.append(level[-1].val)

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return res


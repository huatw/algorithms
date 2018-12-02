# recur
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        def bfs(level, res):
            if not level:
                return res
            res.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            return bfs(next_level, res)
        return bfs([root], [])



# iter
class Solution:
    def levelOrder(self, root):
        res = []
        stack = [root]
        while stack:
            level = []
            next_stack = []

            for node in stack:
                if not node:
                    continue
                level.append(node.val)
                next_stack.append(node.left)
                next_stack.append(node.right)

            if level:
                res.append(level)
            stack = next_stack

        return res

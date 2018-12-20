class Solution:
    def pathSum(self, root, total):
        res = []
        def dfs(node, cur_total, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and cur_total + node.val == total:
                res.append([*path])
            dfs(node.left, cur_total + node.val, path)
            dfs(node.right, cur_total + node.val, path)
            path.pop()

        dfs(root, 0, [])
        return res


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        res = []
        if root.left:
            for path in self.pathSum(root.left, sum - root.val):
                res.append([root.val] + path)
        if root.right:
            for path in self.pathSum(root.right, sum - root.val):
                res.append([root.val] + path)
        return res

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





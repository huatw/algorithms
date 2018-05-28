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





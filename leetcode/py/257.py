# DFS iter small-space-complexity
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        # node, path
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            new_path = [*path, str(node.val)]
            if not node.left and not node.right:
                res.append('->'.join(new_path))
            else:
                if node.left:
                    stack.append((node.left, new_path))
                if node.right:
                    stack.append((node.right, new_path))
        return res

# DFS iter
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        # node, path
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            new_path = [*path, str(node.val)]
            if not node.left and not node.right:
                res.append('->'.join(new_path))
            else:
                if node.left:
                    stack.append((node.left, new_path))
                if node.right:
                    stack.append((node.right, new_path))
        return res

# DFS
class Solution:
    def binaryTreePaths(self, root):
        res = []
        def recur(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append('->'.join(path))
            else:
                for next_node in [node.left, node.right]:
                    if next_node:
                        recur(next_node, path)
            path.pop()
        if root:
            recur(root, [])
        return res

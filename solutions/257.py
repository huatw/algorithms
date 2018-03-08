# DFS
class Solution(object):
    def binaryTreePaths(self, root):
        paths = []

        def recur(node, path):
            path.append(str(node.val))

            if not node.left and not node.right:
                paths.append('->'.join(path))
            else:
                if node.left:
                    recur(node.left, path)
                if node.right:
                    recur(node.right, path)

            path.pop()

        if root:
            recur(root, [])

        return paths




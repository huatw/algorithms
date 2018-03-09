# logN * logN
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        l_depth = self.calDepth(root.left)
        r_depth = self.calDepth(root.right, False)

        if l_depth == r_depth:
            return 2 ** (l_depth + 1) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def calDepth(self, root, isLeft = True):
        if not root:
            return 0

        depth = 1
        if isLeft:
            while root.left:
                depth += 1
                root = root.left
        else:
            while root.right:
                depth += 1
                root = root.right

        return depth


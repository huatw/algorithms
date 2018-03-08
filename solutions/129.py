class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0

        self.res = 0

        def recur(node, path = 0):
            newPath = path * 10 + node.val

            if node.left:
                recur(node.left, newPath)
            if node.right:
                recur(node.right, newPath)
            if not node.left and not node.right:
                self.res += newPath

        recur(root)
        return self.res




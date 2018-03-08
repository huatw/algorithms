class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.total = 0

        def recur(node, isLeft = False):
            if not node:
                return

            if isLeft and not node.left and not node.right:
                self.total += node.val

            recur(node.left, True)
            recur(node.right)

        recur(root)
        return self.total




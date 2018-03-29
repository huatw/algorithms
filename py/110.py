# DFS
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        def check(root):
            if not root:
                return 0

            l_depth = check(root.left)
            if l_depth is False:
                return False

            r_depth = check(root.right)
            if r_depth is False:
                return False

            if abs(l_depth - r_depth) > 1:
                return False

            return max(l_depth, r_depth) + 1

        return check(root) is not False




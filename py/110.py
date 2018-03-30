# DFS
class Solution(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0

            l_depth, r_depth = check(root.left), check(root.right)

            if abs(l_depth - r_depth) > 1:
                raise

            return max(l_depth, r_depth) + 1

        try:
            check(root)
            return True
        except:
            return False




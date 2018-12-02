class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0
            left_height = check(node.left)
            if left_height == -1:
                return -1
            right_height = check(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return check(root) != -1


# DFS
class Solution:
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




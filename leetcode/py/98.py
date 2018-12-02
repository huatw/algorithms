class Solution:
    def isValidBST(self, root):
        max_val = -float('inf')

        def traverse(node):
            nonlocal max_val
            if not node:
                return True

            if not traverse(node.left) or node.val <= max_val:
                return False

            max_val = node.val

            return traverse(node.right)

        return traverse(root)


class Solution(object):
    def isValidBST(self, root, less_than = float('inf'), more_than = -float('inf')):
        if not root:
            return True

        if root.val >= less_than or root.val <= more_than:
            return False

        return self.isValidBST(root.left, min(root.val, less_than), more_than) and self.isValidBST(root.right, less_than, max(root.val, more_than))



class Solution(object):
    def isValidBST(self, root):
        def recur(node):
            if not node:
                return True

            l_val = recur(node.left)
            if l_val is False:
                return False

            r_val = recur(node.right)
            if r_val is False:
                return False

            ret_min, ret_max = node.val, node.val

            if l_val is not True:
                if l_val[1] >= node.val:
                    return False
                ret_min = l_val[0]

            if r_val is not True:
                if r_val[0] <= node.val:
                    return False
                ret_max = r_val[1]

            return ret_min, ret_max

        return recur(root) is not False
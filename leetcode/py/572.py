class Solution:
    def isSubtree(self, s, t):
        def serialize(node):
            if not node:
                return 'None'
            return '(' + str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right) + ')'

        return serialize(t) in serialize(s)


class Solution:
    def isSubtree(self, s, t):
        def check(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            return check(n1.left, n2.left) and check(n1.right, n2.right)

        def dfs_check(n1, n2):
            if check(n1, n2) or (n1 and dfs_check(n1.left, n2)) or (n1 and dfs_check(n1.right, n2)):
                return True
            return False
        return dfs_check(s, t)

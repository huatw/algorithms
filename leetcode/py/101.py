class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def check(l_node, r_node):
            if not l_node and not r_node:
                return True
            if not l_node or not r_node or l_node.val != r_node.val:
                return False
            return check(l_node.left, r_node.right) and check(l_node.right, r_node.left)

        return check(root.left, root.right)


# stack based
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.right))
            stack.append((n1.right, n2.left))
        return True

# stack based DFS
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]

        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True



class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




# DFS stack
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]

        while stack:
            p_node, q_node = stack.pop()
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
                stack.append((p_node.right, q_node.right))
                stack.append((p_node.left, q_node.left))

            elif p_node != q_node:
                return False

        return True




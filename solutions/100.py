class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




# DFS
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




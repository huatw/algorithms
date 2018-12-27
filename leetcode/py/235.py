class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if q.val < root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if q.val > root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

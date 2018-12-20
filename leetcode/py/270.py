class Solution:
    def closestValue(self, root, target):
        if not root:
            return float('inf')

        close_val = self.closestValue(root.left, target) if target < root.val else self.closestValue(root.right, target)
        return root.val if abs(close_val - target) > abs(root.val - target) else close_val




class Solution:
    def closestValue(self, root, target):
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if target < root.val else root.right
        return res

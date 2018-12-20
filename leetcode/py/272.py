# O(N) O(K)
class Solution:
    def closestKValues(self, root, target, k):
        def in_order_traversal(node):
            if not node:
                return
            yield from in_order_traversal(node.left)
            yield node.val
            yield from in_order_traversal(node.right)

        res = collections.deque()
        for val in in_order_traversal(root):
            if len(res) == k:
                if abs(res[0] - target) < abs(val - target):
                    return list(res)
                else:
                    res.popleft()
            res.append(val)
        return list(res)

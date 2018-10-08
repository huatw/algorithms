# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive
class Solution:
    def pathSum(self, root, target):
        def recur(node, accs):
            if not node:
                return 0
            res = sum([acc == node.val for acc in accs])
            next_accs = [acc - node.val for acc in accs] + [target]
            return res + recur(node.left, next_accs) + recur(node.right, next_accs)
        return recur(root, [target])


# DFS
class Solution:
    def pathSum(self, root, sum):
        total = 0
        stack = [(root, {})] if root else []

        while stack:
            node, vn_map = stack.pop()
            new_map = collections.defaultdict(int, {node.val: 1})

            if node.val == sum:
                total += 1

            for v, n in vn_map.items():
                nsum = v + node.val
                if nsum == sum:
                    total += n
                new_map[nsum] += n

            if node.left:
                stack.append((node.left, new_map))
            if node.right:
                stack.append((node.right, new_map))

        return total

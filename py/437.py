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
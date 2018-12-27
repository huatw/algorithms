class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        level = [root]
        left_first = False
        while level:
            left_first = not left_first
            next_level = []
            level_vals = []
            for node in reversed(level):
                level_vals.append(node.val)
                if left_first:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            res.append(level_vals)
            level = next_level

        return res
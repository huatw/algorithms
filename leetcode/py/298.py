class Solution:
    def longestConsecutive(self, root):
        if not root:
            return 0
        res = 0
        stack = [(root, 0, float('inf'))]
        while stack:
            node, cur_len, p_val = stack.pop()
            res = max(res, cur_len)
            if not node:
                continue
            if node.val == p_val + 1:
                stack.append((node.left, cur_len + 1, node.val))
                stack.append((node.right, cur_len + 1, node.val))
            else:
                stack.append((node.left, 1, node.val))
                stack.append((node.right, 1, node.val))
        return res

class Solution:
    def longestConsecutive(self, root):
        def dfs(node, cur_len, p_val):
            if not node:
                return cur_len
            if node.val == p_val + 1:
                return max(dfs(node.left, cur_len + 1, node.val), dfs(node.right, cur_len + 1, node.val))
            return max(cur_len, dfs(node.left, 1, node.val), dfs(node.right, 1, node.val))

        return dfs(root, 0, float('inf'))


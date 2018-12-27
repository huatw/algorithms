import functools

class Solution:
    def rob(self, root):
        @functools.lru_cache(None)
        def dfs(node):
            if not node:
                return 0
            children_sum = dfs(node.left) + dfs(node.right)
            root_sum = node.val
            if node.left:
                root_sum += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                root_sum += dfs(node.right.left) + dfs(node.right.right)
            return max(root_sum, children_sum)
        return dfs(root)



class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left, right = dfs(node.left), dfs(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)

            return (now, later) # rob now or later

        return max(dfs(root))

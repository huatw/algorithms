# logN * logN
# def with_cache(fn):
#     cache = {}
#     def wrapper(node):
#         if node not in cache:
#             cache[node] = fn(node)
#         return cache[node]
#     return wrapper

class Solution:
    def countNodes(self, root):
        @functools.lru_cache(None)
        def dfs_left(node):
            return 1 + dfs_left(node.left) if node else 0

        @functools.lru_cache(None)
        def dfs_right(node):
            return 1 + dfs_right(node.right) if node else 0

        def recur(node):
            if not node:
                return 0

            left_height, right_height = dfs_left(node.left), dfs_right(node.right)
            if left_height == right_height:
                return 2 ** (left_height + 1) - 1
            return 1 + recur(node.left) + recur(node.right)

        return recur(root)

class Solution:
    def combine(self, n, k):
        res = []

        def dfs(idx, rest_k, path):
            if rest_k == 0:
                res.append(path)
                return

            for i in range(idx, n + 1):
                dfs(i + 1, rest_k - 1, path + [i])

        dfs(1, k, [])

        return res


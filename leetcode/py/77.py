class Solution:
    def combine(self, n, k):
        res = []

        def dfs(idx, rest_k, acc):
            if rest_k == 0:
                res.append([*acc])
                return
            for i in range(idx, n + 1):
                acc.append(i)
                dfs(i + 1, rest_k - 1, acc)
                acc.pop()
        dfs(1, k, [])
        return res

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


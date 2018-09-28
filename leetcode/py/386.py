# DFS
class Solution:
    def lexicalOrder(self, n):
        res = []
        def dfs(k):
            if k <= n:
                res.append(k)
                t = 10 * k
                for i in range(10):
                    dfs(t + i)

        for i in range(1, 10):
            dfs(i)

        return res
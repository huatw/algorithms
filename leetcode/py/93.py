# DFS
class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def dfs(rest, rest_n, path):
            if rest_n == 0 and not rest:
                res.append('.'.join(path))

            if rest_n == 0 or not rest:
                return

            for i, ch in enumerate(rest[:3]):
                if int(rest[:i + 1]) < 256:
                    dfs(rest[i + 1:], rest_n - 1, path + [rest[:i + 1]])
                if ch == '0' and i == 0:
                    break

        dfs(s, 4, [])
        return res

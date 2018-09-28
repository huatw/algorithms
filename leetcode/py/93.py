'''
first cut: 1 to 3
second cut: first cut + (1 to 3)
third cut: second cut + (1 to 3)

cut => check valid => terminate recursion / continute dfs
'''
class Solution:
    def restoreIpAddresses(self, s):
        res = []

        # dfs fn,
        # cuts: cuts we left
        # acc: accumulated cut string
        # rest_s: string to be cut
        def dfs(cuts, acc, rest_s):
            # terminate condition
            if cuts == 0 and not rest_s:
                res.append('.'.join(acc))

            if cuts == 0 or not rest_s:
                return

            for i in range(1, min(4, 1 + len(rest_s))):
                if int(rest_s[:i]) <= 255:
                    dfs(cuts - 1, [*acc, rest_s[:i]], rest_s[i:])
                if rest_s[0] == '0':
                    break

        # start dfs with initial setups
        dfs(4, [], s)

        return res



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

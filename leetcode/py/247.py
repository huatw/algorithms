class Solution:
    def findStrobogrammatic(self, n):
        MAPPING = {
            '1': '1',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }

        def dfs(lo, hi, path):
            if lo > hi:
                return [''.join(path)]
            res = []
            if lo == hi:
                for digit in '018':
                    path[lo] = digit
                    res += dfs(lo + 1, hi - 1, path)
            else:
                for digit in '01689':
                    if lo == 0 and digit == '0':
                        continue
                    path[lo], path[hi] = digit, MAPPING[digit]
                    res += dfs(lo + 1, hi - 1, path)
            return res
        return dfs(0, n - 1, [None] * n)


class Solution:
    def findStrobogrammatic(self, n):
        MAPPING = {
            '1': '1',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }

        res = []

        def recur(idx, rest, acc):
            if rest == 0:
                res.append(''.join(acc))
            elif rest == 1:
                for ch in '018':
                    acc[idx] = ch
                    recur(idx + 1, rest - 1, acc)
            else:
                for ch in '1698' if rest == n else '16980':
                    acc[idx] = ch
                    acc[-(idx + 1)] = MAPPING[ch]
                    recur(idx + 1, rest - 2, acc)

        recur(0, n, [''] * n)

        return res
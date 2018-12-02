# len(low) -> len(high) using q1
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

    def strobogrammaticInRange(self, low, high):
        if int(low) > int(high):
            return 0
        res = 0
        for n in range(len(low), len(high) + 1):
            for val in self.findStrobogrammatic(n):
                if int(high) >= int(val) >= int(low):
                    res += 1
        return res

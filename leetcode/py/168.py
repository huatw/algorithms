class Solution:
    def convertToTitle(self, n):
        res = []
        while n:
            n, remain = divmod(n, 26)
            if remain == 0:
                n, remain = n - 1, 26
            res.append(chr(remain - 1 + ord('A')))
        return ''.join(reversed(res))

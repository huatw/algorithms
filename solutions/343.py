class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        t = (n-2) // 3
        n -= t * 3
        total = 3 ** t

        return total * n


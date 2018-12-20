class Solution:
    def getMoneyAmount(self, n):
        cache = [[0] * (n + 1) for _ in range(n + 1)]

        for lo in range(n - 1, 0, -1):
            for hi in range(lo + 1, n + 1):
                cache[lo][hi] = float('inf')
                for pivot in range(lo, hi):
                    cache[lo][hi] = min(cache[lo][hi], pivot + max(cache[lo][pivot - 1], cache[pivot + 1][hi]))

        return cache[1][n]
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0

        res = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if res[i]:
                j = i
                while i * j < n:
                    res[i * j] = False
                    j += 1

        return sum(res) - 2
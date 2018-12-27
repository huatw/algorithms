# O(n2)
class Solution:
    def numTrees(self, n):
        dp = [1]

        for i in range(1, n + 1):
            dp.append(sum([dp[j] * dp[i - 1 - j] for j in range(i)]))

        return dp[-1]




import functools

class Solution:
    def numTrees(self, n):
        @functools.lru_cache(None)
        def dfs(num):
            return sum(dfs(i) * dfs(num - 1 - i) for i in range(num)) if num != 0 else 1

        return dfs(n)


'''
state transition:
    total(n) = total(0) * total(n - 1)
             + total(1) * total(n - 2)
             + total(2) * total(n - 3)
             ..
             + total(n - 2) * total(1)
             + total(n - 1) * total(0)


total(0) = 1
total(1) = total(0) * total(0) = 1
total(2) = total(0) * total(1) + total(1) * total(0) = 2
total(3) = total(0) * total(2) + total(1) * total(1) + total(2) * total(0) = 5
'''
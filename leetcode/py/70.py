class Solution:
    def climbStairs(self, n):
        dp = [0, 1]
        for _ in range(n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

class Solution:
    def climbStairs(self, n):
        prev, now = 0, 1
        for _ in range(n):
            prev, now = now, prev + now
        return now

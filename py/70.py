# DP
class Solution(object):
    def climbStairs(self, n):
        pre, now = 0, 1

        for i in range(n):
            pre, now = now, pre+now

        return now


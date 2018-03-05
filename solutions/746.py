# space On
class Solution(object):
    def minCostClimbingStairs(self, cost):
        res = [0, 0]

        for i, c in enumerate(cost):
            res.append(c + min(res[i], res[i+1]))

        return min(res[-1], res[-2])




# space O1
class Solution(object):
    def minCostClimbingStairs(self, cost):
        pSum, ppSum = 0, 0

        for i, c in enumerate(cost):
            pSum, ppSum = c + min(pSum, ppSum), pSum

        return min(pSum, ppSum)




'''
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3
-2, -2, -2, 3, 3
-2, -4, -6, -3 0
'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        diffs = [g - c for g, c in zip(gas, cost)]
        idx = None
        balance = 0
        for i, diff in enumerate(diffs):
            if balance > 0:
                balance = balance + diff
            else:
                balance = diff
                idx = i

        return idx
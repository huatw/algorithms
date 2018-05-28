#DP
class Solution(object):
    def findTargetSumWays(self, nums, S):
        level = {0: 1}

        for n in nums:
            newLevel = collections.defaultdict(int)

            for sm, cnt in level.items():
                newLevel[sm - n] += cnt
                newLevel[sm + n] += cnt

            level = newLevel

        return level[S]




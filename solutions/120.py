# DP
# n -> next level n or n+1
class Solution(object):
    def minimumTotal(self, triangle):
        res = [float('inf'), 0]

        for level in triangle:
            newRes = [float('inf')]
            for i, n in enumerate(level):
                newRes.append(min(res[i+1], res[i]) + n)
            res = newRes + [float('inf')]

        return min(res)




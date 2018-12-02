'''
states_at_level_n[i] =
    min(states_at_level_n-1[i], states_at_level_n-1[i - 1]) + triangle_at_level_n[i]

[             [inf, 0, inf, inf, inf]
  [2],        [     2, inf, inf, inf]
  [3,4],      [     5, 6,   inf, inf]
  [6,5,7],    [     11,10,  13,  inf]
  [4,1,8,3]   [     14,11,  21,  16 ]
]
'''
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        dp = [float('inf')] * (len(triangle) + 1)
        dp[1] = 0
        for level in triangle:
            for i, num in reversed(list(enumerate(level))):
                dp[i + 1] = min(dp[i + 1], dp[i]) + num

        return min(dp)

class Solution:
    def minimumTotal(self, triangle):
        res = [float('inf'), 0]

        for level in triangle:
            level_res = [float('inf')]
            for i, num in enumerate(level):
                level_res.append(min(res[i + 1], res[i]) + num)
            res = level_res + [float('inf')]

        return min(res)


'''
[[2], [3,4], [6,5,7], [4,1,8,3]]
follow up 如果 所有number放一行怎么办
[2, 3,4, 6,5,7, 4,1,8,3]
'''
def get_height(triangle):
    height = 0
    total = 0
    while total != len(triangle):
        height += 1
        total += height
    return height

def minimum_total(triangle):
    if not triangle:
        return 0

    height = get_height(triangle)
    dp = [float('inf')] * (height + 1)
    dp[1] = 0
    start = 0
    for t in range(1, height + 1):
        level = triangle[start:start + t]
        start += t
        for i, num in reversed(list(enumerate(level))):
            dp[i + 1] = min(dp[i + 1], dp[i]) + num

    return min(dp)
minimum_total([2, 3,4, 6,5,7, 4,1,8,3])

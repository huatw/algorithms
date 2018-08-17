'''
    r a b b b i t
  1 1 1 1 1 1 1 1
r 0 1 1 1 1 1 1 1
a 0 0 1 1 1 1 1 1
b 0 0 0 1 2 3 3 3
b 0 0 0 1 1 2 2 2
i 0 0 0 0 0 0 3 3
t 0 0 0 0 0 0 0 3
'''
# DP
class Solution:
    def numDistinct(self, s, t):
        res = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        res[0] = [1] * (len(s) + 1)

        for i, cht in enumerate(t):
            for j, chs in enumerate(s):
                # 左上角（匹配这个格子） + 左（丢弃这个格子，保持左边值）
                if cht == chs:
                    res[i + 1][j + 1] = res[i][j] + res[i + 1][j]
                else:
                    res[i + 1][j + 1] = res[i + 1][j]

        return res[-1][-1]


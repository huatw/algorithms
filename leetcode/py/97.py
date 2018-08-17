# DFS with memo
class Solution:
    def isInterleave(self, s1, s2, s3):
        memo = {}
        def dfs(i1, i2, i3):
            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]

            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)

            left, right = i1 < len(s1) and s1[i1] == s3[i3] and dfs(i1 + 1, i2, i3 + 1), i2 < len(s2) and s2[i2] == s3[i3] and dfs(i1, i2 + 1, i3 + 1),

            memo[(i1, i2, i3)] = left or right
            return memo[(i1, i2, i3)]

        return dfs(0, 0, 0)


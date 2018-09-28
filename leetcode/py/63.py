#DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0] * (n + 1) for i in range(m + 1)]
        res[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] != 1:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[-1][-1]
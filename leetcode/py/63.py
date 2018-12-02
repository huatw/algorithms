class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid):
        if not obstacle_grid or not obstacle_grid[0]:
            return 0

        M, N = len(obstacle_grid), len(obstacle_grid[0])

        res = [[0] * (N + 1) for _ in range(M + 1)]
        res[0][1] = 1

        for i in range(M):
            for j in range(N):
                if obstacle_grid[i][j] == 0:
                    res[i + 1][j + 1] = res[i][j + 1] + res[i + 1][j]

        return res[-1][-1]

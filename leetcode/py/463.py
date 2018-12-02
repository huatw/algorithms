class Solution:
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2

        return res

#DP
class Solution(object):
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        res = [[float('inf')] * (len(grid[0]) + 1) for i in range(len(grid) + 1)]
        res[0][1], res[1][0] = 0, 0

        for i, g in enumerate(grid):
            for j, v in enumerate(g):
                res[i+1][j+1] = grid[i][j] + min(res[i][j+1], res[i+1][j])

        return grid[-1][-1]



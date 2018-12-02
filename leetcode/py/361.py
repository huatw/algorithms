class Solution:
    def maxKilledEnemies(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0
        M, N = len(grid), len(grid[0])
        def calc_row_kill(i, j):
            total = 0
            for k in range(j, N):
                if grid[i][k] == 'E':
                    total += 1
                elif grid[i][k] == 'W':
                    break
            return total

        def calc_col_kill(i, j):
            total = 0
            for k in range(i, M):
                if grid[k][j] == 'E':
                    total += 1
                elif grid[k][j] == 'W':
                    break
            return total

        res = 0
        col_kills = [None] * N
        for i in range(M):
            row_kill = None
            for j in range(N):
                if grid[i][j] == 'W':
                    row_kill, col_kills[j] = None, None
                    continue
                if row_kill == None:
                    row_kill = calc_row_kill(i, j)
                if col_kills[j] == None:
                    col_kills[j] = calc_col_kill(i, j)
                if grid[i][j] == '0':
                    res = max(res, row_kill + col_kills[j])

        return res

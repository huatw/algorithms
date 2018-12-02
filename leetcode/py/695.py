# DFS
class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            total = 1
            for nx, ny in get_neighbors(x, y):
                total += dfs(nx, ny)
            return total

        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))

        return res

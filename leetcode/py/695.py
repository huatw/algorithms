# DFS
class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        cur_area = 0

        def dfs(x, y):
            nonlocal max_area, cur_area
            if not (row > x >= 0 and col > y >= 0 and grid[x][y] == 1):
                return
            cur_area += 1
            grid[x][y] = 0

            for (dx, dy) in directions:
                dfs(x + dx, y + dy)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cur_area = 0
                    dfs(i, j)
                    max_area = max(max_area, cur_area)

        return max_area
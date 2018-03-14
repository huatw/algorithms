# DFS
class Solution:
    def numIslands(self, grid):
        cnt = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':
                return

            grid[x][y] = '0'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)


        for x, row in enumerate(grid):
            for y, el in enumerate(row):
                if el == '1':
                    cnt += 1
                    dfs(x, y)

        return cnt
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

# BFS
class Solution:
    def numIslands(self, grid):
        cnt = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(x, y):
            dq = collections.deque()
            dq.append((x, y))
            grid[x][y] = 0

            while dq:
                i, j = dq.popleft()
                for (di, dj) in directions:
                    new_i, new_j = di + i, dj + j
                    if len(grid) > new_i >= 0 and len(grid[0]) > new_j >= 0 and grid[new_i][new_j] == '1':
                        dq.append((new_i, new_j))
                        grid[new_i][new_j] = 0

        for x, row in enumerate(grid):
            for y, el in enumerate(row):
                if el == '1':
                    cnt += 1
                    bfs(x, y)

        return cnt

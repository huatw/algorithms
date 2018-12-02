class Solution:
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        nodes_set = set()

        def dfs(x, y, base_x, base_y, path):
            if grid[x][y] == 0:
                return
            path.append((x - base_x, y - base_y))
            grid[x][y] = 0
            for nx, ny in get_neighbors(x, y):
                dfs(nx, ny, base_x, base_y, path)
            return path

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    nodes_set.add(tuple(dfs(i, j, i, j, [])))
        return len(nodes_set)



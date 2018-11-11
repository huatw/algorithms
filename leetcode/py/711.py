class Solution:
    def numDistinctIslands2(self, grid):
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        nodes_set = set()
        nodes = []
        base_node = None

        def dfs(x, y):
            if not (row > x >= 0 and col > y >= 0 and grid[x][y] == 1):
                return
            nodes.append((x - base_node[0], y - base_node[1]))
            grid[x][y] = 0
            for (dx, dy) in directions:
                dfs(x + dx, y + dy)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    base_node = (i, j)
                    nodes = [(0, 0)]
                    dfs(i, j)
                    nodes_set.add(tuple(sorted(nodes)))

        return len(nodes_set)
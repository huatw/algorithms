class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        M, N = len(matrix), len(matrix[0])
        seen_pacific, seen_atlantic = set(), set()

        def get_neighbors(x, y):
            DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in DIRECTIONS:
                nx, ny = dx + x, dy + y
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def dfs(x, y, seen):
            if (x, y) in seen:
                return
            seen.add((x, y))
            for nx, ny in get_neighbors(x, y):
                if matrix[nx][ny] >= matrix[x][y]:
                    dfs(nx, ny, seen)

        for i in range(M):
            dfs(i, 0, seen_pacific)
            dfs(i, N - 1, seen_atlantic)

        for i in range(N):
            dfs(0, i, seen_pacific)
            dfs(M - 1, i, seen_atlantic)

        return list(seen_pacific & seen_atlantic)

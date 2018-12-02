class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        def get_neighbors(x, y):
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in DIRECTIONS:
                nx, ny = dx + x, dy + y
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def with_cache(fn):
            node_len_map = {}
            def wrapper(x, y):
                if (x, y) not in node_len_map:
                    node_len_map[(x, y)] = fn(x, y)
                return node_len_map[(x, y)]
            return wrapper

        @with_cache
        def dfs(x, y):
            res = 0
            for nx, ny in get_neighbors(x, y):
                if matrix[nx][ny] > matrix[x][y]:
                    res = max(res, dfs(nx, ny))
            return res + 1

        return max(dfs(i, j) for i in range(M) for j in range(N))


class Solution:
    def longestIncreasingPath(self, matrix):
        if not len(matrix) or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        get_new_xy = lambda x, y: [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        is_valid_point = lambda x, y: M > x >= 0 and N > y >= 0

        def dfs(x, y, seen):
            if (x, y) not in seen:
                seen[(x, y)] = 1
                for nx, ny in get_new_xy(x, y):
                    if is_valid_point(nx, ny) and matrix[nx][ny] > matrix[x][y]:
                        seen[(x, y)] = max(seen[(x, y)], dfs(nx, ny, seen) + 1)
            return seen[(x, y)]

        seen = {}
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j, seen))
        return res


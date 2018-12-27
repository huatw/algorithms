class Solution:
    def longestLine(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        seen = set()

        DIRECTIONS = [[(1, 0), (-1, 0)], [(1, 1), (-1, -1)], [(-1, 1), (1, -1)], [(0, 1), (0, -1)]]

        def dfs(x, y):
            if matrix[x][y] == 0:
                return 0
            if (x, y) in seen:
                return 0
            seen.add((x, y))

            res = 0
            for ds in DIRECTIONS:
                dis = 1
                for dx, dy in ds:
                    nx, ny = x, y
                    while True:
                        nx, ny = nx + dx, ny + dy
                        if not (M > nx >= 0 and N > ny >= 0 and matrix[nx][ny] == 1):
                            break
                        seen.add((nx, ny))
                        dis += 1
                res = max(res, dis)
            return res

        return max(dfs(i, j) for j in range(N) for i in range(M))


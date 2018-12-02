class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        M, N = len(grid), len(grid[0])
        n_buildings = sum(val for row in grid for val in row if val == 1)
        hit = [[0] * N for _ in range(M)]
        dist_sum = [[0] * N for _ in range(M)]

        def bfs(x, y):
            visited = [[False] * N for _ in range(M)]
            visited[x][y] = True
            cnt = 1
            dq = collections.deque([(x, y, 0)])
            while dq:
                i, j, dist = dq.popleft()
                for di, dj in DIRECTIONS:
                    new_i, new_j, new_dist = i + di, j + dj, dist + 1
                    if 0 <= new_i < M and 0 <= new_j < N and not visited[new_i][new_j]:
                        visited[new_i][new_j] = True
                        if grid[new_i][new_j] == 0:
                            dq.append((new_i, new_j, new_dist))
                            dist_sum[new_i][new_j] += new_dist
                            hit[new_i][new_j] += 1
                        if grid[new_i][new_j] == 1:
                            cnt += 1
            return cnt == n_buildings

        if not all(bfs(x, y) for x in range(M) for y in range(N) if grid[x][y] == 1):
            return -1

        return min([dist_sum[x][y] for x in range(M) for y in range(N) if grid[x][y] == 0 and hit[x][y] == n_buildings] or [-1])

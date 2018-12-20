# dijkstra
class Solution:
    def shortestDistance(self, maze, start, destination):
        M, N = len(maze), len(maze[0])
        def get_next_point(x, y, dis):
            DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                steps = 0
                while 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 1:
                    steps += 1
                    nx, ny = nx + dx, ny + dy
                nx, ny = nx - dx, ny - dy
                if maze[nx][ny] == 0:
                    yield nx, ny, dis + steps

        is_destination = lambda x, y: [x, y] == destination

        hq = [(0, *start)]
        visited = {(start[0], start[1]): 0}

        while hq:
            dis, x, y = heapq.heappop(hq)
            if is_destination(x, y):
                return dis
            for nx, ny, ndis in get_next_point(x, y, dis):
                if (nx, ny) not in visited or visited[(nx, ny)] > ndis:
                    visited[(nx, ny)] = ndis
                    heapq.heappush(hq, (ndis, nx, ny))

        return -1



class Solution:
    def shortestDistance(self, maze, start, destination):
        M, N = len(maze), len(maze[0])
        def get_next_point(x, y, dis):
            DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRECTIONS:
                steps = 0
                nx, ny = x + dx, y + dy
                while 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 1:
                    steps += 1
                    nx, ny = nx + dx, ny + dy
                nx, ny = nx - dx, ny - dy
                if maze[nx][ny] == 0:
                    yield nx, ny, dis + steps

        is_destination = lambda x, y: [x, y] == destination

        dq = collections.deque([(*start, 0)])
        visited = {(start[0], start[1]): 0}

        res = float('inf')
        while dq:
            x, y, dis = dq.popleft()
            if is_destination(x, y):
                res = min(res, dis)
            for nx, ny, ndis in get_next_point(x, y, dis):
                if (nx, ny) not in visited or visited[(nx, ny)] > ndis:
                    visited[(nx, ny)] = ndis
                    dq.append((nx, ny, ndis))

        return res if res != float('inf') else -1

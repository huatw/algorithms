class Solution:
    def hasPath(self, maze, start, destination):
        M, N = len(maze), len(maze[0])
        def get_next_point(x, y):
            DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                while 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 1:
                    nx, ny = nx + dx, ny + dy
                nx, ny = nx - dx, ny - dy
                if maze[nx][ny] == 0:
                    yield nx, ny

        is_destination = lambda x, y: [x, y] == destination

        dq = collections.deque([start])
        visited = {(start[0], start[1])}

        while dq:
            x, y = dq.popleft()
            if is_destination(x, y):
                return True
            for nx, ny in get_next_point(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dq.append((nx, ny))

        return False

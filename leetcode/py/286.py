class Solution:
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return

        M, N = len(rooms), len(rooms[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def bfs(level, seen):
            steps = 0
            while level:
                next_level = []
                for (x, y) in level:
                    rooms[x][y] = min(rooms[x][y], steps)
                    for (nx, ny) in get_neighbors(x, y):
                        if (nx, ny) not in seen and rooms[nx][ny] > 0:
                            seen.add((nx, ny))
                            next_level.append((nx, ny))

                level = next_level
                steps += 1

        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    bfs([(i, j)], set())



class Solution:
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return

        M, N = len(rooms), len(rooms[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def bfs(level, steps, seen):
            next_level = []
            for (x, y) in level:
                rooms[x][y] = min(rooms[x][y], steps)
                for (nx, ny) in get_neighbors(x, y):
                    if (nx, ny) not in seen and rooms[nx][ny] > 0:
                        seen.add((nx, ny))
                        next_level.append((nx, ny))

            if next_level:
                bfs(next_level, steps + 1, seen)


        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    bfs([(i, j)], 0, set())

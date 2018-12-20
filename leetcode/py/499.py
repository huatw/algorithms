class Solution:
    def findShortestWay(self, maze, ball, hole):
        M, N = len(maze), len(maze[0])
        def get_next_point(x, y, path, dis):
            DIRECTIONS = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')] # dlru
            for dx, dy, ds in DIRECTIONS:
                nx, ny, npath = x + dx, y + dy, path + ds
                steps = 0
                while 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 1:
                    steps += 1
                    if [nx, ny] == hole:
                        yield nx, ny, npath, dis + steps
                    nx, ny = nx + dx, ny + dy
                nx, ny = nx - dx, ny - dy
                if maze[nx][ny] == 0:
                    yield nx, ny, npath, dis + steps

        is_hole = lambda x, y: [x, y] == hole

        hq = [(0, '', *ball)]
        visited = {(ball[0], ball[1]): (0, '')}

        min_dis, min_path = float('inf'), 'impossible'
        while hq:
            dis, path, x, y = heapq.heappop(hq)
            if (dis, path) > (min_dis, min_path):
                break
            for nx, ny, npath, ndis in get_next_point(x, y, path, dis):
                if is_hole(nx, ny):
                    min_dis, min_path = min((min_dis, min_path), (ndis, npath))
                elif (nx, ny) not in visited or visited[(nx, ny)] > (ndis, npath):
                    visited[(nx, ny)] = (ndis, npath)
                    heapq.heappush(hq, (ndis, npath, nx, ny))

        return min_path


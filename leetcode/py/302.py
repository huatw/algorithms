class Solution:
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        M, N = len(image), len(image[0])
        boundary = [float('inf'), -float('inf'), float('inf'), -float('inf')]

        def once(fn):
            seen = set()
            def wrapper(x, y):
                if (x, y) not in seen:
                    seen.add((x, y))
                    return fn(x, y)
            return wrapper

        def get_neighbors(x, y):
            DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRECTIONS:
                nx, ny = dx + x, dy + y
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def update_boundary(x, y):
            boundary[0] = min(boundary[0], x)
            boundary[1] = max(boundary[1], x)
            boundary[2] = min(boundary[2], y)
            boundary[3] = max(boundary[3], y)

        @once
        def dfs(x, y):
            if image[x][y] == '0':
                return
            update_boundary(x, y)
            for nx, ny in get_neighbors(x, y):
                dfs(nx, ny)

        dfs(x, y)
        return (boundary[1] - boundary[0] + 1) * (boundary[3] - boundary[2] + 1)



class Solution:
    def minArea(self, image, x, y):
        def first(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        top = first(0, x, lambda x: '1' in image[x])
        bottom = first(x, len(image), lambda x: '1' not in image[x])
        left = first(0, y, lambda y: any(row[y] == '1' for row in image))
        right = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))

        return (bottom - top) * (right - left)

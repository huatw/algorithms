# maintain a pq of border  mnlog(m + n)
class Solution:
    def trapRainWater(self, height_map):
        if not height_map or not height_map[0]:
            return 0

        m, n = len(height_map), len(height_map[0])
        hq = [] # min heap
        water = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(hq, (height_map[i][j], i, j))
                    height_map[i][j] = None

        while hq:
            height, i, j = heapq.heappop(hq)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if m > x > 0 and n > y > 0 and height_map[x][y] != None:
                    water += max(height - height_map[x][y], 0)
                    heapq.heappush(hq, (max(height_map[x][y], height), x, y))
                    height_map[x][y] = None

        return water

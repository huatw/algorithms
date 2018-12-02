# TLE
class Solution:
    def minAreaRect(self, points):
        points = set((x, y) for x, y in points)

        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in points and (x2, y1) in points:
                    res = min(res, abs((x1 - x2) * (y1 - y2)))

        return res if res != float('inf') else 0


class Solution:
    def minAreaRect(self, points):
        seen = set()
        res = float('inf')

        for (x1, y1) in points:
            for (x2, y2) in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))

        return 0 if res == float('inf') else res

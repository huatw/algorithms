# (M+N)log(N)
class Solution:
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters)

        r = 0
        for h in houses:
            idx = bisect.bisect_left(heaters, h)
            if idx == len(heaters):
                r = max(r, h - heaters[idx - 1])
            elif idx == 0:
                r = max(r, heaters[idx] - h)
            else:
                r = max(r, min(heaters[idx] - h, h - heaters[idx - 1]))
        return r